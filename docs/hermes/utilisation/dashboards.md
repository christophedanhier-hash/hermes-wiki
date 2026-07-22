# Dashboards et monitoring

Visualisez l'activité de votre assistant en temps réel avec des dashboards HTML autonomes, déployés sur GitHub Pages.

## Principe

Un dashboard est un fichier HTML statique (zéro JavaScript serveur, zéro backend) :

```
Script de collecte → JSON + HTML → Push GitHub Pages
                                      ↓
                    https://user.github.io/mon-dashboard/
```

**Avantages :** gratuit (GitHub Pages), accessible partout, aucun serveur à maintenir.

## Les dashboards de LEO

> ⚠️ **Mise à jour du 04/07/2026** : Les 7 dashboards pré-crash (LEO KPI, BAVI LEO, Machines, Crons, GitHub, n8n, Global) sont OBSOLÈTES et figés au 30/06/2026. NE PLUS les consulter.

LEO a **1 dashboard unifié** en production, généré par le collecteur `collect-v2.py` (8 sources — n8n retiré 13/07) :

| Dashboard | Contenu | URL | Collecte | Déploiement |
|-----------|---------|-----|----------|-------------|
| **LEO Dashboard** | Synthèse, Analyses, Infra, BAVI (20 KPI, 4 charts, 4 vaults) | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) | collect-v2.py */15 | deploy-dashboard.sh H:10 |

Scripts :
- `~/.hermes/profiles/leo-copilot/scripts/collect-v2.py` — collecteur unifié (state.db des 5 profils, infra, budget, vaults)
- `~/.hermes/profiles/leo-copilot/scripts/deploy-dashboard.sh` — génère HTML + push GitHub Pages

Cron ID `4d6ec4488b3c` dans le profil `leo-copilot`.

Tous sont générés par des scripts `no_agent` — **0$ de coût LLM** par mise à jour.

## Architecture technique

Chaque dashboard suit le même pattern :

1. **Un script de collecte** (Python) qui :
   - Récupère les données (API, fichiers, logs)
   - Génère un `index.html` avec Chart.js ou CSS pur

2. **Un cron no_agent** qui exécute le script toutes les 4h

3. **Un dépôt GitHub Pages** qui sert le HTML

### Script type

```python
#!/usr/bin/env python3
import json, subprocess
from pathlib import Path

# 1. Collecter les données
data = collecter_metriques()

# 2. Générer le HTML
html = generer_dashboard(data)

# 3. Écrire dans le repo
repo = Path("/tmp/mon-dashboard")
repo.joinpath("index.html").write_text(html)

# 4. Push sur GitHub
subprocess.run(["git", "-C", str(repo), "add", "."])
subprocess.run(["git", "-C", str(repo), "commit", "-m", "Màj dashboard"])
subprocess.run(["git", "-C", str(repo), "push", "origin", "main"])
```

### Déploiement

```bash
# 1. Créer le repo
gh repo create mon-dashboard --public

# 2. Activer GitHub Pages
echo '{"source":{"branch":"main","path":"/"}}' | \
  gh api repos/user/mon-dashboard/pages --input -

# 3. Cloner en local
git clone https://github.com/user/mon-dashboard.git /tmp/mon-dashboard

# 4. Configurer le cron
hermes cron create \
  --script deploy-dashboard.sh \
  --schedule "0 */4 * * *" \
  --name "mon-dashboard" \
  --no-agent
```

## Pitfalls

### 🔴 Pas de JavaScript si le navigateur flashe

Sur certains appareils (Chromebook, mobile), Chart.js en mode responsive peut causer un rafraîchissement en boucle. Solution : **remplacer Chart.js par un tableau CSS statique**.

```css
/* Au lieu d'un graphique JS : tableau statique */
.hist-table td.ok-cell { color: #22c55e; }
.hist-table td.err-cell { color: #ef4444; }
```

### 🔴 Gérer l'identité Git

Dans l'environnement minimal d'un cron, `git commit` échoue si l'identité n'est pas configurée :

```python
subprocess.run(["git", "config", "user.name", "MonAssistant"])
subprocess.run(["git", "config", "user.email", "assistant@exemple.com"])
```

### 🔴 Gérer l'authentification GitHub

Le cron n'a pas de TTY pour le flow OAuth Git. Passez le token dans l'URL :

```python
import os
tok = os.environ.get("GH_TOKEN")
if tok:
    remote = f"https://user:{tok}@github.com/user/repo.git"
    subprocess.run(["git", "remote", "set-url", "origin", remote])
```

### 🔴 Les repos locaux doivent être synchronisés

`dashboard-watch` vérifie l'âge du dernier commit **dans le repo local** pour déterminer si un dashboard est stale. Si votre script de déploiement push vers un clone temporaire (`/tmp/...`), le repo local ne sera jamais mis à jour et `dashboard-watch` déclenchera un redeploiement à chaque cycle.

**Solution :** après avoir pushé depuis `/tmp/`, faites un `git pull` dans le repo local :

```bash
cd ~/Projets_Dev/n8n-dashboard
git pull origin main
```

> 🐛 **Bug #16** — Cette cause racine a été corrigée sur le dashboard n8n (juin 2026).

### 🔴 Webhook budget pour n8n

> ⚠️ n8n retiré le 13/07/2026. Ce bloc est conservé pour référence. Si vous utilisiez n8n pour remplacer un cron Hermes, n8n tournait dans Docker et n'a pas accès direct au filesystem. Créez un **webhook HTTP** sur l'hôte :

> ⚠️ **Note 17/07/2026** : n8n a été retiré de LEO le 13/07/2026. Cette section est conservée à titre d'exemple.

```python
# budget-webhook.py — mini serveur HTTP
# POST /budget-update → écrit dans budget.json
# GET  /health        → status
```

Lancé en background (`python3 scripts/budget-webhook.py &`). n8n y POSTe les données collectées.

### 🔴 Budget désynchronisé

Si le budget affiché sur un dashboard ne correspond pas au `budget.json`, le cron `dashboard-watch` (voir `crons.md`) déclenche une alerte. Vérifiez que les clés lues par le script de déploiement correspondent exactement à celles du JSON :

```python
# Dans budget.json : "avg_daily", "total_spent" (pas "daily_spend")
# Dans le script : budget.get("avg_daily", 0)  # ✅ correct
```

## Surveillance automatique (dashboard-watch)

Un cron **dashboard-watch** (`scripts/dashboard-watch.py`) tourne toutes les 2h et vérifie :

1. **HTTP 200** — chaque dashboard répond
2. **Âge < 2h** — données fraîches
3. **Budget cohérent** — valeur affichée ≈ `budget.json` (écart max 1$)
4. **Redeploiement auto** — si stale ou 404, le script relance le déploiement
5. **Rebuild GH Pages** — après chaque push, appelle l'API pour forcer le rafraîchissement CDN

```python
# Extrait : rebuild GH Pages après push
subprocess.run(["gh", "api", f"repos/user/{repo}/pages/builds", "-X", "POST"])
```

## 🦁 Global Dashboard LEO (portail unique)

Depuis le 22/06/2026, LEO a un **portail unique** qui consolide tout en une seule page :
- 🔵 **Crons (41, 39 actifs)** — statut, historique (collect-v2)
- 📊 **1 Dashboard unifié** (leo-dashboard) — remplace les 7 anciens dashboards
- 💰 **Budget DeepSeek** — solde, jours restants
- 🖥️ **Ports** — dashboards 8765+9119, code-server 7681
- 🏛️ **BAVI LEO** — sessions, messages, tokens
- 🖥️ **Machines (3)** — statut en ligne/hors ligne
- 🚨 **Alertes** — dernières anomalies détectées
- 🔗 **Liens rapides** — accès au dashboard unifié

**Avantages :**
- ✅ **Plus aucun rapport Telegram** — collect-v2 + déploiement horaire livrent en local
- ✅ **Un seul bookmark** au lieu de 7
- ✅ **Collecte */15, déploiement H:10** — 0$ de coût LLM
- ✅ **Auto-déploiement GH Pages** via deploy-dashboard.sh

- **Usage LLM** — requêtes/jour, tokens consommés, coût estimé
- **Système** — CPU, RAM, disque, uptime de votre serveur
- **Projets** — Suivi d'avancement, tâches complétées
- **Réseau** — Latence, bande passante, statut des services

## Pour aller plus loin

- Voir `03-utilisation/crons.md` pour le déploiement automatisé
- Voir `03-utilisation/architecture-leo.md` pour la vue complète (schéma Mermaid, interactions, filets)
- Voir `exemples/LEO.md` pour les dashboards en production
*Document mis à jour le 18/07/2026 à 12:00 — Léo 🦁*

---

> 🤖 Dernier audit : 22/07/2026 à 09:00 (UTC+2)



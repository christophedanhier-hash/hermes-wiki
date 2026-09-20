# Dashboards, supervision et interfaces locales

> **Page canonique de référence :** [`hermes/architecture.md`](../architecture.md). Mesures vérifiées le **20/09/2026**.

Visualisez l'activité de votre assistant, l'état des services et les métriques des profils en temps réel via des dashboards HTML autonomes et des services web dédiés.

## Principe

Les dashboards et interfaces de LEO combinent des pages HTML statiques légères (zéro backend lourd, hébergeables en local ou sur GitHub Pages) et des services applicatifs spécialisés :

```
Script de collecte (no_agent) → JSON + HTML → Servi localement ou GitHub Pages
                                            ↓
                             http://localhost:8765/dashboard
```

**Avantages :** exécution légère, aucun coût LLM pour les collectes récurrentes, portabilité complète.

---

## Les services et dashboards observés sur LEO

Au 20/09/2026, les services et interfaces réseau observés sont :

| Service | Port | Portée observée | Fonction & Contenu |
|---|---:|---|---|
| **Panel LEO** | 8765 | Accessible réseau | Métriques globales, crons, supervision des 6 profils, vaults |
| **Leo Docs** | 8766 | Accessible réseau | Explorateur documentaire et consultation des wikis |
| **Hermes Dashboard** | 9119 | Accessible réseau | Interface native Hermes Agent |
| **My Émile IA** | 8793 | Localhost | Workbench métier et pédagogique |

### Collecte unifiée (`collect-v2.py`)

Les métriques consolidées sur le Panel LEO sont générées par :
- `~/.hermes/profiles/michel/scripts/collect-v2.py` — collecteur unifié (bases des profils opérationnels, métriques système, budget LLM, état des vaults) ;
- `~/.hermes/profiles/michel/scripts/deploy-dashboard.sh` — génération du HTML et mise à disposition locale ou déploiement distant.

Ces collectes sont planifiées sous forme de jobs `no_agent` dans l'ordonnanceur Michel (**0$ de consommation de tokens**).

---

## Architecture technique

Chaque tableau de bord suit le même cycle :

1. **Un script de collecte** (Python) qui :
   - Récupère les données (fichiers d'état des profils, logs, statut système, API) ;
   - Génère un `index.html` avec Chart.js ou tableaux CSS purs.

2. **Un cron `no_agent`** qui exécute le script périodiquement sans solliciter de modèle d'IA.

3. **Un serveur local ou GitHub Pages** qui sert le document HTML.

### Script type de génération

```python
#!/usr/bin/env python3
import json, subprocess
from pathlib import Path

# 1. Collecter les données
data = collecter_metriques()

# 2. Générer le HTML
html = generer_dashboard(data)

# 3. Écrire dans le dépôt ou répertoire servi
repo = Path("/tmp/mon-dashboard")
repo.joinpath("index.html").write_text(html, encoding="utf-8")

# 4. Déploiement Git si nécessaire
subprocess.run(["git", "-C", str(repo), "add", "."])
subprocess.run(["git", "-C", str(repo), "commit", "-m", "Màj dashboard"])
subprocess.run(["git", "-C", str(repo), "push", "origin", "main"])
```

### Exemple de configuration cron

```bash
hermes cron create \
  --script deploy-dashboard.sh \
  --schedule "10 * * * *" \
  --name "mon-dashboard" \
  --no-agent
```

---

## Bonnes pratiques & pièges évités (Pitfalls)

### 🔴 Éviter le rechargement en boucle sur mobile
Sur certains appareils légers, Chart.js en mode responsive peut provoquer un rafraîchissement continu. La solution éprouvée consiste à privilégier des **tableaux CSS statiques** pour l'affichage synthétique des statuts :

```css
.hist-table td.ok-cell { color: #22c55e; }
.hist-table td.err-cell { color: #ef4444; }
```

### 🔴 Identité Git dans l'environnement minimal cron
Dans l'environnement d'exécution isolé d'un cron, `git commit` échoue si l'identité n'est pas explicite :

```python
subprocess.run(["git", "config", "user.name", "Michel"])
subprocess.run(["git", "config", "user.email", "michel@local"])
```

### 🔴 Synchronisation des dépôts locaux
`dashboard-watch` vérifie la fraîcheur des commits locaux. Si un déploiement pousse depuis un clone temporaire (`/tmp/...`), le dépôt local doit être synchronisé via un `git pull` pour éviter des redéclenchements inutiles.

---

## Surveillance et pipelines documentaires

La supervision de LEO ne se limite pas à l'affichage web ; elle s'intègre aux pipelines documentaires automatisés :

- **`docs-update`** : mise à jour des documentations structurantes ;
- **`doc-watch-auto`** : surveillance automatique des référentiels (Wiki Hermes, BAVI_LEO, guide Christophe) via `doc-watch-snapshot.py` ;
- **`doc-crons-sync`** : synchronisation périodique de l'inventaire des crons ;
- **Auto-commit wiki** : traçabilité des modifications.

### Surveillance automatique (`dashboard-watch.py`)

Un script de contrôle vérifie à intervalles réguliers :
1. **Disponibilité HTTP (code 200)** des interfaces servies ;
2. **Fraîcheur des données** (< 2h) ;
3. **Cohérence des métriques de budget** entre fichiers JSON et affichage.

---

## Synthèse de la supervision LEO

Au 20/09/2026, la console et le portail centralisent :
- 🔵 **Crons ordonnancés** : 72 jobs dans `profiles/michel/cron/jobs.json` (71 activés, 70 `no_agent`, 2 LLM) ;
- 📊 **Panel LEO (port 8765)** : vue unifiée des métriques, sessions et états de santé ;
- 📚 **Leo Docs (port 8766)** : accès centralisé à la documentation et aux wikis ;
- 🤖 **Hermes Dashboard (port 9119)** : console d'administration Hermes ;
- 🎓 **My Émile IA (port 8793)** : interface locale dédiée au travail pédagogique ;
- 💰 **Suivi des coûts LLM** : consommation maîtrisée sur Azure Foundry et OpenRouter, coût nul pour les automatisations directes ;
- 🚨 **Suivi opérationnel** : l'unité systemd Michel en boucle d'auto-restart (conflit de PID déjà actif) est suivie au niveau runbook infra.

---

## Contexte historique (daté)

> 📜 **Historique des dashboards (juin - juillet 2026) :**
>
> - **30/06/2026 :** Abandon des 7 anciens dashboards fragmentés (LEO KPI, BAVI LEO, Machines, Crons, GitHub, Global) au profit d'une interface unifiée pilotée par `collect-v2.py`.
> - **Historique des ports et services :** Les configurations antérieures mentionnaient des ports intermédiaires (comme le port code-server 7681) qui ne font plus partie des services actifs mesurés au 20/09/2026.
> - **Paliers de crons :** Les mentions historiques de 45, 49 ou 58 crons correspondent à des étapes de montée en charge antérieures à l'inventaire stabilisé actuel.

---

## Pour aller plus loin

- Consulter [`architecture.md`](../architecture.md) pour la description canonique du système
- Consulter [`architecture-leo.md`](architecture-leo.md) pour le schéma d'ensemble des flux
- Consulter [`bots-telegram.md`](bots-telegram.md) pour les interfaces Telegram associées
- Consulter [`profiles.md`](../configuration/profiles.md) pour la configuration des profils

---

> 🤖 Dernière mesure vérifiée : **20/09/2026** — LEO et Michel. Source de vérité : `ss -ltnp`, processus actifs et `architecture.md`.

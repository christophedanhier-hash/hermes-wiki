# L'architecture LEO — Exemple concret

LEO est l'assistant personnel de Christophe. Ce document détaille son architecture pour servir d'exemple à ceux qui veulent construire le leur.

## Identité

```
Nom : LEO
Type : Majordome numérique
Hôte : Linux (Debian-like)
Canal principal : Telegram
Profils : 1 seul (default)
```

## Providers LLM

| Provider | Rôle | Coût |
|----------|------|------|
| DeepSeek 🤖 | Principal (Telegram, conversations, tâches complexes) | Payant ($42 de solde) |
| Ollama 🏠 | Local, gratuit (batch, traitement bulk, qwen2.5:7b) | Gratuit (pas de GPU (CPU)) |
| Gemini ⚡ | Fallback automatique | Gratuit (quota API) |

## Communications

LEO communique uniquement par **Telegram** (pas d'autre canal). L'email est utilisé **en sortie uniquement** (LEO peut envoyer des emails depuis `leodanhieria@gmail.com`, mais ne reçoit pas de consignes par email).

## Tâches quotidiennes

### Collecte & Déploiement

```yaml
H:10 — collect-v2.py (9 sources unifiées)
  - sessions, budget, crons, infra, n8n, github, bavi, services, vaults
  - Déploiement toutes les heures via leo-copilot
  Coût: 0 € (no_agent)
```

### Crons

| Cron | Horaire | Type | Coût | Description |
|------|---------|------|------|-------------|
| `collect-v2` | **H:10** | 🔧 Script | **0$** | Collecte unifiée 9 sources → leo-dashboard |
| `daily-backup` | 06:00 | 🔧 Script | **0$** | Backup fichiers critiques |
| `drive-sync` | 18:00 | 🔧 Script | **0$** | Sync Drive ↔ GitHub |
| `credentials-check` | Lun 09:00 | 🔧 Script | **0$** | Vérification tokens OAuth |
| `doc-watch-auto` | 00/06/12/18 | 🔧 Script | **0$** | Surveillance docs 5 wikis |
| `Classifieur emails` | 30m | 🧠 Ollama | **0$** 🏠 | Classification Gmail |
| Veille IA (phase 1) | 07:30 | 🔧 Script | **0$** | Collecte RSS 11 sources |
| Veille IA (phase 2) | 08:00 | 🤖 DeepSeek | ~0.05$ | Analyse + email Cowork |
| `check-hermes-update` | 09:00 | 🔧 Script | **0$** | Vérification nouvelle version Hermes |
| `dashboard-watch` | */2h | 🔧 Script | **0$** | Vérification leo-dashboard |

### Workflows n8n (3)

| Workflow n8n | Rôle |
|-------------|------|
| Drive → Issue | Surveillance Drive → issue GitHub |
| Gardien du Drive | Protection documents Google Docs |
| Save Contacts | Sauvegarde des contacts Google |

### Dashboard (1 seul)

| Dashboard | Technologie | Màj | Lien |
|-----------|-------------|-----|------|
| 🌍 leo-dashboard | HTML + Chart.js | H:10 | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) |

### Vaults Obsidian (4)

| Vault | Usage |
|-------|-------|
| leo | Vault personnel LEO |
| default | Vault par défaut Hermes |
| emile | Vault pédagogie Émile |
| bavi | Vault bureaux BAVI |

Tous les scripts de déploiement incluent :
- `--allow-empty` + `run_id` dans le footer pour éviter "nothing to commit"
- Force-push fallback si le push est rejeté
- **Rebuild GH Pages API** après push (CDN forcé)
- Validation des clés `budget.json` au déploiement

## Règles de fonctionnement

### 1. Règle #1 : Réfléchir avant d'agir

Avant chaque action impliquant un choix technique, identifier 2-3 approches, peser le pour/contre, choisir la meilleure. La précipitation est la première cause d'erreur.

### 2. Arbitrage LLM (3 niveaux)

```
Tâche → Script pur ? → no_agent (0 token)
       → A besoin d'un LLM ? → Ollama (gratuit)
                              → Gemini (fallback)
                              → DeepSeek (payant, premium)
       → Jamais sacrifier la qualité pour économiser
```

### 3. Anti-régression

- **1 envoi max** — email ou action : UNE SEULE tentative
- **Pas de réessai** après échec sans accord explicite
- **Corrections → skills** (pas en mémoire passagère)
- **Zéro répétition** — réponse concise, pas de blabla

### 4. Un seul profil

LEO a vécu la perte d'accès Telegram lors d'un basculement de profil. Leçon apprise : **un seul profil, un seul gateway, tout dedans**.

### 5. Sécurité email

- Envoi UNIQUEMENT depuis `leodanhieria@gmail.com`
- JAMAIS depuis `christophe.danhier@gmail.com`
- Christophe TOUJOURS en CC
- Si erreur : STOP net, ne pas réessayer

## Structure des fichiers

```
/opt/data/
├── config.yaml           → Configuration Hermes
├── .env                  → Variables d'environnement (clés API)
├── google_token.json     → Token OAuth Google
├── hermes-backup.py      → Script de backup
├── deploy_dashboard.py   → Script déploiement dashboard KPI
├── deploy_machines.py    → Script déploiement métriques machines
├── update_budget_v6.py   → Script relevé budget DeepSeek
├── update_machines_kpi.py→ Script collecte métriques machines
└── scripts/
    ├── run-backup.sh
    ├── run-budget.sh
    ├── run-machines-kpi.sh
    ├── run-dashboard.sh
    ├── run-leo-dashboard.sh
    ├── run-leo-dashboard.sh
    └── deploy-leo-dashboard.py
```

## Leçons apprises

### 12/06/2026 — Trop de profils

**Problème :** Création d'un profil `local` pour Ollama. Arrêt du gateway `local` = perte d'accès Telegram.

**Solution :** Unifier dans un seul profil, Ollama par API directe. Fiabilité > flexibilité.

### 13/06/2026 — Précipitation

**Problème :** Actions sans réflexion préalable = régressions (mauvais token, erreur OAuth, envoi multiple d'email).

**Solution :** Règle #1 : réfléchir avant d'agir. Toujours.

### 14/06/2026 — Crons instables

**Problème :** Crons qui utilisaient le mauvais Python, scripts introuvables, identité Git manquante, push qui échoue.

**Solution :** Uniformisation : wrappers shell + no_agent + identité Git et token dans le script.

## Inspirez-vous, ne copiez pas

LEO est taillé sur mesure pour Christophe. Votre assistant aura ses propres besoins, règles et personnalité. Prenez ce qui vous est utile, adaptez le reste.

## Architecture Système

### 1. Infrastructure
L'infrastructure du système est composée des éléments suivants :

- **Host LEO** : i7-7700K, 22GB de RAM
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Telegram Client** : Chromebook pour la communication Telegram
- **Modèles IA** :
  - Ollama qwen2.5:7b

### 2. Budget API
Le budget actuel pour les API est de $54.57, avec des seuils d'alerte fixés à $30 et un seuil de stoppage à $10. Le routage des requêtes API se fait dans l'ordre suivant : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs
Le système exécute actuellement 14 tâches cron, dont les détails sont listés ci-dessous :

| **Nom de la Tâche** | **Horaires d'exécution** | **Script/Action** |
|---------------------|-------------------------|------------------|
| LEO Full Backup quotidien (complet) | `0 2 * * *` | - |
| 🔍 Veille IA quotidienne | `0 7 * * *` | - |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | - |
| 📧 Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | gmail_classifier.py |
| 📝 docs-update | `0 */4 * * *` | run-docs-update.sh |
| 🔄 drive-sync | `0 * * * *` | drive-sync.sh |
| 📖 doc-watch-auto | `0 */6 * * *` | doc-watch-auto.sh |
| 🩺 Auto-Heal Agent | `*/15 * * * *` | - |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh |
| 📦 Archive Watch — leo-tracker | `0 */6 * * *` | agent-pro-archive.sh |
| 🩺 Data Freshness Watchdog | `*/5 * * * *` | check-freshness.sh |
| 📊 Unified Collector v2 | `*/15 * * * *` | - |
| 🚀 Deploy Unified Dashboard | `2,17,32,47 * * * *` | deploy-dashboard.sh |
| 🏗️ GitHub Pages Build Monitor | `*/5 * * * *` | check-pages-builds.py |

### 4. Dashboards
Le système met en place plusieurs dashboards pour surveiller et optimiser les opérations :

- **crons** : Moniteur des tâches cron
- **github** : Suivi des builds de GitHub Pages
- **machines** : Surveillance des machines hôtes
- **wiki** : Page wiki MkDocs

### 5. Sessions & Utilisation
Le système enregistre les sessions et l'utilisation suivantes :

- **Total sessions** : 191
- **Total messages** : 8836
- **Sessions Telegram** : 8

La taille de la base de données est actuellement de 59.5 MB.

--- 

Ce document fournit une vue d'ensemble de l'architecture système, des ressources utilisées et des tâches en cours d'exécution.
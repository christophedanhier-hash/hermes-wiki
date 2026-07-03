## Architecture Système

### 1. Infrastructure
L'infrastructure du système est composée des éléments suivants :

- **Host LEO**: i7-7700K, 22GB de RAM
- **Container Debian 13** : Python 3.13, DeepSeek V4 Flash, Chromebook Telegram, Ollama qwen2.5:7b

### 2. Budget API
Le budget actuel pour les APIs est de $50.8. Les seuils d'alerte sont définis à $30 et le stop à $10. Le routage des requêtes est organisé comme suit : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs
Il y a actuellement 13 crons en activité :

| **Nom du Cron** | **Horaires** | **Scripts/Actions** |
| --- | --- | --- |
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
| 📊 Unified Collector v2 | `*/15 * * * *` | - |
| 🚀 Deploy Unified Dashboard | `15 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |

### 4. Dashboards
Les dashboards suivants sont mis à jour régulièrement :

- **crons**
- **github**
- **machines**
- **wiki**

### 5. Sessions & Utilisation
Le système enregistre les sessions et l'utilisation comme suit :

- **Total de sessions** : 629
- **Total de messages** : 14,431
- **Sessions Telegram** : 10

La taille totale de la base de données est de 100.9 MB.
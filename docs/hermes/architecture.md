## Architecture Système

### 1. Infrastructure
L'infrastructure de LEO est composée du suivant :
- **Host LEO**: i7-7700K avec 22GB de RAM.
- **Container Debian 13** : Python 3.13, DeepSeek V4 Flash, Chromebook Telegram, Ollama qwen2.5:7b.

### 2. Budget API
Le budget actuel pour les APIs est de $51.46 avec des seuils d'alerte fixés à $30 et un stop à $10. Le routage est configuré comme suit : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs (13)
| **Nom** | **Horaires** | **Script** |
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
Les dashboards actuellement utilisés sont :
- crons
- github
- machines
- wiki

### 5. Sessions & Utilisation
- **Total sessions**: 483
- **Total messages**: 13210
- **Sessions Telegram**: 9

La taille de la base de données est de 89.1 MB.
## Architecture Système

### 1. Infrastructure
- **Host LEO**: i7-7700K, 22GB RAM
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Chromebook Telegram**
- **Ollama qwen2.5:7b**

### 2. Budget API
- Balance DeepSeek: $42.09
- Seuils d'alerte: $30
- Stop budget: $10
- Routage Ollama → Gemini → DeepSeek

### 3. Crons Actifs (28)
| **Tâche** | **Heure de lancement** | **Script** |
|-----------|------------------------|------------|
| 🔍 Veille IA quotidienne | `0 7 * * *` | send_veille_smtp.py |
| 🔄 Déploiement auto tofdan.be | `5 * * * *` | deploy-tofdan.sh |
| 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | gmail_classifier.py |
| ✍️ docs-update | `0 */4 * * *` | run-docs-update.sh |
| 🔄 drive-sync | `0 * * * *` | drive-sync.sh |
| 📖 doc-watch-auto | `0 */6 * * *` | doc-watch-auto.sh |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh |
| 📊 Unified Collector v2 | `*/15 * * * *` |  |
| 🚀 Deploy Unified Dashboard | `10 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |
| 🛡️ LEO Health Check (script) | `2,17,32,47 * * * *` | leo-health-check.py |
| 📒 vault-daily-journal (vault-leo) | `0 23 * * *` |  |
| 📒 vault-default-daily-journal | `5 23 * * *` |  |
| 🔧 LEO Maintenance quotidienne | `0 3 * * *` | leo-daily-maintenance.py |
| 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` |

### 4. Dashboards
- crons
- github
- machines
- wiki

### 5. Sessions & Utilisation
- Total sessions: 1509
- Total messages: 23767
- Telegram: 15 sessions
- Database size: 185.8 MB
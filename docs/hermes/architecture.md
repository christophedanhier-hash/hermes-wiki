## Architecture Système

### 1. Infrastructure

- **Host LEO**: i7-7700K avec 22GB de RAM
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Chromebook Telegram**
- **Ollama qwen2.5:7b**

### 2. Budget API

- **Balance DeepSeek**: $47.31
- **Seuils d'alerte**: $30
- **Stop**: $10
- **Routage**: Ollama → Gemini → DeepSeek

### 3. Crons Actifs (19)

| **Tâche** | **Horodatage** | **Script** |
|-----------|----------------|------------|
| 🔍 Veille IA quotidienne | `0 7 * * *` | run-iae-daily.sh |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | deploy-tofdan.sh |
| 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | gmail_classifier.py |
| 📝 docs-update | `0 */4 * * *` | run-docs-update.sh |
| 🔄 drive-sync | `0 * * * *` | drive-sync.sh |
| 📖 doc-watch-auto | `0 */6 * * *` | doc-watch-auto.sh |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh |
| 📊 Unified Collector v2 | `*/15 * * * *` | unified_collector_v2.py |
| 🚀 Deploy Unified Dashboard | `10 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |
| 🛡️ LEO Health Check (script) | `*/15 * * * *` | leo-health-check.py |
| 📒 vault-daily-journal (vault-leo) | `0 23 * * *` | vault-daily-journal.sh |
| 📒 vault-default-daily-journal | `0 23 * * *` | vault-default-daily-journal.sh |
| 🔧 LEO Maintenance quotidienne | `0 3 * * *` | leo-daily-maintenance.py |
| 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | leo-full-backup.py |

### 4. Dashboards

- **crons**
- **github**
- **machines**
- **wiki**

### 5. Sessions & Utilisation

- **Total sessions**: 1115
- **Total messages**: 18682
- **Telegram**: 13 sessions
- **Database size**: 141.6 MB
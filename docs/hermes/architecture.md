# Architecture Système

## 1. Infrastructure
- **Host LEO**: Processeur récent, RAM suffisante
- **Container**: Debian 13, Python 3.13, DeepSeek V4 Flash
- **Telegram Client**: Chromebook Telegram
- **Modèles d'IA**: Ollama qwen2.5:7b

## 2. Budget API
- **Balance DeepSeek**: $46.1
- **Seuils d'alerte**: $30 (avertissement), $10 (arrêt)
- **Routage**: Ollama → Gemini → DeepSeek

## 3. Crons Actifs (22)
| **Tâche** | **Horodatage** | **Script** |
| --- | --- | --- |
| 🔍 Veille IA quotidienne | `0 7 * * *` | send_veille_smtp.py |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | deploy-tofdan.sh |
| 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | gmail_classifier.py |
| 📝 docs-update | `0 */4 * * *` | run-docs-update.sh |
| 🔄 drive-sync | `0 * * * *` | drive-sync.sh |
| 📖 doc-watch-auto | `0 */6 * * *` | doc-watch-auto.sh |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh |
| 📊 Unified Collector v2 | `*/15 * * * *` |  |
| 🚀 Deploy Unified Dashboard | `10 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |
| 🛡️ LEO Health Check (script) | `*/15 * * * *` | leo-health-check.py |
| 📒 vault-daily-journal (vault-leo) | `0 23 * * *` |  |
| 📒 vault-default-daily-journal | `0 23 * * *` |  |
| 🔧 LEO Maintenance quotidienne | `0 3 * * *` | leo-daily-maintenance.py |
| 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | leo-backup.sh |

## 4. Dashboards
- **crons**: Moniteur des tâches planifiées
- **github**: Suivi des dépôts et contributions GitHub
- **machines**: Surveillance de l'état des machines
- **wiki**: Gestion et mise à jour du wiki

## 5. Sessions & Utilisation
- **Total sessions**: 1206
- **Total messages**: 19521
- **Telegram**: 14 sessions
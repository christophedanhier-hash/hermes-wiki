# Architecture Système

## 1. Infrastructure
- **Host LEO**: i7-7700K, 22GB RAM
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Telegram Client**: Chromebook Telegram
- **Model AI**: Ollama qwen2.5:7b

## 2. Budget API
- **Balance DeepSeek**: $45.69
- **Seuils Alertes**: $30 (alerte), $10 (arrêt)
- **Routage**: Ollama → Gemini → DeepSeek

## 3. Crons Actifs (23)
| **Tâche** | **Horaires** | **Script** |
|-----------|--------------|------------|
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
| 🔒 vault-daily-journal (vault-leo) | `0 23 * * *` |  |
| 🔒 vault-default-daily-journal | `0 23 * * *` |  |
| 🔧 LEO Maintenance quotidienne | `0 3 * * *` | leo-daily-maintenance.py |
| 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | leo-ful

## 4. Dashboards
- **crons**: Moniteur des tâches cron en cours d'exécution.
- **github**: Suivi des modifications et des contributions sur les repositories GitHub.
- **machines**: Surveillance de l'état des machines et du système.
- **wiki**: Documentation et informations sur la structure et le fonctionnement du système.

## 5. Sessions & Utilisation
- **Total sessions**: 1271
- **Total messages**: 19864
- **Telegram**: 14 sessions
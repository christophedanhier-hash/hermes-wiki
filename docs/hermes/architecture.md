# Architecture Système

## 1. Infrastructure
LEO est hébergé sur un host i7-7700K avec 22GB de RAM, exécutant Debian 13 et Python 3.13. L'application DeepSeek V4 Flash y est déployée, ainsi que le Telegram Chromebook pour les communications externes. Ollama qwen2.5:7b est également intégré dans ce système.

## 2. Budget API
- **Balance DeepSeek :** $47.66
- **Seuils d'alerte :** $30 (pour des alertes), $10 (pour le stop)
- **Routage :** Ollama → Gemini → DeepSeek

## 3. Crons Actifs
| **Nom du Cron** | **Heure de Déclenchement** | **Commande Exécutée** |
|-----------------|----------------------------|-----------------------|
| 🔍 Veille IA quotidienne | `0 7 * * *` | - |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | /opt/data/scripts/deploy-tofdan.sh |
| 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | gmail_classifier.py |
| ✍️ docs-update | `0 */4 * * *` | run-docs-update.sh |
| 🔄 drive-sync | `0 * * * *` | drive-sync.sh |
| 📖 doc-watch-auto | `0 */6 * * *` | doc-watch-auto.sh |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh |
| 📊 Unified Collector v2 | `*/15 * * * *` | - |
| 🚀 Deploy Unified Dashboard | `10 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |
| 🛡️ LEO Health Check (script) | `*/15 * * * *` | leo-health-check.py |
| 📒 vault-daily-journal (vault-leo) | `0 23 * * *` | - |
| 📒 vault-default-daily-journal | `0 23 * * *` | - |
| 🔧 LEO Maintenance quotidienne | `0 3 * * *` | leo-daily-maintenance.py |
| 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | leo-ful

## 4. Dashboards
Les dashboards couvrent les sections suivantes :
- **crons**
- **github**
- **machines**
- **wiki**

## 5. Sessions & Utilisation
- **Total des sessions :** 1062
- **Total des messages :** 18104
- **Sessions Telegram :** 13

La taille de la base de données est actuellement de 134.2 MB.
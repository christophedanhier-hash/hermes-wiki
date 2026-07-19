# Architecture Système

## 1. Infrastructure
- **Host LEO**: i7-7700K, 22GB RAM
- **Container**: Debian 13, Python 3.14, DeepSeek V4 Flash
- **Telegram Client**: Chromebook Telegram
- **Model AI**: DeepSeek V4 Flash/Pro, Ollama qwen2.5:7b, Gemini 3.5 Flash (fallback)

## 2. Budget API
- Balance: $41.83 (solde actuel) — Coût total : ~$19.97
- Seuils d'alerte: $30
- Stop: $10
- Routage: DeepSeek → Gemini → Ollama

## 3. Crons Actifs (38)
| **Tâche** | **Horodatage** | **Script** |
| --- | --- | --- |
| 🔍 Veille IA quotidienne | `0 7 * * *` | send_veille_smtp.py |
| 🔄 Déploiement auto tofdan.be | `5 * * * *` | deploy-tofdan.sh |
| 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | gmail_classifier.py |
| ✍️ docs-update | `0 */4 * * *` | run-docs-update.sh |
| 🔄 drive-sync | `0 * * * *` | drive-sync.sh |
| 📖 doc-watch-auto | `0 */6 * * *` | doc-watch-auto.sh |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh |
| 📊 Unified Collector v2 | `*/15 * * * *` | collect-v2.py |
| 🚀 Deploy Unified Dashboard | `10 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |
| 🛡️ LEO Health Check (script) | `2,17,32,47 * * * *` | leo-health-check.py |
| 📒 Journaux Quotidiens | `0 23 * * *` | vault-daily-journal |
| 🔧 LEO Maintenance quotidienne | `0 3 * * *` | leo-daily-maintenance.py |
| 💾 LEO Backup quotidien → GDrive | `0 6 * * *` | leo-backup.sh |
| 🔄 Gateway Auto-Restart | toutes les heures | gateway-restart |
| 📡 Machine KPI Collector | `*/15 * * * *` | machine-kpi.py |
| 📝 Audit rédactionnel unifié | quotidien | audit-redactionnel.sh |
| 🛡️ Watchdog BAVI-LEO | `*/5 * * * *` | watchdog-bavi.sh |
| 🖥️ Dashboards Watchdog | `*/2 * * * *` | dashboards-watchdog.sh |
| 🔄 Rebuild Wiki BAVI/Voyages | quotidien | rebuild-wiki.sh |
| 💾 Recovery State Export GDrive | horaire | recovery-export.sh |
| 📋 doc-crons-sync | quotidien | doc-crons-sync.sh |
| 📦 Auto-Archive BAVI LEO | `*/5 * * * *` | auto-archive.py |
| 🔍 Audit Infra | quotidien | audit-infra.sh |
| 🩺 Cron Watchdog v2 | continu | cron-watchdog-v2 |
| Gardien du Drive | continu | gardien-drive.sh |
| Drive → Issue GitHub | sur détection | drive-to-issue.py |
| Collecte Viessmann | `*/30 * * * *` | viessmann-collect.py |
| 📊 Agrégation Énergie horaire | `5 * * * *` | energy-aggregate.py |
| ⚡ HomeWizard P1 | continu | homewizard-p1.py |
| 📷 Surveillance caméras | continu | camera-surveillance.py |
| 📧 Check Gmail (important) | `*/30 * * * *` | gmail-check.sh |
| 🩺 GitHub Actions Watchdog | `*/10 * * * *` | github-actions-watchdog.sh |
| 🔄 Refresh Google Tokens | `*/50 * * * *` | refresh-tokens.sh |
| 💾 Save Contacts | quotidien | save-contacts.sh |
| 📦 Cron Log Archiver | horaire | log-archiver.sh |
| 📊 Synthèse Hebdomadaire LEO | hebdo | synthese-hebdo.sh |
| 🔄 Auto-commit wikis | horaire | auto-commit-wikis.sh |

## 4. Dashboards
- crons
- github
- machines
- wiki

## 5. Sessions & Utilisation
- Total sessions: >1500
- Total messages: >24000
- Telegram: 5 bots actifs
- Dashboard LEO: port 8765 (panel) + 9119 (Hermes dashboard)

---

> 🤖 Dernier audit : 19/07/2026 à 06:10 (UTC+2)
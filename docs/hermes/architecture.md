# Architecture Système

## 1. Infrastructure
- **Host LEO**: i7-7700K, 22GB RAM
- **Container**: Debian 13, Python 3.14, DeepSeek V4 Flash
- **Telegram Client**: Chromebook Telegram
|- **Model AI**: DeepSeek (v4-flash/v4-pro), fallback gemini-3.5-flash → qwen2.5:7b (Ollama local)

## 2. Budget API
- Balance: $41.83 (solde actuel) — Coût total : ~$19.97
- Seuils d'alerte: $30
- Stop: $10
- Routage: DeepSeek → Gemini → Ollama

## 3. Crons Actifs (41 configurés, 39 actifs, 2 en pause)

| # | **Tâche** | **Horodatage** | **Script réel** | **Statut** |
|---:|---|:---:|---|:---:|
| 1 | 🔍 Veille IA quotidienne | `0 7 * * *` | run-veille-ia-wrapper.sh | ⏸️ Paused |
| 2 | 🔄 Déploiement auto tofdan.be | `5 * * * *` | deploy-tofdan.sh | ✅ |
| 3 | 📧 Email Classifier (inbox zero) | `*/30 * * * *` | gmail_classifier-wrapper.sh | ✅ |
| 4 | 📝 docs-update | `0 */4 * * *` | run-docs-update.sh | ✅ |
| 5 | 🔄 drive-sync | `0 * * * *` | drive-sync.sh | ✅ |
| 6 | 📋 Doc Watch Auto | `*/2 * * * *` | doc-watch-auto.sh | ✅ |
| 7 | 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh | ✅ |
| 8 | 📊 Unified Collector v2 | `*/15 * * * *` | collect-v2.py | ✅ |
| 9 | 💰 Budget Alert | `0 8,20 * * *` | budget-alert-wrapper.sh | ✅ |
| 10 | 🛡️ LEO Health Check | `2,17,32,47 * * * *` | leo-health-check.py | ✅ |
| 11 | 🔧 LEO Maintenance quotidienne | `0 3 * * *` | leo-daily-maintenance.py | ✅ |
| 12 | 💾 LEO Backup quotidien → GDrive | `0 6 * * *` | leo-full-backup.py | ✅ |
| 13 | 📦 Auto-Archive BAVI LEO | toutes les 5m | auto-archive-wrapper.sh | ✅ |
| 14 | 🔄 Auto-commit wikis | `0 * * * *` | auto-commit-repos.sh | ✅ |
| 15 | 🔄 Refresh Google Tokens | `*/50 * * * *` | refresh_google_tokens.py | ✅ |
| 16 | 🦺 GitHub Actions Watchdog | `4,19,34,49 * * * *` | github_workflow_watchdog.py | ✅ |
| 17 | 📋 doc-crons-sync | `0 */6 * * *` | run-doc-crons-sync.sh | ✅ |
| 18 | 📊 Synthèse Hebdomadaire LEO | Dimanche 20h | synthese_hebdo.py | ✅ |
| 19 | 🔄 Rebuild Wiki BAVI local | `*/15 * * * *` | rebuild-wiki.sh | ✅ |
| 20 | 🔄 Rebuild Wiki Voyages local | `15 * * * *` | rebuild-voyages.sh | ✅ |
| 21 | 📡 Machine KPI Collector | `*/5 * * * *` | machine-kpi.py | ✅ |
| 22 | 🔄 Gateway Auto-Restart | `*/15 * * * *` | gateway-watchdog.sh | ✅ |
| 23 | 💾 Recovery State Export → GDrive | `30 * * * *` | export-recovery-state.py | ✅ |
| 24 | 📷 Surveillance caméras → Telegram | `*/5 * * * *` | camera-motion-alert.py | ✅ |
| 25 | ⚡ Énergie — HomeWizard P1 | `*/2 * * * *` | collect-energy.py | ✅ |
| 26 | 🛡️ Watchdog BAVI-LEO | `*/5 * * * *` | bavi-watchdog.py | ✅ |
| 27 | Collecte Viessmann | `*/5 * * * *` | collect-viessmann.py | ⏸️ Paused |
| 28 | Gardien du Drive | `0 */6 * * *` | gardien-drive-wrapper.sh | ✅ |
| 29 | Drive → Issue GitHub | `*/30 * * * *` | drive-issue-wrapper.sh | ✅ |
| 30 | Save Contacts | `*/15 * * * *` | save-contacts-wrapper.sh | ✅ |
| 31 | 🖥️ Dashboards Watchdog (8765+9119) | `*/2 * * * *` | dashboards-watchdog.sh | ✅ |
| 32 | 🦺 Cron Watchdog v2 | `*/15 * * * *` | cron-watchdog-wrapper.sh | ✅ |
| 33 | 📓 Journaux Quotidiens (10 emplacements) | `0 23 * * *` | cron job agent (obsidian skill) | ✅ |
| 34 | 📧 Check Gmail — importants | toutes les 30m | check-gmail.py | ✅ |
| 35 | 🔍 Audit Infra (cohérence globale) | `0 * * * *` | infra-audit.py | ✅ |
| 36 | 📦 Cron Log Archiver | `15 * * * *` | cron-log-archiver.py | ✅ |
| 37 | 📊 Agrégation Énergie horaire | `0 * * * *` | energy-aggregate.py | ✅ |
| 38 | 📝 Audit rédactionnel unifié | `0 6 * * *` | cron job agent | ✅ |
| 39 | 📋 Sync Contacts Sheets | toutes les 2h | contacts-sync.py | ✅ |
| 40 | 🕐 Audit Qualité Crons (journalier) | `0 7 * * *` | cron-quality-audit.py | ✅ |
| 41 | 📞 Point contact LEO (4×/jour) | `0 8,11,14,17 * * *` | cron job agent | ✅ |

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

> 🤖 Dernier audit : 22 July 2026 à 09:00 (UTC+2)


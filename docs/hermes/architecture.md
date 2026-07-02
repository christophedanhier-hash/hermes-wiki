# Architecture Système

## 1. Infrastructure
- **Host LEO**: i7-7700K, 22GB RAM
- **Container Debian 13**:
  - Python 3.13
  - DeepSeek V4 Flash
  - Chromebook Telegram
  - Ollama qwen2.5:7b

## 2. Budget API
- Balance DeepSeek: $51.93
- Seuils d'alerte: $30 / stop: $10
- Routage: Ollama → Gemini → DeepSeek

## 3. Crons Actifs (14)
| **Nom** | **Horodatage** | **Description** |
| --- | --- | --- |
| LEO Full Backup quotidien (complet) | `0 2 * * *` |  |
| 🔍 Veille IA quotidienne | `0 7 * * *` |  |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` |  |
| 📧 Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | gmail_classifier.py |
| 📝 docs-update | `0 */4 * * *` | run-docs-update.sh |
| 🔄 drive-sync | `0 * * * *` | drive-sync.sh |
| 📖 doc-watch-auto | `0 */6 * * *` | doc-watch-auto.sh |
| 🩺 Auto-Heal Agent | `*/15 * * * *` |  |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh |
| 📦 Archive Watch — leo-tracker | `0 */6 * * *` | agent-pro-archive.sh |
| 📊 Unified Collector v2 | `*/15 * * * *` |  |
| 🚀 Deploy Unified Dashboard | `2,17,32,47 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |
| 🛡️ Auto-Fix Daemon | `*/5 * * * *` | auto-fix-daemon.sh |

## 4. Dashboards
- crons
- github
- machines
- wiki

## 5. Sessions & Utilisation
- Total sessions: 374
- Total messages: 12,123
- Telegram: 9 sessions
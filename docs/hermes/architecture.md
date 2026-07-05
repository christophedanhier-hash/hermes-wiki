# Architecture Système

## 1. Infrastructure
L'infrastructure de LEO est composée des éléments suivants :
- **Host LEO** : i7-7700K, 22GB RAM
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Chromebook Telegram**
- **Ollama qwen2.5:7b**

## 2. Budget API
Le budget actuel pour les APIs est de $47.34, avec des seuils d'alerte à $30 et un seuil de stop à $10. Le routage des requêtes se fait selon la hiérarchie suivante : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs
Le tableau ci-dessous présente les 19 crons actifs :

| **Tâche** | **Horodatage** | **Script** |
|-----------|----------------|------------|
| 🔍 Veille IA quotidienne | `0 7 * * *` | - |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | deploy-tofdan.sh |
| 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | gmail_classifier.py |
| 📝 docs-update | `0 */4 * * *` | run-docs-update.sh |
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
| 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | leo-full-backup.py |

## 4. Dashboards
Les dashboards suivants sont disponibles :
- **crons**
- **github**
- **machines**
- **wiki**

## 5. Sessions & Utilisation
- **Total sessions** : 1082
- **Total messages** : 18473
- **Sessions Telegram** : 13

La taille de la base de données est de 140.3 MB.
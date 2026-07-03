# Architecture Système

## 1. Infrastructure
L'infrastructure de LEO est composée des éléments suivants :
- **Host LEO** : i7-7700K avec 22GB de RAM.
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**.
- **Chromebook Telegram** pour la communication via Telegram.
- **Ollama qwen2.5:7b** pour le traitement linguistique et l'intelligence artificielle.

## 2. Budget API
Le budget actuel de l'API est de $50.65, avec des seuils d'alerte à $30 et un seuil de stop à $10. Le routage est configuré comme suit : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs
Il y a actuellement 13 crons en cours :

| **Nom du Cron** | **Heure d'exécution** | **Fichier/Commande** |
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

## 4. Dashboards
Les dashboards suivants sont actuellement disponibles :
- crons
- github
- machines
- wiki

## 5. Sessions & Utilisation
- **Total sessions** : 665
- **Total messages** : 14719
- **Telegram** : 10 sessions
- **Database size** : 103.6 MB
# Architecture Système

## 1. Infrastructure
L'infrastructure de LEO est composée du suivant :

- **Host LEO** : i7-7700K avec 22GB de RAM
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Telegram Client** : Chromebook pour la communication via Telegram
- **Ollama qwen2.5:7b** : Utilisé pour divers services et tâches

## 2. Budget API
Le budget actuel de l'API est de $50.11, avec des seuils d'alerte à $30 et un stop à $10. Le routage des requêtes est organisé comme suit : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs
Il y a actuellement 13 crons en activité :

| **Nom de la Tâche** | **Horodatage** | **Commande** |
|---------------------|---------------|--------------|
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
| 🚀 Deploy Unified Dashboard | `0 12 * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |

## 4. Dashboards
Les dashboards actuellement disponibles sont :

- crons
- github
- machines
- wiki

## 5. Sessions & Utilisation
- **Total sessions** : 776
- **Total messages** : 15905
- **Sessions Telegram** : 11
- **Taille de la base de données** : 113.7 MB
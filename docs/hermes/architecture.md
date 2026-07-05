# Architecture Système

## 1. Infrastructure
L'infrastructure de LEO est composée du suivant :

- **Host LEO** : i7-7700K, 22GB de RAM
- **Container Debian 13** avec Python 3.13 et DeepSeek V4 Flash
- **Flash** pour l'accélération des requêtes
- **Chromebook Telegram** pour la communication via le réseau Telegram
- **Ollama qwen2.5:7b** pour la génération de texte

## 2. Budget API
Le budget actuel pour les APIs est de $48.7, avec un seuil d'alerte à $30 et une limite de stop à $10. Le routage des requêtes se fait dans l'ordre suivant : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs
Il y a actuellement 13 crons en cours d'exécution :

| **Nom du Cron** | **Horodatage** | **Script** |
|-----------------|---------------|------------|
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
| 🚀 Deploy Unified Dashboard | `10 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |

## 4. Dashboards
Les dashboards suivants sont disponibles :

- **crons**
- **github**
- **machines**
- **wiki**

## 5. Sessions & Utilisation
Le nombre total de sessions est de 997, avec un total de 17363 messages échangés. Il y a également 11 sessions Telegram et la taille totale de la base de données est de 125.6 MB.

Cette configuration optimise l'efficacité du système tout en assurant une utilisation efficace des ressources et un suivi précis des opérations.
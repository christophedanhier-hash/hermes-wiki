## Architecture Système

### 1. Infrastructure
Le système LEO est composé d'une infrastructure robuste et bien structurée pour assurer la stabilité et l'efficacité opérationnelle. Voici les détails de l'environnement :

- **Host LEO** : i7-7700K avec 22GB de RAM
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Chromebook Telegram**
- **Ollama qwen2.5:7b**

### 2. Budget API
Le budget actuel pour les APIs est de $42.59, avec des seuils d'alerte à $30 et un seuil de stop à $10. Le routage des requêtes est organisé comme suit :
- **Ollama → Gemini → DeepSeek**

### 3. Crons Actifs
Le système exécute actuellement 28 tâches planifiées (crons) pour maintenir l'efficacité et la fluidité du fonctionnement. Voici les détails de ces tâches :

| **Tâche** | **Horaires** | **Script** |
| --- | --- | --- |
| 🔍 Veille IA quotidienne | `0 7 * * *` | send_veille_smtp.py |
| 🔄 Déploiement auto tofdan.be | `5 * * * *` | deploy-tofdan.sh |
| 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | gmail_classifier.py |
| ✍️ docs-update | `0 */4 * * *` | run-docs-update.sh |
| 🔄 drive-sync | `0 * * * *` | drive-sync.sh |
| 📖 doc-watch-auto | `0 */6 * * *` | doc-watch-auto.sh |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh |
| 📊 Unified Collector v2 | `*/15 * * * *` |  |
| 🚀 Deploy Unified Dashboard | `10 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |
| 🛡️ LEO Health Check (script) | `2,17,32,47 * * * *` | leo-health-check.py |
| 📒 vault-daily-journal (vault-leo) | `0 23 * * *` |  |
| 📒 vault-default-daily-journal | `5 23 * * *` |  |
| 🔧 LEO Maintenance quotidienne | `0 3 * * *` | leo-daily-maintenance.py |
| 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` |

### 4. Dashboards
Le système utilise plusieurs dashboards pour surveiller et gérer les opérations en temps réel :

- **crons**
- **github**
- **machines**
- **wiki**

### 5. Sessions & Utilisation
Les sessions et l'utilisation du système sont suivies de près pour garantir la performance optimale. Voici un aperçu des statistiques :

- **Total sessions** : 1457
- **Total messages** : 23469
- **Telegram sessions** : 15

La taille de la base de données est actuellement de 181.2 MB.

Ce tableau offre une vue d'ensemble de l'architecture système, des tâches planifiées et du suivi des opérations pour assurer un fonctionnement efficace et sécurisé.
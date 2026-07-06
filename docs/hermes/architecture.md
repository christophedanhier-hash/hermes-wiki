## Architecture Système

### 1. Infrastructure
LEO est hébergé sur un host i7-7700K avec 22GB de RAM, exécutant un conteneur Debian 13 Python 3.13 DeepSeek V4 Flash. Les autres composants du système incluent :

- **Telegram Chromebook** : Utilisé pour la communication via Telegram.
- **Ollama qwen2.5:7b** : Modèle de langage utilisé pour certaines tâches.

### 2. Budget API
Le budget actuel est de $47.33, avec des seuils d'alerte à $30 et un seuil de stop à $10. Le routage des API suit la stratégie suivante : Ollama → Gemini → DeepSeek V4 Flash.

### 3. Crons Actifs
LEO exécute actuellement 19 tâches planifiées :

| **Tâche** | **Horaires** | **Script** |
| --- | --- | --- |
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

### 4. Dashboards
Les dashboards suivants sont disponibles :

- **crons** : Suivi des tâches planifiées.
- **github** : Suivi de l'activité sur GitHub.
- **machines** : Suivi des machines et de leurs performances.
- **wiki** : Suivi de la documentation et des mises à jour.

### 5. Sessions & Utilisation
- **Total sessions** : 1098
- **Total messages** : 18539
- **Telegram sessions** : 13

La taille de la base de données est actuellement de 140.3 MB.
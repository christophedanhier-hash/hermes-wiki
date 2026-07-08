# Architecture Système

## 1. Infrastructure
L'infrastructure de LEO est composée des éléments suivants :

- **Host LEO**: i7-7700K avec 22GB de RAM.
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**.
- **Chromebook Telegram** pour la communication via le réseau Telegram.
- **Ollama qwen2.5:7b** pour l'intégration et le traitement des données.

## 2. Budget API
Le budget actuel de l'API est de $45.33, avec les seuils d'alerte fixés à $30 et la limite de dépense à $10. Le routage des requêtes se fait dans l'ordre suivant : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs (23)
| **Tâche** | **Horodatage** | **Script** |
|-----------|----------------|------------|
| 🔍 Veille IA quotidienne | `0 7 * * *` | send_veille_smtp.py |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | deploy-tofdan.sh |
| 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | gmail_classifier.py |
| 📝 docs-update | `0 */4 * * *` | run-docs-update.sh |
| 🔄 drive-sync | `0 * * * *` | drive-sync.sh |
| 📖 doc-watch-auto | `0 */6 * * *` | doc-watch-auto.sh |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh |
| 📊 Unified Collector v2 | `*/15 * * * *` |  |
| 🚀 Deploy Unified Dashboard | `10 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |
| 🛡️ LEO Health Check (script) | `*/15 * * * *` | leo-health-check.py |
| 📒 vault-daily-journal (vault-leo) | `0 23 * * *` |  |
| 📒 vault-default-daily-journal | `0 23 * * *` |  |
| 🔧 LEO Maintenance quotidienne | `0 3 * * *` | leo-daily-maintenance.py |
| 💾 LEO Backup quotidien → GDrive (script) | `0 6 * * *` | leo-fu

## 4. Dashboards
Les dashboards suivants sont en place pour surveiller l'activité et les performances du système :

- **crons**: Moniteur des tâches planifiées.
- **github**: Suivi des activités sur le dépôt GitHub.
- **machines**: Surveillance de la santé et des performances des machines.
- **wiki**: Gestion des pages wiki pour une documentation claire et structurée.

## 5. Sessions & Utilisation
Le système a enregistré les statistiques suivantes :

- **Total sessions**: 1307
- **Total messages**: 20090
- **Telegram**: 14 sessions

La base de données contient actuellement 158.1 MB de données.

--- 

C'est une vue d'ensemble de l'architecture système, des ressources utilisées et des tâches planifiées pour assurer le bon fonctionnement du système LEO.
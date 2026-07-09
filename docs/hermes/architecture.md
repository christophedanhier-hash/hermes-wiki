## Architecture Système

### 1. Infrastructure
L'infrastructure de LEO est composée du suivant :
- **Host**: i7-7700K avec 22GB de RAM.
- **Container**: Debian 13, Python 3.13, DeepSeek V4 Flash.
- **Telegram Client**: Chromebook pour la communication Telegram.
- **Modèles Langage**: Ollama qwen2.5:7b.

### 2. Budget API
Le budget actuel est de $44.11. Les seuils d'alerte sont fixés à $30, et le montant minimal pour arrêter les dépenses est de $10. Le routage des requêtes API suit l'ordre suivant : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs
Le tableau ci-dessous présente les 26 crons actifs :

| **Nom du Cron** | **Horaires d'exécution** | **Script Exécuté** |
|-----------------|-------------------------|--------------------|
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
Les dashboards suivants sont disponibles :
- **crons**: Moniteur des tâches cron.
- **github**: Suivi des activités sur GitHub.
- **machines**: Surveillance de l'état des machines.
- **wiki**: Gestion et mise à jour du wiki.

### 5. Sessions & Utilisation
Les statistiques d'utilisation sont les suivantes :
- **Total sessions**: 1408
- **Total messages**: 21489
- **Sessions Telegram**: 14

La taille de la base de données est de 172.5 MB.

---

Ce document fournit une vue d'ensemble de l'architecture système de LEO, des ressources utilisées et des tâches planifiées.
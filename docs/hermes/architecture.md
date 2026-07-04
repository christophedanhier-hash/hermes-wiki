## Architecture Système

### 1. Infrastructure
L'infrastructure de LEO est composée du suivant :

- **Host LEO** : i7-7700K, 22GB RAM
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Telegram Chromebook** pour la communication avec Telegram
- **Ollama qwen2.5:7b** pour le traitement et l'intelligence artificielle

### 2. Budget API
Le budget actuel de l'API est de $50.05, avec les seuils d'alerte fixés à $30 et la limite de dépense à $10. Le routage des requêtes se fait selon le schéma suivant : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs
Il y a actuellement 13 crons en cours d'exécution :

| **Nom du Cron** | **Horaires de lancement** | **Script** |
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
| 🚀 Deploy Unified Dashboard | `0 12 * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |

### 4. Dashboards
Les dashboards suivants sont disponibles :

- crons
- github
- machines
- wiki

### 5. Sessions & Utilisation
Le nombre total de sessions est de 812 avec un total de 16143 messages. Les détails sur les sessions par plateforme sont :

- **Telegram** : 11 sessions

La taille totale de la base de données est de 116.3 MB.

--- 

C'est une vue d'ensemble de l'architecture système actuelle, mettant en lumière les composants clés et leurs interactions.
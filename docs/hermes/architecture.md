## Architecture Système

### 1. Infrastructure

L'infrastructure de LEO est composée des éléments suivants :

- **Host LEO**: i7-7700K, 22GB RAM
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Chromebook Telegram** 
- **Ollama qwen2.5:7b**

### 2. Budget API

Le budget actuel pour les API est de $49.83. Les seuils d'alerte sont fixés à $30 et le montant minimal avant arrêt des services est de $10. Le routage des requêtes se fait selon la hiérarchie suivante : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs

Voici la liste des 13 crons actifs :

| **Nom du Cron** | **Horaires d'exécution** | **Fichier Exécuté** |
| --- | --- | --- |
| LEO Full Backup quotidien (complet) | `0 2 * * *` | - |
| 🔍 Veille IA quotidienne | `0 7 * * *` | - |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | - |
| 📧 Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | gmail_classifier.py |
| ✍️ docs-update | `0 */4 * * *` | run-docs-update.sh |
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

- **Total sessions**: 848
- **Total messages**: 16485
- **Sessions Telegram**: 11
- **Taille de la base de données**: 117.9 MB
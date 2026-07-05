## Architecture Système

### 1. Infrastructure
L'infrastructure du système est composée des éléments suivants :
- **Host LEO**: i7-7700K avec 22GB de RAM
- **Container Debian 13** : Python 3.13, DeepSeek V4 Flash, Chromebook Telegram, Ollama qwen2.5:7b

### 2. Budget API
Le budget actuel pour les APIs est de $48.92. Les seuils d'alerte sont fixés à $30 et le montant minimal pour la suspension des services est de $10. Le routage des requêtes est organisé comme suit : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs
Il y a actuellement 13 crons en activité, détaillés ci-dessous :

| **Nom** | **Horaires** | **Script** |
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
| 🚀 Deploy Unified Dashboard | `10 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |

### 4. Dashboards
Les dashboards actuellement disponibles sont les suivants :
- crons
- github
- machines
- wiki

### 5. Sessions & Utilisation
Le système a enregistré un total de 961 sessions et 17153 messages. Les détails des utilisations sont comme suit :

- **Total sessions**: 961
- **Total messages**: 17153
- **Sessions Telegram**: 11

La taille totale de la base de données est de 124.2 MB.

---

Cela couvre les principaux aspects de l'architecture système actuelle, y compris l'infrastructure, le budget API, les crons en activité, les dashboards et les sessions d'utilisation.
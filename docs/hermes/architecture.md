## Architecture Système

### 1. Infrastructure
L'infrastructure de LEO est composée du suivant :
- **Host**: i7-7700K avec 22GB de RAM
- **Container**: Debian 13, Python 3.13, DeepSeek V4 Flash
- **Telegram Client**: Chromebook pour la communication Telegram
- **Modèles IA**: Ollama qwen2.5:7b

### 2. Budget API
Le budget actuel de l'API est de $51.84. Les seuils d'alerte sont fixés à $30, et le stop du budget est à $10. Le routage des requêtes est organisé comme suit :
- **Ollama → Gemini → DeepSeek**

### 3. Crons Actifs
Il y a actuellement 13 crons en cours d'exécution :

| Nom de la Tâche | Horaire | Script |
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
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |
| 🛡️ Auto-Fix Daemon | `*/5 * * * *` | auto-fix-daemon.sh |

### 4. Dashboards
Les dashboards suivants sont disponibles :
- crons
- github
- machines
- wiki

### 5. Sessions & Utilisation
- **Total sessions**: 410
- **Total messages**: 12,420
- **Telegram**: 9 sessions

La taille de la base de données est de 82.7 MB.
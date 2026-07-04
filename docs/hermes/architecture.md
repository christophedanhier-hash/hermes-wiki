## Architecture Système

### 1. Infrastructure
L'infrastructure de LEO est composée du suivant :
- **Host LEO**: i7-7700K avec 22GB de RAM.
- **Containers**:
  - Debian 13
  - Python 3.13
  - DeepSeek V4 Flash
- **Serveurs et Clients**:
  - Telegram Chromebook
  - Ollama qwen2.5:7b

### 2. Budget API
Le budget actuel pour les APIs est de $50.38, avec des seuils d'alerte à $30 et un stop à $10. Le routage est organisé comme suit : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs (13)
| **Nom du Cron** | **Horaires de lancement** | **Description** |
|-----------------|----------------------------|-----------------|
| LEO Full Backup quotidien (complet) | `0 2 * * *` | Effectue une sauvegarde complète du système. |
| 🔍 Veille IA quotidienne | `0 7 * * *` | Effectue une veille IA quotidienne pour maintenir la pertinence des données. |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | Déploie automatiquement les mises à jour sur le site tofdan.be. |
| 📧 Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | Utilise un classificateur d'e-mails avec Ollama qwen2.5. |
| 📝 docs-update | `0 */4 * * *` | Met à jour les documents régulièrement. |
| 🔄 drive-sync | `0 * * * *` | Syncronise la base de données Google Drive. |
| 📖 doc-watch-auto | `0 */6 * * *` | Surveillance automatique des documents importants. |
| 🩺 Auto-Heal Agent | `*/15 * * * *` | Gère l'auto-repair du système. |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | Syncronise les compétences avec Copilot. |
| 📦 Archive Watch — leo-tracker | `0 */6 * * *` | Surveillance de l'archive avec le tracker LEO. |
| 📊 Unified Collector v2 | `*/15 * * * *` | Collecte des données unifiées. |
| 🚀 Deploy Unified Dashboard | `0 12 * * *` | Déploie le tableau de bord unifié. |
| 💰 Budget Alert | `0 8,20 * * *` | Envoie une alerte si le budget API dépasse $30.

### 4. Dashboards
Les dashboards actuellement disponibles sont :
- **crons**: Surveillance des tâches planifiées.
- **github**: Suivi des activités sur GitHub.
- **machines**: Information sur les machines et leur état.
- **wiki**: Documentation et informations générales.

### 5. Sessions & Utilisation
- **Total sessions**: 739
- **Total messages**: 15395
- **Sessions Telegram**: 10

La taille de la base de données est actuellement de 110.0 MB, ce qui reflète l'utilisation et le volume des données traitées par LEO.
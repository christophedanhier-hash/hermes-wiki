# Architecture Système

## 1. Infrastructure
L'infrastructure de LEO est composée des éléments suivants :

- **Host LEO**: i7-7700K, 22GB RAM
- **Container Debian 13**
- **Python 3.13** 
- **DeepSeek V4 Flash**
- **Flash Storage**
- **Telegram Client (Chromebook)**
- **Ollama qwen2.5:7b**

## 2. Budget API
Le budget actuel pour les APIs est de $49.15, avec des seuils d'alerte à $30 et un seuil de stop à $10. Le routage des requêtes se fait selon la hiérarchie suivante : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs
Il y a actuellement 13 crons en cours d'exécution :

| **Nom du Cron** | **Horodatage** | **Description** |
| --- | --- | --- |
| LEO Full Backup quotidien (complet) | `0 2 * * *` | Effectue une sauvegarde complète des données. |
| 🔍 Veille IA quotidienne | `0 7 * * *` | Met à jour les connaissances de l'IA en permanence. |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | Effectue un déploiement automatique du site web tofdan.be. |
| 📧 Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | Classifie les emails avec l'IA Ollama qwen2.5. |
| 📝 docs-update | `0 */4 * * *` | Met à jour les documents enregistrés régulièrement. |
| 🔄 drive-sync | `0 * * * *` | Syncronise le contenu du drive. |
| 📖 doc-watch-auto | `0 */6 * * *` | Surveille automatiquement la mise à jour des documents. |
| 🩺 Auto-Heal Agent | `*/15 * * * *` | Effectue un auto-diagnostic et une réparation automatique du système. |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | Syncronise les compétences avec Copilot. |
| 📦 Archive Watch — leo-tracker | `0 */6 * * *` | Surveille l'archive de la traque. |
| 📊 Unified Collector v2 | `*/15 * * * *` | Collecte des données unifiées. |
| 🚀 Deploy Unified Dashboard | `10 * * * *` | Déploie le tableau de bord unifié. |
| 💰 Budget Alert | `0 8,20 * * *` | Envoie une alerte si le budget API atteint $30. |

## 4. Dashboards
Les dashboards actuellement disponibles sont :

- **crons**
- **github**
- **machines**
- **wiki**

## 5. Sessions & Utilisation
- **Total sessions**: 887
- **Total messages**: 16,677
- **Sessions Telegram**: 11

La taille de la base de données est actuellement de 119.6 MB.
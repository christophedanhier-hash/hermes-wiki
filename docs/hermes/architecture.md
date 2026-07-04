# Architecture Système

## 1. Infrastructure
L'infrastructure du système est composée des éléments suivants :

- **Host LEO** : i7-7700K, 22GB de RAM
- **Container Debian 13** : Python 3.13, DeepSeek V4 Flash, Chromebook Telegram, Ollama qwen2.5:7b

## 2. Budget API
Le budget actuel pour les API est de $50.56. Les seuils d'alerte sont fixés à $30 et le stop à $10. Le routage des requêtes est organisé comme suit : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs
Il y a actuellement 13 crons en cours d'exécution :

| **Nom du Cron** | **Horodatage** | **Description** |
|-----------------|---------------|----------------|
| LEO Full Backup quotidien (complet) | `0 2 * * *` | Effectue une sauvegarde complète quotidienne. |
| 🔍 Veille IA quotidienne | `0 7 * * *` | Effectue une veille IA quotidienne. |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | Déploie automatiquement les mises à jour sur le site tofdan.be. |
| 📧 Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | Exécute une classification d'e-mails avec Ollama qwen2.5. |
| ✍️ docs-update | `0 */4 * * *` | Met à jour les documents. |
| 🔄 drive-sync | `0 * * * *` | Synchronise le contenu du drive. |
| 📖 doc-watch-auto | `0 */6 * * *` | Surveillance automatique des documents. |
| 🩺 Auto-Heal Agent | `*/15 * * * *` | Gestionnaire automatisé de réparations. |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | Synchronise les compétences vers le copilote. |
| 📦 Archive Watch — leo-tracker | `0 */6 * * *` | Surveillance automatique des archives. |
| 📊 Unified Collector v2 | `*/15 * * * *` | Collecteur unifié version 2. |
| 🚀 Deploy Unified Dashboard | `15 * * * *` | Déploiement du tableau de bord unifié. |
| 💰 Budget Alert | `0 8,20 * * *` | Alertes budgétaires. |

## 4. Dashboards
Les dashboards suivants sont disponibles :

- **crons** : Suivi des tâches planifiées.
- **github** : Surveillance des activités sur GitHub.
- **machines** : État des machines et performances.
- **wiki** : Documentation et informations générales.

## 5. Sessions & Utilisation
- **Total sessions** : 702
- **Total messages** : 15014
- **Telegram sessions** : 10
- **Taille de la base de données** : 106.4 MB
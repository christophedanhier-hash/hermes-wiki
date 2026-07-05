# Architecture Système

## 1. Infrastructure
L'infrastructure du système est composée des éléments suivants :

- **Host LEO** : i7-7700K avec 22GB de RAM.
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**.
- **Telegram Chromebook** pour la communication et l'interaction via Telegram.
- **Ollama qwen2.5:7b** : Modèle d'intelligence artificielle utilisé pour diverses tâches.

## 2. Budget API
Le budget actuel pour les APIs est de $48.38. Les seuils d'alerte sont définis à $30, et le montant minimal avant arrêt des opérations est fixé à $10. Le routage des requêtes est organisé comme suit : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs
Il y a actuellement 13 crons en cours d'exécution :

| **Nom du Cron** | **Horaires de lancement** | **Script/Commande** |
| --- | --- | --- |
| LEO Full Backup quotidien (complet) | `0 2 * * *` | - |
| 🔍 Veille IA quotidienne | `0 7 * * *` | - |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | - |
| 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | gmail_classifier.py |
| 📝 docs-update | `0 */4 * * *` | run-docs-update.sh |
| 🔄 drive-sync | `0 * * * *` | drive-sync.sh |
| 📖 doc-watch-auto | `0 */6 * * *` | doc-watch-auto.sh |
| 🩺 Auto-Heal Agent | `*/15 * * * *` | - |
| 🔄 sync-skills-to-copilot | `*/30 * * * *` | sync_skills_to_copilot.sh |
| 📦 Archive Watch — leo-tracker | `0 */6 * * *` | agent-pro-archive.sh |
| 📊 Unified Collector v2 | `*/15 * * * *` | - |
| 🚀 Deploy Unified Dashboard | `10 * * * *` | deploy-dashboard.sh |
| 💰 Budget Alert | `0 8,20 * * *` | budget-alert.sh |

## 4. Dashboards
Les dashboards actuellement disponibles sont :

- crons : Affiche l'état des tâches planifiées.
- github : Moniteur des activités sur GitHub.
- machines : Surveillance de l'état des machines et du système.
- wiki : Page documentaire pour la documentation interne.

## 5. Sessions & utilisation
Les statistiques d'utilisation sont les suivantes :

- **Total sessions** : 1033
- **Total messages** : 17585
- **Telegram** : 11 sessions

La taille de la base de données est de 127.4 MB.

---

Ce résumé fournit une vue d'ensemble détaillée de l'architecture système, des ressources utilisées et des tâches planifiées pour assurer le bon fonctionnement du système.
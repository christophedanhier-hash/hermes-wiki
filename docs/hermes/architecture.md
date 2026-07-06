# Architecture Système

## 1. Infrastructure
L'infrastructure de LEO est composée des éléments suivants :

- **Host LEO**: i7-7700K avec 22GB de RAM.
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**.
- **Chromebook Telegram** pour la gestion des communications via Telegram.
- **Ollama qwen2.5:7b** pour l'intégration et le traitement des données.

## 2. Budget API
Le budget actuel pour les APIs est de $46.73, avec des seuils d'alerte à $30 et un seuil de stop à $10. Le routage des requêtes est organisé comme suit : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs
Il y a actuellement 22 crons en cours d'exécution :

| **Nom du Cron** | **Horaires** | **Script** |
|-----------------|--------------|------------|
| 🔍 Veille IA quotidienne | `0 7 * * *` | send_veille_smtp.py |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | deploy-tofdan.sh |
| 📧 Email Classifier — rule-based (inbox zero) | `*/30 * * * *` | gmail_classifier.py |
| ✏️ docs-update | `0 */4 * * *` | run-docs-update.sh |
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
Les dashboards suivants sont en place :

- **crons**
- **github**
- **machines**
- **wiki**

## 5. Sessions & Utilisation
Le système a enregistré les statistiques suivantes :
- Total de sessions : 1170
- Total de messages : 19319
- Telegram : 14 sessions

La taille actuelle de la base de données est de 146.8 MB.

---

Ce document fournit une vue d'ensemble détaillée de l'architecture système, des ressources utilisées et des activités en cours pour LEO.
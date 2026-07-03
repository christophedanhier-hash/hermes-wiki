# Architecture Système

## 1. Infrastructure
L'infrastructure du système est composée des éléments suivants :

- **Host LEO** : i7-7700K avec 22GB de RAM.
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Telegram Client** : Chromebook pour la gestion des sessions Telegram.
- **Modèles Langage** : Ollama qwen2.5:7b.

## 2. Budget API
Le budget actuel pour les APIs est de $51.03, avec les seuils d'alerte fixés à $30 et le stop à $10. Le routage des requêtes est organisé comme suit : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs
Il y a actuellement 13 crons en cours d'exécution :

| **Nom du Cron** | **Horaires** | **Description** |
|-----------------|--------------|----------------|
| LEO Full Backup quotidien (complet) | `0 2 * * *` | Effectue une sauvegarde complète du système. |
| 🔍 Veille IA quotidienne | `0 7 * * *` | Met à jour les informations de veille IA. |
| 🔄 Déploiement auto tofdan.be | `0 * * * *` | Gère l'automaticité des déploiements sur le site tofdan.be. |
| 📧 Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | Exécute un classifieur d'e-mails avec Ollama qwen2.5. |
| ✍️ docs-update | `0 */4 * * *` | Met à jour les documents en fonction des changements. |
| 🔄 drive-sync | `0 * * * *` | Synchronise les données du cloud Drive. |
| 📖 doc-watch-auto | `0 */6 * * *` | Surveille automatiquement les documents pour des mises à jour. |
| 💊 Auto-Heal Agent | `*/15 * * * *` | Gère l'autoréparation du système. |
| 🩺 sync-skills-to-copilot | `*/30 * * * *` | Syncronise les compétences vers Copilot. |
| 📦 Archive Watch — leo-tracker | `0 */6 * * *` | Surveille la sauvegarde de l'archive. |
| 📊 Unified Collector v2 | `*/15 * * * *` | Collecte des données unifiées. |
| 🚀 Deploy Unified Dashboard | `15 * * * *` | Déploie le tableau de bord uni. |
| 💰 Budget Alert | `0 8,20 * * *` | Envoie une alerte si le budget API atteint $30.

## 4. Dashboards
Les dashboards actuellement disponibles sont :

- **crons**
- **github**
- **machines**
- **wiki**

## 5. Sessions & Utilisation
Le système a enregistré les suivants :

- **Total sessions** : 521
- **Total messages** : 13650
- **Sessions Telegram** : 10

La taille de la base de données est de 93.5 MB.

---

Cette architecture offre une structure solide et efficace pour gérer les tâches automatiques, l'analyse des données, le déploiement et la synchronisation, tout en maintenant un contrôle sur le budget API.
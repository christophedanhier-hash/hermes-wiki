## Architecture Système

### 1. Infrastructure
L'infrastructure de LEO est composée du suivant :
- **Host LEO**: i7-7700K, 22GB RAM
- **Containers**:
  - Debian 13
  - Python 3.13
  - DeepSeek V4 Flash
  - Telegram Chromebook
  - Ollama qwen2.5:7b

### 2. Budget API
Le budget API actuel est de $55.54, avec des seuils d'alerte à $30 et un seuil de stop à $10. Le routage est configuré comme suit : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs (18)
| **Nom du Cron** | **Horaires** | **Description** |
| --- | --- | --- |
| LEO Full Backup quotidien (complet) | `0 2 * * *` | Effectue une sauvegarde complète du système à minuit. |
| Budget Check quotidien | `0 8,20 * * *` | Vérifie le budget API et envoie des alertes si nécessaire. |
| Hermes Update Check | `0 9 * * *` | Vérifie la mise à jour de l'application Hermes. |
| Veille IA quotidienne | `0 7 * * *` | Effectue une veille IA pour maintenir les connaissances mises à jour. |
| Vérification infra hebdo | `0 8 * * 1` | Effectue des vérifications d'infrastructure hebdomadaires le lundi matin. |
| Déploiement auto tofdan.be | `0 * * * *` | Effectue un déploiement automatique du site tofdan.be à chaque heure. |
| sync-memory | `*/30 * * * *` | Exécute le script `sync-memory.py` pour synchroniser la mémoire. |
| Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | Utilise le script `gmail_classifier.py` pour classifier les emails. |
| docs-update | `0 */4 * * *` | Exécute le script `run-docs-update.sh` pour mettre à jour les documents. |
| drive-sync | `0 * * * *` | Effectue une synchronisation du dossier Google Drive avec le système. |
| credentials-check | `0 6 * * *` | Vérifie régulièrement les informations de connexion. |
| doc-watch-auto | `0 */6 * * *` | Exécute le script `doc-watch-auto.sh` pour surveiller automatiquement les documents. |
| Auto-Heal Agent | `*/15 * * * *` | Effectue un auto-réparation du système tous les 15 minutes. |
| sync-skills-to-copilot | `*/30 * * * *` | Exécute le script `sync_skills_to_copilot.sh` pour synchroniser les compétences vers Copilot. |
| Archive Watch — leo-tracker | `0 */6 * * *` | Exécute le script `agent-pro-archive.sh` pour surveiller l'archive. |
| Data Freshness Watchdog | `*/5 * * * *` | Vérifie la fraîcheur des données toutes les 5 minutes. |
| Unified Collector v2 | `*/15 * * * *` | Collecte et centralise les données de manière unifiée.

### 4. Dashboards
Les dashboards couvrent plusieurs aspects :
- **crons**: Moniteur des tâches planifiées.
- **github**: Suivi des activités sur GitHub.
- **machines**: Surveillance des machines et performances.
- **wiki**: Documentation et informations de la documentation.

### 5. Sessions & Utilisation
- **Total sessions**: 116
- **Total messages**: 5413
- **Sessions Telegram**: 5

La base de données a une taille totale de 39,8 MB.
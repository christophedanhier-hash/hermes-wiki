## Architecture Système

### 1. Infrastructure
L'infrastructure du système est composée des éléments suivants :
- **Host LEO** : i7-7700K avec 22GB de RAM.
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash, Chromebook Telegram, Ollama qwen2.5:7b**.

### 2. Budget API
Le budget actuel pour les APIs est de $55.37. Les seuils d'alerte sont fixés à $30 et le montant minimal avant arrêt des services est de $10. Le routage des requêtes se fait dans l'ordre suivant : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs
Il y a actuellement 18 crons en activité, dont la liste détaillée est la suivante :

| **Nom du Cron** | **Horodatage** | **Description** |
| --- | --- | --- |
| LEO Full Backup quotidien (complet) | `0 2 * * *` | Effectue une sauvegarde complète du système. |
| Budget Check quotidien | `0 8,20 * * *` | Vérifie régulièrement le budget API. |
| Hermes Update Check | `0 9 * * *` | Vérifie la mise à jour de l'application Hermes. |
| Veille IA quotidienne | `0 7 * * *` | Effectue une veille sur les dernières avancées en intelligence artificielle. |
| Vérification infra hebdo | `0 8 * * 1` | Effectue une vérification hebdomadaire de l'infrastructure. |
| Déploiement auto tofdan.be | `0 * * * *` | Déploie automatiquement les mises à jour sur le site tofdan.be. |
| sync-memory | `*/30 * * * *` | Exécute la synchronisation mémoire. |
| Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | Classifie les e-mails avec l'assistant Ollama qwen2.5. |
| docs-update | `0 */4 * * *` | Met à jour les documents. |
| sync-drive | `0 * * * *` | Synchronise le drive. |
| credentials-check | `0 6 * * *` | Vérifie régulièrement les informations de connexion. |
| doc-watch-auto | `0 */6 * * *` | Surveille automatiquement les documents. |
| Auto-Heal Agent | `*/15 * * * *` | Effectue un auto-réparation des agents. |
| sync-skills-to-copilot | `*/30 * * * *` | Synchronise les compétences vers Copilot. |
| Archive Watch — leo-tracker | `0 */6 * * *` | Surveille l'archive de la traque. |
| Data Freshness Watchdog | `*/5 * * * *` | Vérifie la fraîcheur des données. |
| Unified Collector v2 | `*/15 * * * *` | Collecte les données unifiées.

### 4. Dashboards
Les dashboards suivants sont disponibles pour surveiller l'activité du système :
- **crons** : Monitore le statut et la fréquence des crons.
- **github** : Suivi des activités sur GitHub.
- **machines** : Surveillance de l'état des machines.
- **wiki** : Documentation et informations générales.

### 5. Sessions & Utilisation
Le système a enregistré les statistiques suivantes :
- **Total sessions** : 153
- **Total messages** : 6908
- **Telegram sessions** : 6

La taille de la base de données est actuellement de 47.4 MB.

--- 

Ce tableau offre une vue d'ensemble de l'architecture système, des ressources en cours d'utilisation et des mécanismes de maintenance automatisés.
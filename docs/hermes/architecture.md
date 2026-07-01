# Architecture Système

## 1. Infrastructure
L'infrastructure de l'assistant LEO est composée des éléments suivants :

- **Host LEO**: i7-7700K avec 22GB de RAM.
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**.
- **Chromebook Telegram** pour la communication via Telegram.
- **Ollama qwen2.5:7b** pour le traitement des tâches complexes.

## 2. Budget API
Le budget actuel pour les APIs est de $56.36, avec des seuils d'alerte à $30 et un seuil de stop à $10. Le routage des requêtes API suit la séquence suivante : Ollama → Gemini → DeepSeek V4 Flash.

## 3. Crons Actifs
Le tableau ci-dessous présente les 19 crons actifs :

| **Nom du Cron** | **Heure de lancement** | **Description** |
| --- | --- | --- |
| LEO Full Backup quotidien (complet) | `0 2 * * *` | Effectue une sauvegarde complète du système. |
| Budget Check quotidien | `0 8,20 * * *` | Vérifie le budget et envoie des alertes si nécessaire. |
| Hermes Update Check | `0 9 * * *` | Vérifie la mise à jour de l'application Hermes. |
| Veille IA quotidienne | `0 7 * * *` | Effectue une veille IA pour maintenir les connaissances à jour. |
| Vérification infra hebdo | `0 8 * * 1` | Effectue une vérification hebdomadaire de l'infrastructure. |
| Déploiement auto tofdan.be | `0 * * * *` | Déploie automatiquement les mises à jour sur le site tofdan.be. |
| Dashboards (10-en-1) | `0 * * * *` | Lance la génération des dashboards. run-all-dashboards.sh |
| Watchdogs | `*/5 * * * *` | Lance la surveillance continue de l'infrastructure. run-all-watchdogs.sh |
| Auto-commit repos | `*/15 * * * *` | Effectue un commit automatique des modifications dans les répertoires de code. auto-commit-repos.sh |
| Publish (index+HTML) | `15 * * * *` | Publie l'index et les fichiers HTML générés. publish.sh |
| sync-memory | `*/30 * * * *` | Synchronise la mémoire du système. sync-memory.py |
| Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | Classifie les emails avec l'assistant Ollama qwen2.5. gmail_classifier.py |
| docs-update | `0 */4 * * *` | Met à jour les documents automatiquement. run-docs-update.sh |
| drive-sync | `0 * * * *` | Synchronise le contenu du cloud Drive. drive-sync.sh |
| credentials-check | `0 6 * * *` | Vérifie la validité des informations de connexion. check-credentials.py |
| doc-watch-auto | `0 */6 * * *` | Surveillance automatique des documents. doc-watch-auto.py |
| Auto-Heal Agent | `*/15 * * * *` | Gère l'autoréparation du système. |

## 4. Dashboards
Les dashboards sont gérés par les crons suivants :

- **crons**: Lance la génération des dashboards pour les métriques de cron.
- **github**: Lance la génération des dashboards pour les données GitHub.
- **machines**: Lance la génération des dashboards pour l'état des machines.
- **wiki**: Lance la génération des dashboards pour le contenu du wiki.

## 5. Sessions & Utilisation
Le système a enregistré un total de 59 sessions et 3720 messages. Les détails sont les suivants :

- **Total sessions**: 59
- **Total messages**: 3720
- **Sessions via Telegram**: 4

La taille de la base de données est de 25.8 MB, ce qui indique un usage modéré et une gestion efficace des ressources.

--- 

Cette page Wiki MkDocs fournit une vue d'ensemble détaillée de l'architecture système, permettant une meilleure compréhension et gestion des opérations en cours.
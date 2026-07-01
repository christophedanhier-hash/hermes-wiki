# Architecture Système

## 1. Infrastructure
L'infrastructure de LEO est composée des éléments suivants :
- **Host LEO** : i7-7700K avec 22GB de RAM.
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Chromebook Telegram**
- **Ollama qwen2.5:7b**

## 2. Budget API
Le budget actuel pour les APIs est de $55.88, avec des seuils d'alerte à $30 et un stop à $10. Le routage est organisé comme suit : Ollama → Gemini → DeepSeek.

## 3. Crons Actifs (22)
| **Nom du Cron** | **Horaires** | **Description** |
|-----------------|--------------|----------------|
| LEO Full Backup quotidien (complet) | `0 2 * * *` | Effectue une sauvegarde complète du système chaque jour à minuit. |
| Budget Check quotidien | `0 8,20 * * *` | Vérifie régulièrement le budget et envoie des alertes si nécessaire. |
| Hermes Update Check | `0 9 * * *` | Vérifie la mise à jour de l'agent Hermes chaque matin à neuf heures. |
| Veille IA quotidienne | `0 7 * * *` | Effectue une veille d'intelligence artificielle quotidienne pour maintenir les connaissances à jour. |
| Vérification infra hebdo | `0 8 * * 1` | Effectue une vérification hebdomadaire de l'infrastructure chaque lundi matin à huit heures. |
| Déploiement auto tofdan.be | `0 * * * *` | Effectue un déploiement automatique du site tofdan.be en continu. |
| Dashboards (10-en-1) | `0 * * * *` | Exécute le script run-all-dashboards.sh pour mettre à jour les dashboards. |
| Watchdogs | `*/5 * * * *` | Exécute le script run-all-watchdogs.sh pour surveiller l'état des services. |
| Auto-commit repos | `*/15 * * * *` | Effectue un auto-commit régulier des repositories. |
| Publish (index+HTML) | `15 * * * *` | Publie les index et HTML générés. |
| sync-memory | `*/30 * * * *` | Synchronise la mémoire du système. |
| Email Classifier — Ollama qwen2.5 | `*/30 * * * *` | Classifie les e-mails avec l'assistant Ollama qwen2.5. |
| docs-update | `0 */4 * * *` | Met à jour les documents régulièrement. |
| drive-sync | `0 * * * *` | Synchronise le cloud drive. |
| credentials-check | `0 6 * * *` | Vérifie les informations de connexion. |
| doc-watch-auto | `0 */6 * * *` | Surveille automatiquement les documents. |
| Auto-Heal Agent | `*/15 * * * *` | Effectue un auto-guérison du système.

## 4. Dashboards
Les dashboards sont gérés par des crons qui s'exécutent régulièrement :
- **crons/github/machines/wiki** : Gère les mises à jour et l'affichage des informations sur GitHub, les machines et le wiki.

## 5. Sessions & Utilisation
- **Total sessions** : 87
- **Total messages** : 4798
- **Telegram** : 5 sessions

La taille de la base de données est actuellement de 35.4 MB.
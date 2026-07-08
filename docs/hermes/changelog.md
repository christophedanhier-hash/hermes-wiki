# 📋 Changelog

*Document vivant*

## 2026-07-01 au 08/07/2026

- **Synthèse Hebdomadaire LEO** : Ajout du script `synthese_hebdo.py` pour générer une synthèse hebdomadaire.
- **Cron Ownership Watchdog** : Mise à jour du script `cron-owner-watchdog.sh` pour surveiller les propriétaires des tâches cron.
- **Rebuild Wiki BAVI local** : Ajout d'une tâche cron pour rebuild le wiki BAVI local toutes les heures via `rebuild-wiki.sh`.
- **Auto-commit wikis** : Les scripts de commit automatiques ont été mis à jour avec 89 commits dans le dépôt `hermes-christophe`, et 146 commits dans le dépôt `wiki`.
- **Unified Collector v2** : Ajout du script pour la version v2 de l'collector unifié.
- **Budget Alert** : Mise à jour du script `budget-alert.sh` pour des alertes budgétaires à 8h et 20h.
- **Auto-Archive BAVI LEO** : Ajout d'une tâche cron pour auto-archiver les données BAVI toutes les cinq minutes via `auto-archive.py`.
- **Vault Daily Journal** : Mise à jour des scripts `vault-leo` et `vault-default-daily-journal` pour journaliser les activités quotidiennes.
- **GitHub Actions Watchdog** : Ajout du script `github_workflow_watchdog.py` pour surveiller les actions GitHub.
- **Cron Health Watchdog** : Mise à jour du script `cron_health_watchdog.py` pour scanner les logs des tâches cron.
# 📋 Changelog

*Document vivant*

## 10/07/2026

- **🔴 Restauration d'urgence** — Perte du conteneur Docker LEO. Restauration complète depuis `leo-full-backup-2026-07-10.tar.gz` (cf. `backup-recovery.md`).
  - Fix symlink SOUL.md cassé (pointait vers `~/Projets_Dev/`)
  - Redémarrage des 5 gateways (default, leo-copilot, bureau-robert, bavi-leo, emile)
  - Correction des paths OBSIDIAN_VAULT_PATH dans les 5 `.env`
  - Backup immédiat post-restauration (93 Mo)
  - 39 crons restaurés et actifs ✅
- **Unified Collector v2** : Mise à jour du script pour une collecte unifiée améliorée.
- **Synthèse Hebdomadaire LEO** : Ajout d'une mise à jour hebdomadaire pour le résumé de la semaine.
- **Vault Daily Journal (vault-leo)**, **Vault Default Daily Journal (5 23 * * *)** : Mises à jour des scripts pour un journal quotidien plus précis.
- **Auto-Archive BAVI LEO (5min) (every 5m)** : Optimisation du script d'archivage automatique pour une meilleure gestion de l'espace.
- **Rebuild Wiki BAVI local (*/15 * * * *)** : Ajout d'une tâche pour la reconstruction locale du wiki BAVI toutes les quinze minutes.
- **Rebuild Wiki Voyages local (15 * * * *)** : Nouvelle tâche ajoutée pour la reconstruction locale du wiki Voyages à 3h00.
- **Check OAuth Tokens (48h) (0 8 * * *)** : Mise en place d'un script pour vérifier les tokens OAuth toutes les 48 heures.

> 🤖 Dernier audit : 20/07/2026 à 07:26 (UTC+2)


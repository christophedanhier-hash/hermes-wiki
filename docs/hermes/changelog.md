# 📋 Changelog

*Document vivant — suivi hebdomadaire des évolutions.*

## [15-06-2026]

- **Infrastructure :**
  - `drive-sync` passe en mode bidirectionnel complet (Drive → GitHub → Drive)
  - Sync `--up` automatisé — les données locales remontent vers le Drive
  - Nouveau fichier `Voyages/Distances/distances-voyages.json` généré par `generate_voyages_wiki.py`

- **Corrections :**
  - Tableau liste des voyages formaté correctement (en-tête)
  - Distances kilométriques inter-étapes ajoutées (formule Haversine)
  - Synchronisation du curseur `--full` : `last_sync` sauvegardé avant `--down` pour que `--up` voie les changements

- **Documentation :**
  - Wiki LEO : mise à jour architecture + leo-architecture (Drive source de vérité, 12 crons, flux bidirectionnel)
  - Skill `gdrive-source-of-truth` créé

---

## [12-06-2026 à 15-06-2026]

- **Nouvelles fonctionnalités :**
  - Ajout du cron `wiki-oca-sync` (H:35) pour synchroniser les fichiers Cowork Drive vers le wiki OCA et les pousser.
  - Mise à jour de la description dans `DESCRIPTION_MAP` avec l'ajout de `wiki-oca-sync`.
  - Export des documents en format `.md`, implémentation d'un workflow de vérification et gestion des conflits.

- **Corrections :**
  - Retrait des liens wikis externes du wiki LEO, conservant uniquement les tuiles des dashboards.
  - Remplacement des tableaux de liens par quatre tuiles des dashboards et des wikis.
  - Ajout d'une page cachée au portail avec des tuiles vers tous les wikis et dashboards.

- **Améliorations :**
  - Mise à jour du wiki LEO, notamment la configuration, le routage, les règles et bonnes pratiques.
  - Retrait des sections T600 et Voyages du wiki LEO.

---

*Aucun historique précédent.*
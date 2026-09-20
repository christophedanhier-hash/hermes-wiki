# Chapitre 28 — Crons quotidiens : backup, veille IA, sync

Les crons quotidiens sont les tâches lourdes qui s'exécutent une fois par jour. Backup, veille IA, synchronisation — le ménage automatisé.

> **Référence opérationnelle :** L'ordonnancement complet des 71 jobs actifs est documenté dans [`hermes/configuration/profiles.md`](../configuration/profiles.md) et centralisé sous le profil `michel` (`profiles/michel/cron/jobs.json`).

## Les crons quotidiens de LEO

```yaml
06:00 — Backup quotidien
  Action: Archive de tous les profils + configs locales
  Rétention: 7 jours
  Coût: 0 € (no_agent)
  Script: ~/.hermes/profiles/michel/scripts/leo-full-backup.py

07:30 — Veille IA (Phase 1)
  Action: Collecte des flux RSS
  Coût: 0 € (no_agent)

08:00 — Veille IA (Phase 2)
  Action: Synthèse et analyse par LLM
  Coût: Faible (appel LLM planifié)

09:00 — Hermes Update Check
  Action: Vérifie si une mise à jour d'Hermes Agent est disponible
  Coût: 0 € (no_agent)

18:00 — Sync Drive → GitHub
  Action: Miroir Google Drive ↔ dépôts GitHub / wikis
  Coût: 0 € (no_agent)
```

## Backup quotidien

```yaml
Périmètre de sauvegarde:
  - Profils opérationnels : default, michel, robert, sylvia, emile, gerard
  - Configs (config.yaml, SOUL.md, variables locales)
  - Mémoires persistantes, skills synchronisés et sessions
  - Scripts d'automatisation et crons

Destination:
  - Local: ~/.hermes/backups/
  - Cloud: Google Drive (Hermes_Christophe/backups/)
  
Rétention: 7 jours
Taille moyenne: ~40-70 MB
```

## Veille IA quotidienne

```yaml
Processus:
  1. Collecte RSS (sources tech et IA)
  2. Analyse et sélection des articles les plus pertinents
  3. Rédaction du rapport formaté
  4. Envoi automatique de la synthèse

Coût: Faible (~0,05 €/jour)
Tags: ALERTE, NOUVEAU, À SUIVRE, CONFORMITÉ, TENDANCE
```

## Synchronisation Drive → GitHub

```yaml
Fonctionnement:
  - Scanne les dossiers Google Drive partagés
  - Détecte les nouveaux fichiers .docx ou .md
  - Convertit les .docx en .md
  - Commit + push sur le wiki GitHub correspondant

Wikis synchronisés:
  - BAVI_LEO ↔ Drive (docs bureaux)
  - voyages-wiki ↔ Drive (roadbooks)
  - emile-wiki ↔ Drive (documents et notes professionnelles)
```

## Planification avec cron

```yaml
# Format: minute heure jour mois jour_semaine
0 6 * * *   → Tous les jours à 06:00 (backup)
30 7 * * * → Tous les jours à 07:30 (veille phase 1)
0 8 * * *   → Tous les jours à 08:00 (veille phase 2)
0 9 * * *   → Tous les jours à 09:00 (check version)
0 18 * * *  → Tous les jours à 18:00 (sync Drive)
```

---

*Document mis à jour le 20/09/2026 — Léo 🦁*

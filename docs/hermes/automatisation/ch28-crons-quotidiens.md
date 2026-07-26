Le titre devrait être mis à jour pour refléter la réalité des informations fournies.

Les crons quotidiens sont les tâches lourdes qui s'exécutent une fois par jour. Backup, veille IA, synchronisation — le ménage automatisé.

## Les crons quotidiens de LEO

> ⚠️ **Mise à jour 04/07/2026** : suite aux changements post-crash, le déploiement des dashboards est maintenant unifié toutes les heures via `collect-v2.py`. L'Auto-Fix Daemon a été supprimé.

```yaml
Les crons quotidiens doivent être mis à jour pour refléter ces modifications.
```

## Backup quotidien

```yaml
Les profils et bots mentionnés dans le document ne correspondent pas à la réalité. Les profils et bots actuels sont default, emile, michel, robert, sylvia.

Destination:
  - Local: ~/.hermes/backups/
  - Cloud: Google Drive (Hermes_Christophe/backups/)
  
Rétention: 7 jours
Taille moyenne: ~40-70 MB
```

## Veille IA quotidienne

```yaml
Processus:
  - **Collecte RSS (17 sources, ~50 articles)**
  2. DeepSeek V4 Flash analyse chaque article
  3. Sélection des 15 plus pertinents
  4. Rédaction du rapport formaté
  5. Envoi par email à christophe.danhier@gmail.com

Coût: ~0,05 €/jour = ~1,50 €/mois
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
  - emile-wiki ↔ Drive (brouillons mémoire)
```

## Planification avec cron

```yaml
# Format: minute heure jour mois jour_semaine
0 6 * * *   → Tous les jours à 06:00
30 7 * * * → Tous les jours à 07:30
0 8 * * *   → Tous les jours à 08:00
0 9 * * *   → Tous les jours à 09:00
0 18 * * *  → Tous les jours à 18:00
```
*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

> 🤖 Dernier audit : 26/07/2026 à 12:00 (UTC+2)

# Plan de mission — Mise à jour documentaire Hermes LEO

## Objet

Remettre en cohérence la documentation de la plateforme Hermes LEO avec la réalité opérationnelle, en priorité la carte d'architecture du Wiki Hermes.

## Gouvernance

- **LEO** : pilote documentaire, matrice des pages, structure, rédaction, cohérence inter-pages, build et preuve du wiki.
- **Michel** : audit infrastructure et vérité terrain ; profils, providers, gateways, crons, services, ports, scripts, watchdogs et pipelines.
- **Christophe** : arbitrage des décisions de présentation et validation des divergences produit.
- **Règle d'exécution** : un seul lot actif à la fois ; aucun patch de wiki avant validation du rapport d'audit et du plan.

## Phase 0 — Audit croisé en lecture seule

### LEO

1. Identifier le dépôt source réel et son état Git.
2. Inventorier les pages d'architecture, la nav et la carte documentaire.
3. Repérer les doublons, pages générées et liens entrants.
4. Extraire les affirmations chiffrées et les dates obsolètes.
5. Vérifier le build local et l'URL servie actuelle sans modifier.

### Michel

1. Vérifier les profils réellement actifs et leur configuration chargée.
2. Vérifier les gateways, providers, modèles effectifs et fallbacks.
3. Compter les jobs Michel, distinguer no_agent et LLM, et vérifier les crons hôte.
4. Vérifier services, ports, dashboards, scripts, vaults et watchdogs.
5. Vérifier les pipelines doc-watch/docs-update et leurs sources.
6. Retourner une preuve par fait, sans modification.

## Phase 1 — Matrice de vérité

Créer une matrice unique :

| Page | Fait actuel | Source de vérité | Écart | Action | Type |
|---|---|---|---|---|---|
| architecture.md | ... | config/commande | ... | corriger | manuelle/générée |

Classer chaque élément :

- actuel et conforme ;
- actuel mais périmé dans le wiki ;
- historique à conserver avec bandeau ;
- généré à corriger dans le script source ;
- doublon à fusionner ;
- non mesuré à ne pas affirmer.

## Phase 2 — Décisions de structure

Avant modification, trancher :

1. page canonique de l'architecture ;
2. pages historiques à archiver ;
3. contenu généré versus contenu éditorial ;
4. modèle de présentation des profils et bots ;
5. emplacement de la carte documentaire ;
6. chiffres dynamiques à renvoyer vers le dashboard plutôt qu'à figer dans le wiki ;
7. périmètre public versus documentation privée.

## Phase 3 — Mise à jour séquentielle

Ordre prévu après validation du plan :

1. architecture canonique et diagramme Mermaid ;
2. page architecture/profils/gateways/providers ;
3. page crons et automatisations ;
4. dashboards, services et ports ;
5. synchronisations, backups et watchdogs ;
6. carte documentaire et navigation ;
7. changelog et bandeaux historiques ;
8. cross-check des pages secondaires.

Pour chaque lot :

```text
patch source → tests structurels → build MkDocs strict → commit
→ déploiement de la destination correcte → page servie 200
→ vérification navigateur → mise à jour carte documentaire
```

## Phase 4 — Coordination et clôture

- relire les rapports LEO et Michel ensemble ;
- vérifier que toute affirmation possède une source réelle ;
- vérifier que les pages générées sont corrigées à leur source ;
- vérifier liens, nav, tableaux, Mermaid, dates et archives ;
- vérifier le site servi et non seulement les fichiers Markdown ;
- mettre à jour le changelog ;
- consigner les commits et les preuves ;
- clôturer le lot MyAC/documentaire seulement après validation complète.

## État initial mesuré

- Wiki source : `/home/tofdan/Projets_Dev/hermes-wiki`.
- Dernier commit observé : `286514e`.
- Hermes : `v0.19.0`, Python `3.14.4`.
- Jobs Michel : `72`, dont `70` no_agent et `2` LLM.
- Services observés : `8765`, `8766`, `9119`, `8793`.
- Écarts déjà visibles : anciennes valeurs `45`, `49`, `58` jobs ; anciennes dates de juillet/août ; modèles et architecture contradictoires ; mémoire/profils décrits de façon divergente.

## Interdit à ce stade

- aucune modification du wiki ;
- aucun commit/push ;
- aucune modification de cron, config ou script ;
- aucune suppression de page ;
- aucune réécriture des journaux historiques.

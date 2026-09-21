# Audit vérité terrain — Wiki Hermes et carte d’architecture

Date de mesure : 2026-09-21 03:34 (Europe/Brussels)
Auditeur : Michel
Périmètre : `/home/tofdan/Projets_Dev/hermes-wiki`, profils Hermes locaux, services et crons Michel.

## Résultat

L’architecture canonique et la carte documentaire sont cohérentes sur les éléments contrôlés. Une anomalie opérationnelle est confirmée : `hermes-gateway-michel.service` est en `activating (auto-restart)` alors que le port 9119, le dashboard et les autres services contrôlés répondent.

## Mesures croisées

| Élément | Source 1 | Source 2 | Résultat |
|---|---|---|---|
| Profils et providers | `/home/tofdan/.hermes/profiles/*/config.yaml` | `docs/hermes/architecture.md` | 6 profils observés ; `default`, `michel`, `robert`, `emile`, `gerard` sur Azure Foundry avec `gpt-5.6-luna`; `sylvia` sur OpenRouter avec `meta/muse-spark-1.3-contributor` |
| Crons Michel | `profiles/michel/cron/jobs.json` | `docs/hermes/architecture.md` | 72 jobs, 71 activés, 70 `no_agent`, 2 pilotés par agent : cohérent |
| Services | `ss -ltnp` | `systemctl --user list-units` | ports 8765/8766/9119/8793 à l’écoute ; services dashboard, docs, portail et My Émile actifs |
| HTTP | `curl` localhost | écoute réseau / processus | 8765=200, 8766=302, 9119=302, 8793=307 : routes joignables (redirections attendues) |
| Wiki | `git status` et `git log` | fichiers `docs/` et `mkdocs.yml` | branche `main` alignée avec `origin/main` avant ce lot ; architecture et carte présentes dans la navigation |
| Rapports source | `stat` sur les deux rapports du 20/09 | journal du 20/09 | 21 563 octets et 7 465 octets ; artefacts présents et lisibles |

## Correction documentaire effectuée

- La page canonique `hermes/architecture.md` est datée de cette mesure.
- La carte `hermes/utilisation/documentation-map.md` est datée de cette mesure.
- Ce rapport est ajouté à la navigation du Wiki.
- L’anomalie du gateway Michel reste explicitement séparée du lot documentaire : elle est confirmée, mais non corrigée ici sans mandat infrastructure distinct.

## Vérification

Le build MkDocs strict et la page servie doivent être exécutés après ce lot. La preuve de livraison est le commit du dépôt, complété par ce fichier et le résultat du build.

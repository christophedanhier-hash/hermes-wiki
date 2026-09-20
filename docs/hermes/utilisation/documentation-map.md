# 🗺️ Carte Documentaire — Wiki Hermes LEO

> **Référentiel de cohérence.** Toute évolution de la plateforme doit mettre à jour cette carte et les pages impactées dans le même lot.

## Source de vérité documentaire

- **Architecture courante** : [`hermes/architecture.md`](../architecture.md)
- **Architecture et communication détaillées** : [`hermes/architecture-communication.md`](../architecture-communication.md)
- **Profils et configuration** : [`hermes/configuration/profiles.md`](../configuration/profiles.md)
- **Providers** : [`hermes/configuration/providers.md`](../configuration/providers.md)
- **Dashboards** : [`hermes/utilisation/dashboards.md`](dashboards.md)
- **Changements** : `hermes/changelog.md` (page absente du dépôt actuel ; à recréer dans un lot dédié)

La page `hermes/architecture.md` est désormais la page canonique de l'état actuel. Les pages datées et historiques ne sont pas des sources de vérité courante.

## Pages critiques et dépendances

| Page | Rôle | Source principale | Dépendances |
|---|---|---|---|
| `hermes/architecture.md` | état de référence de la plateforme | configs, processus, ports, jobs | profils, providers, dashboards, changelog |
| `hermes/architecture-communication.md` | profils, interfaces et flux | architecture canonique + gateways | profils, bots, Hive |
| `hermes/configuration/profiles.md` | profils et mémoires | `profiles/*/config.yaml` | architecture |
| `hermes/configuration/providers.md` | routage LLM | configs et usage effectif | architecture |
| `hermes/utilisation/architecture-leo.md` | fonctionnement LEO et dashboards | architecture + collecteurs | dashboards, crons |
| `hermes/utilisation/dashboards.md` | interfaces de supervision | services et ports réels | architecture |
| `hermes/utilisation/documentation-map.md` | cette carte | inventaire Git + nav | toutes les pages critiques |

## Pages historiques

| Page | Traitement |
|---|---|
| `hermes/etat-des-lieux.md` | conserver comme historique ; ne pas utiliser pour les chiffres actuels |
| `hermes/decouvrir/ch03-architecture-leo.md` | conserver comme chapitre pédagogique ; réaligner ou marquer les instantanés historiques |
| archives et journaux datés | conserver sans réécrire les faits de leur date |

## Matrice des changements

| Changement | Pages à vérifier | Source de mesure |
|---|---|---|
| Provider ou modèle | architecture, profils, providers, communication | `profiles/*/config.yaml`, `session_model_usage` |
| Ajout/suppression de profil | architecture, profils, bots, carte | `profiles/`, registry Hive, gateways |
| Nouveau gateway ou bot | architecture, communication, bots | processus, état gateway, Telegram |
| Nouveau cron | architecture, dashboards, synchronisation | `profiles/michel/cron/jobs.json`, crontab hôte séparé |
| Nouveau dashboard ou service | architecture, dashboards | `ss -ltnp`, route HTTP, service |
| Backup ou watchdog | architecture, backup, sécurité | scripts et journaux réels |
| Pipeline documentaire | architecture, carte, changelog | scripts doc-watch/docs-update |
| Nouvelle page | navigation, carte, liens entrants | `mkdocs.yml`, build strict |

## Règles

1. Une valeur chiffrée indique son périmètre, sa source et sa date.
2. Une page générée est corrigée dans son script source avant régénération.
3. Un historique n'est jamais réécrit pour produire un faux état courant.
4. Une page supprimée ou déplacée impose une recherche des liens entrants et un build strict.
5. La preuve finale est la page servie, pas seulement le fichier Markdown.

## État de la présente carte

- Audit LEO : 20/09/2026.
- Audit infrastructure Michel : 20/09/2026.
- Wiki source : `/home/tofdan/Projets_Dev/hermes-wiki`.
- La migration des pages secondaires est planifiée par lots ; cette première version établit la page canonique et la matrice.

> Dernière mise à jour : **20/09/2026** — LEO, avec audit infrastructure Michel.

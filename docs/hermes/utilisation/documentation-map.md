# 🗺️ Carte Documentaire — Wiki Hermes LEO

> **Référentiel de cohérence transverse.** Toute évolution de la plateforme doit mettre à jour cette carte et les pages impactées dans le même lot éditorial.

---

## 1. Sources de vérité documentaire actives

L'architecture documentaire active du Wiki Hermes est organisée autour d'une référence canonique unique et de pages opérationnelles spécialisées :

- **Architecture de référence (canonique & consolidée)** : [`hermes/architecture.md`](../architecture.md)
- **Audit de vérité terrain (mesures directes)** : [`hermes/audit-verite-terrain-2026-09-21.md`](../audit-verite-terrain-2026-09-21.md)
- **Profils, mémoires et skills** : [`hermes/configuration/profiles.md`](../configuration/profiles.md)
- **Providers et routage des modèles LLM** : [`hermes/configuration/providers.md`](../configuration/providers.md)
- **Dashboards, supervision et services** : [`hermes/utilisation/dashboards.md`](dashboards.md)
- **Passerelles Telegram et Gateways** : [`hermes/utilisation/bots-telegram.md`](bots-telegram.md)
- **Sauvegardes et PRA** : [`hermes/utilisation/backup-recovery.md`](backup-recovery.md)
- **Sécurité documentaire & hygiène des secrets** : [`hermes/utilisation/securite.md`](securite.md)
- **Interface web native Hermes** : [`hermes/interface-web.md`](../interface-web.md)
- **Journal public des changements vérifiés** : [`hermes/changelog.md`](../changelog.md)

---

## 2. Consolidation documentaire de septembre 2026

Dans le cadre du chantier de consolidation de l'écosystème Hermes LEO, la documentation a fait l'objet d'une rationalisation majeure sans aucune perte de contenu :

### Fusion des documents d'architecture
Les trois documents d'architecture préexistants ont été consolidés en un **document actif unique** : [`hermes/architecture.md`](../architecture.md) :
1. `docs/hermes/architecture.md` (page socle) ;
2. `docs/hermes/architecture-communication.md` (profils, flux, Hive, rôles) ;
3. `docs/hermes/utilisation/architecture-leo.md` (dashboards, services, ordonnanceur, pipelines).

Les pages absorbées sont archivées avec bandeau de traçabilité dans :
- `docs/hermes/archives/architecture-2026/architecture-communication.md`
- `docs/hermes/archives/architecture-2026/architecture-leo.md`

### Retrait de la navigation active de pages secondaires
Quatre pages ont été retirées de la navigation du site pour resserrer le parcours utilisateur sur les composants opérationnels de référence :
- `docs/hermes/decisions/pourquoi-deepseek-pas-gemini.md` (analyse financière historique 07/2026) ;
- `docs/hermes/services/spotify.md` (plugin musical secondaire) ;
- `docs/hermes/utilisation/quotidien.md` (guide utilisateur générique) ;
- `docs/hermes/installation/linux.md` (procédure d'installation initiale).

Ces pages ont été déplacées dans `docs/hermes/archives/retirees-2026/` avec bandeau d'archive explicite. Leur contenu est intégralement préservé pour l'historique et la traçabilité.

---

## 3. Matrice des pages critiques et dépendances

| Page active | Rôle & Vocation | Sources de vérité directes | Dépendances & Pages associées |
|---|---|---|---|
| [`hermes/architecture.md`](../architecture.md) | État de référence absolu de la plateforme | `~/.hermes/profiles/*/config.yaml`, `jobs.json`, `ss -ltnp` | `profiles.md`, `providers.md`, `dashboards.md`, `changelog.md` |
| [`hermes/audit-verite-terrain-2026-09-21.md`](../audit-verite-terrain-2026-09-21.md) | Rapport de conformité terrain et contre-audit | Inspections processus, écoute réseau, registres | `architecture.md`, `documentation-map.md` |
| [`hermes/changelog.md`](../changelog.md) | Historique public des évolutions validées | Commits, tickets et mesures vérifiées | `architecture.md`, `profiles.md`, `providers.md` |
| [`hermes/configuration/profiles.md`](../configuration/profiles.md) | Configuration des 6 profils et mémoires dédiées | `~/.hermes/profiles/*/config.yaml` | `architecture.md`, `bots-telegram.md` |
| [`hermes/configuration/providers.md`](../configuration/providers.md) | Routage des modèles et fournisseurs LLM | Configuration Hermes + `session_model_usage` | `architecture.md` |
| [`hermes/utilisation/dashboards.md`](dashboards.md) | Interfaces de supervision et métriques | `collect-v2.py`, services HTTP 8765, 8766, 9119, 8793 | `architecture.md`, `backup-recovery.md` |
| [`hermes/utilisation/bots-telegram.md`](bots-telegram.md) | Passerelles de dialogue et gateways Telegram | Processus gateway, configuration Telegram | `architecture.md`, `profiles.md` |
| [`hermes/utilisation/backup-recovery.md`](backup-recovery.md) | Stratégie de sauvegarde, PRA et Recovery Kit | `leo-full-backup.py`, `jobs.json`, `recovery-kit/` | `architecture.md`, `securite.md` |
| [`hermes/utilisation/securite.md`](securite.md) | Règles d'hygiène, confinement et secrets | Fichiers d'environnement, permissions système | `backup-recovery.md` |
| [`hermes/interface-web.md`](../interface-web.md) | Interface utilisateur web Hermes Agent | Service natif port 9119 | `architecture.md` |
| [`hermes/utilisation/documentation-map.md`](documentation-map.md) | Référentiel transverse de cartographie | Inventaire Git + configuration `mkdocs.yml` | Toutes pages |

---

## 4. Section Historique & Archives

Les documents archivés sont conservés hors navigation active pour consultation historique sans altérer la clarté opérationnelle :

### Archives consolidées 2026 (`docs/hermes/archives/`)

| Fichier archivé | Contexte & Raison du classement | Référence active équivalente |
|---|---|---|
| `architecture-2026/architecture-communication.md` | Document fusionné — profils, gateways et flux Hive | [`hermes/architecture.md`](../architecture.md) |
| `architecture-2026/architecture-leo.md` | Document fusionné — supervision, services et ordonnanceur | [`hermes/architecture.md`](../architecture.md) |
| `retirees-2026/pourquoi-deepseek-pas-gemini.md` | Analyse financière comparative juillet 2026 | [`hermes/configuration/providers.md`](../configuration/providers.md) |
| `retirees-2026/spotify.md` | Fiche plugin musical Spotify | Hors navigation active |
| `retirees-2026/quotidien.md` | Guide générique d'usage initial | [`hermes/index.md`](../index.md) & [`hermes/architecture.md`](../architecture.md) |
| `retirees-2026/linux.md` | Guide d'installation initiale Debian/Ubuntu | [`hermes/index.md`](../index.md) |
| `decisions/pourquoi-deepseek-pas-copilot.md` | Décision comparative antérieure | [`hermes/configuration/providers.md`](../configuration/providers.md) |
| `automatisation-ch27-crons-horaires.md` | Ancien découpage thématique crons | [`hermes/architecture.md`](../architecture.md) |
| `dashboards-ch24-monitoring-crons.md` | Ancien découpage dashboards | [`hermes/utilisation/dashboards.md`](dashboards.md) |

### Autres pages historiques du dépôt
- `hermes/etat-des-lieux.md` : consigne les constats initiaux post-crash (juin 2026) ;
- `hermes/decouvrir/ch03-architecture-leo.md` : chapitre pédagogique initial ;
- `hermes/annexes/exemple-leo-complet.md` : retour d'expérience mono-profil historique ;
- Journaux datés (`journal-*.md`) : conservés sans modification rétroactive.

---

## 5. Matrice des changements et règles de traçabilité

| Typologie du changement | Pages à réviser systématiquement | Source de vérité à vérifier |
|---|---|---|
| Modification de modèle ou fournisseur LLM | `architecture.md`, `providers.md`, `profiles.md`, `changelog.md` | `profiles/*/config.yaml`, métriques d'usage |
| Création, renommage ou suppression de profil | `architecture.md`, `profiles.md`, `bots-telegram.md`, `documentation-map.md` | `~/.hermes/profiles/`, registre Hive |
| Nouvelle passerelle, bot ou gateway | `architecture.md`, `bots-telegram.md` | Processus, passerelles actives, configuration Telegram |
| Ajout ou modification de tâche planifiée | `architecture.md`, `dashboards.md`, `backup-recovery.md` | `~/.hermes/profiles/michel/cron/jobs.json` |
| Évolution de port ou service réseau | `architecture.md`, `dashboards.md` | `ss -ltnp`, réponse HTTP et contenu servi |
| Évolution des scripts de sauvegarde ou PRA | `architecture.md`, `backup-recovery.md`, `securite.md` | `leo-full-backup.py`, `recovery-kit/` |
| Ajout ou déplacement de page | `mkdocs.yml`, `documentation-map.md`, liens entrants | `mkdocs build --strict` |

---

## 6. Règles de maintenance documentaire LEO

1. **Exactitude factuelle** : Citer la source directe, le fichier et la date de mesure pour tout indicateur chiffré.
2. **Priorité au script source** : Pour tout fichier généré automatiquement, corriger le script amont avant régénération.
3. **Respect du passé** : Ne jamais modifier les données d'un journal ou d'une archive datée pour feindre un état courant.
4. **Vérification d'intégrité stricte** : Tout déplacement ou renommage impose le contrôle des liens relatifs entrants et la validation par `mkdocs build --strict`.
5. **Preuve finale par le service** : La conformité finale se valide sur la documentation compilée et servie, pas uniquement sur le Markdown brut.

---

> 🤖 Carte mise à jour le **21/09/2026** — LEO 🦁 & Michel 🔧.
> Référentiel de conformité : Wiki Hermes (`/home/tofdan/Projets_Dev/hermes-wiki`).

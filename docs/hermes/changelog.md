# 📜 Changelog — Changements Vérifiés de l'Écosystème Hermes

> **Page canonique de référence :** [`hermes/architecture.md`](architecture.md). Mesures vérifiées le **20/09/2026**.
> Ce journal public consigne exclusivement les évolutions d'architecture, de configuration et de documentation vérifiées et mesurées sur l'environnement de production LEO.

---

## 20/09/2026 — Réalignement canonique de la documentation & audit plateforme

### 🔍 Mesures vérifiées sur l'environnement LEO (20/09/2026)

Un audit complet de la plateforme Hermes Agent et de ses profils a été mené le 20/09/2026. Les mesures suivantes constituent l'état de référence :

- **Runtime & Version** : Hermes Agent `v0.19.0` sous Python `3.14.4` (`/home/tofdan/.hermes/venv/bin/hermes`).
- **Profils opérationnels (6 profils)** :
    - `default` : LEO, agent principal de dialogue, de veille et de pilotage général.
    - `michel` : copilote infrastructure, crons, watchdogs et déploiements.
    - `robert` : conseil stratégique, gouvernance IT et architecture.
    - `sylvia` : logistique de voyages et roadbooks camping-car.
    - `emile` : assistant professionnel d'Émilie dans My Émile IA Workbench (Avenyra) : rédaction, structuration et gestion des notes, rapports, activités et documents pro (validation humaine).
    - `gerard` : assistant astronomie et astrophotographie de Christophe, suivi du site tofdan/astro, documentation générale et guide d'étude (dont projet T600).
    - *Note d'identité* : **LEO est un agent Hermes** (profil `default`) opérant via le gateway Hermes en DM direct avec Christophe (aucun handle Telegram inventé). `leo` est l'alias Hive du profil `default`, et non un septième profil.
- **Routage LLM & Providers configurés** :
    - Profils `default`, `michel`, `robert`, `emile`, `gerard` : **Azure Foundry** avec le modèle `gpt-5.6-luna` et secours déclaré vers Google Gemini (`custom:google/gemini-3.7-flash` ou Google Gemini selon configuration).
    - Profil `sylvia` : **OpenRouter** avec le modèle `meta/muse-spark-1.3-contributor`.
- **Jobs planifiés Michel** (`~/.hermes/profiles/michel/cron/jobs.json`) :
    - 72 jobs planifiés au total : **71 activés**, 70 exécutés sans LLM (`no_agent`), **2 jobs pilotés par LLM**.
- **Services locaux et interfaces actives** :
    - Port `8765` : Panel LEO (métriques, crons et pilotage).
    - Port `8766` : Leo Docs (explorateur documentaire).
    - Port `9119` : Hermes Dashboard (supervision de la plateforme).
    - Port `8793` : Workbench My Émile IA (écoute locale localhost, développé via Avenyra).
- **Mémoire & Isolation** :
    - Mémoires strictement indépendantes par profil (`~/.hermes/profiles/<nom>/memories/`). Aucune mémoire partagée.
- **Communication inter-profils** :
    - Bus Hive inter-profils pour le passage asynchrone de messages et le suivi des obligations.
- **Suivi d'infrastructure** :
    - Constat documenté sans masquage : boucle d'auto-restart de l'unité systemd Michel (conflit de PID actif sur le gateway), prise en charge séparée dans le runbook infrastructure.

---

### 📦 Commits structurants de la mise à jour documentaire

#### Commit `62aba3c` — Socle d'architecture canonique & navigation (Lot 1)
- **Création de la page canonique** [`hermes/architecture.md`](architecture.md) : état de référence de la plateforme issu des mesures directes (profils, ports, jobs, pipelines).
- **Refonte de la carte documentaire** [`hermes/utilisation/documentation-map.md`](utilisation/documentation-map.md) : matrice d'impact des changements et règles de traçabilité.
- **Alignement navigation** : ajout de la référence canonique dans `mkdocs.yml` et mise à jour de [`hermes/TABLE.md`](TABLE.md).
- **Nettoyage des liens** : suppression des renvois obsolètes et correction des liens brisés.

#### Commit `000a3f6` — Profils, providers, bots et dashboards (Lot 2)
- **Profils** ([`hermes/configuration/profiles.md`](configuration/profiles.md)) : description des 6 profils opérationnels, confirmation de l'isolation mémoire et clarification de l'alias Hive `leo`.
- **Providers** ([`hermes/configuration/providers.md`](configuration/providers.md)) : actualisation du routage LLM (Azure Foundry `gpt-5.6-luna`, OpenRouter `meta/muse-spark-1.3-contributor`, fallbacks Gemini).
- **Interfaces Telegram** ([`hermes/utilisation/bots-telegram.md`](utilisation/bots-telegram.md)) : rétablissement de la réalité des gateways, retrait des handles Telegram fictifs, LEO en DM direct.
- **Architecture LEO & Dashboards** ([`hermes/architecture.md`](architecture.md), [`hermes/utilisation/dashboards.md`](utilisation/dashboards.md)) : réalignement des 4 services locaux (8765, 8766, 9119, 8793) et des 72 jobs Michel.

#### Présente mise à jour — Changelog et Communication (Lot 3)
- **Création de cette page** [`hermes/changelog.md`](changelog.md) : traçabilité publique des changements vérifiés.
- **Réalignement de l'architecture de communication** ([`hermes/architecture.md`](architecture.md)) : conformité avec les 6 profils, routage Azure/OpenRouter, intégration Hive et séparation des faits historiques.
- **Mise à jour de la navigation** : référencement de `changelog.md` dans `mkdocs.yml` et `documentation-map.md`.

#### Correction documentaire ciblée — Rôles opérationnels réels d'Émile et Gérard (20/09/2026)
- **Émile** : Rectification du profil. Émile n'est plus un assistant de formation/mémoire (phase pédagogique initiale terminée). Il est l'assistant professionnel d'Émilie dans My Émile IA Workbench (développé via Avenyra) pour rédiger, structurer et gérer notes, rapports, activités et documents professionnels (avec validation humaine).
- **Gérard** : Rectification du profil. Gérard n'est pas limité aux dossiers T600/OCA (projet parmi d'autres). Il est l'assistant de Christophe pour l'astronomie, l'astrophotographie, le wiki et le site tofdan liés à l'astronomie, la documentation générale et son étude comme guide astronomie. Aucun bot Telegram inventé.
- **Alignement transverse** : Révision coordonnée des pages actives et chapitres de configuration (`architecture.md`, `profiles.md`, `providers.md`, `bots-telegram.md`, `dashboards.md`, `backup-recovery.md`, `interface-web.md`).

---

#### Refonte complète de la table de la plateforme — 21/09/2026
- Remplacement de `hermes/TABLE.md`, devenue obsolète après les évolutions Hermes/LEO.
- Nouvelle structure centrée sur les 6 profils, les services actuels, Leo Docs, LEO Knowledge, le pipeline multi-profils, la sécurité et les parcours opérationnels.
- Conservation de l’ancienne version dans `hermes/archives/retirees-2026/table-legacy-2026-09-21.md`.
- Build strict et liens vérifiés avant publication.

---

## 🏛️ Rappels des faits historiques antérieurs

> [!NOTE]
> Les mentions ci-dessous sont conservées à titre d'archive technique pour éclairer l'évolution de la plateforme et ne doivent pas être lues comme un état opérationnel actuel.

- **11/07/2026 — Suppression de la mémoire partagée** : arrêt du mécanisme de synchronisation transverse des mémoires et bascule sur le modèle hermétique où chaque profil détient exclusivement ses propres `memories/`.
- **26/07/2026 — Rationalisation des profils** : renommage du profil `bureau-robert` en `robert` ; attribution formelle des crons et de l'infrastructure au profil `michel`.
- **Rôles initiaux d'Émile et Gérard** : Le profil `emile` a débuté comme assistant pour les études et la rédaction du mémoire de fin d'études avant son affectation professionnelle au workbench Avenyra. Le profil `gerard` a d'abord été documenté sur la seule documentation T600/OCA avant la prise en compte complète de ses activités d'astronomie et du site tofdan.
- **Anciennes configurations de modèles** : utilisation historique de DeepSeek V4 (Flash / Pro) et compteurs antérieurs (45 à 58 crons selon les étapes de consolidation de juillet et août 2026), supplantés par la stack actuelle mesurée au 20/09/2026.

---

*Document mis à jour le 20/09/2026 — LEO 🦁 & Michel 🔧*

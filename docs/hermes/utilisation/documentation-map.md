# 🗺️ Carte Documentaire — Wiki Hermes LEO

> **Usage** : quand une modification système impacte la documentation, cette carte indique **quelles pages** doivent être mises à jour.
> **Règle** : toute modification de la plateforme LEO → mettre à jour cette carte ET les pages impactées dans le même mouvement.

## 📄 Pages du wiki

| # | Page | Couvre | Pages liées | Statut |
|:-:|:-----|:-------|:------------|:------:|
| 1 | `index.md` | Portail d'accueil, résumé écosystème | Toutes | ✅ |
| 2 | `architecture.md` | Architecture système (serveur, conteneurs) | 3, 7 | ✅ |
| 3 | `architecture-communication.md` | **5 bots** (LEO, Copilot, Émile, Voyages, Robert), routage, sync mémoire | 7, 13, 20 | ✅ |
| 4 | `changelog.md` | Historique des modifications | Toutes | ✅ |
| 5 | ~~`etat-des-lieux.md`~~ | **ARCHIVÉ** — inventaire pré-crash, obsolète | 14, 18, 20 | ❌ |
| 6 | `interface-web.md` | Interface web Hermes | — | ✅ |
| 7 | ~~`exemples/LEO.md`~~ | **SUPPRIMÉ** — remplacé par guide v3+ (archives) | — | ❌ |
| 8 | `configuration/profiles.md` | **5 profils**, gateways, skills, mémoire | 20 | ✅ |
| 9 | `configuration/providers.md` | Providers LLM (deepseek, google, ollama) | 7, 14 | ✅ |
| 10 | `installation/linux.md` | Installation Linux | — | ✅ |
| 11 | `installation/windows.md` | Installation Windows | — | ✅ |
| 12 | `utilisation/quotidien.md` | Usage quotidien comme LEO | 7 | ✅ |
| 13 | `utilisation/bots-telegram.md` | **5 bots**, tokens, architecture | 3, 7, 14 | ✅ |
| 14 | `utilisation/architecture-leo.md` | Dashboard unifié, collect-v2, crons, 🐍 workflows Python, vaults, routage LLM | 7, 15, 16, 19, 21 | ✅ |
| 15 | `utilisation/crons.md` | **41 crons** (tous actifs, leo-copilot exclusif), collect-v2 | 14, 16, 21 | ✅ |
| 16 | `utilisation/dashboards.md` | **1 dashboard unifié** (leo-dashboard), 8 sources (n8n retiré 13/07/2026), vaults | 14, 15, 19 | ✅ |
| 17 | `utilisation/backup-recovery.md` | Backup & recovery | 14 | ✅ |
| 18 | `utilisation/skills-catalogue.md` | Catalogue des skills BAVI LEO & Hermes | 5, 20 | ✅ |
| 19 | ~~`services/n8n.md`~~ | **ARCHIVÉ** — n8n déprécié le 13/07/2026, remplacé par 🐍 workflows Python | 14, 16 | ❌ |
| 20 | `services/spotify.md` | Contrôle musical Spotify | — | ✅ |
| 21 | `utilisation/securite.md` | Sécurité — bonnes pratiques documentaires, données sensibles | Toutes | ✅ |
| 22 | `utilisation/documentation-map.md` | **Cette carte** — référentiel de cohérence | Toutes | ✅ |
| — | ~~`services/gardien-drive.md`~~ | **ARCHIVÉ** — workflow n8n déprécié, sync via scripts Python | 19 | ❌ |
| — | ~~`etat-des-lieux.md`~~ | **ARCHIVÉ** — inventaire pré-crash, obsolète | — | ❌ |
| — | ~~`services/n8n.md`~~ | **ARCHIVÉ** — voir ci-dessus | — | ❌ |
| — | `bureaux/ch14-bureau-robert.md` | Robert — conseiller stratégique IA (Solidaris) | 3, 13, 8 | ✅ |
| — | `audit-documents-a-reviser.md` | Suivi des corrections post-audit | Toutes | ✅ |
| — | `hermes/index.md` | Présentation Hermes Agent, philosophie LEO | 9, 12 | ✅ |
| 23 | `decisions/pourquoi-deepseek-pas-gemini.md` | Choix DeepSeek vs Gemini, prix juillet 2026 | 7, 9, 14 | ✅ |

### Pages archivées (plus dans la navigation)

| Page | Archivée le | Raison |
|:-----|:-----------:|:-------|
| `archives/dashboards-ch24-monitoring-crons.md` | 04/07/2026 | 7 dashboards obsolètes → 1 unifié |
| `archives/decisions/pourquoi-deepseek-pas-copilot.md` | 04/07/2026 | Décision dépassée (Copilot → Gemini) |
| `archives/automatisation-ch27-crons-horaires.md` | 30/06/2026 | Ancien système de crons |
| `archives/exemples-LEO.md` | 30/06/2026 | Remplacé par guide v3+ |
| `archives/skills-ch17-skills-productivite.md` | 30/06/2026 | Refonte skills |
| `archives/skills-ch18-skills-devops.md` | 30/06/2026 | Refonte skills |
| `archives/services-analyse-gestion-releases.md` | 30/06/2026 | Obsolète |

## 🔗 Graphe de dépendances

Quand tu modifies **cette page** → vérifie aussi celles-ci :

```
architecture-communication.md (3)
  → bots-telegram.md (13)        ← Architecture bots, routage 5 profils
  → architecture-leo.md (14)     ← Routage LLM, collect-v2

bots-telegram.md (13)
  → architecture-communication.md (3)  ← Cohérence 5 bots

configuration/providers.md (9)
  → architecture-leo.md (14)     ← Providers utilisés

crons.md (15)
  → dashboards.md (16)           ← Métriques des crons (collect-v2)
  → architecture-leo.md (14)     ← Watchdogs, déploiement

dashboards.md (16)
  → crons.md (15)                ← Crons associés
  → architecture-leo.md (14)     ← Architecture
```

## 📋 Checklist mise à jour documentaire

Quand tu changes... | Pages à vérifier
:-------------------|:----------------
**Provider LLM** (ex: DeepSeek→autre) | 3, 9, 13, 14
**Ajout/suppression bot** | 3, 5, 8, 13, 14
**Nouveau cron** | 14, 15, 16
**Nouveau dashboard / collecteur** | 14, 16
**Modification collect-v2.py** | 14, 15, 16
**Nouveau skill** | 18
**Modif config serveur** | 2
**Ajout/suppression vault** | 14, 16
**Déploiement horaire** | 14, 15
**Changement structure profils** | 3, 8, 13, 14

## 📌 Pages critiques (toujours vérifier en premier)

1. **`architecture-communication.md`** — Vision globale, routage, 5 bots
2. **`utilisation/architecture-leo.md`** — Dashboard unifié, collect-v2, vaults, workflows Python
3. **`utilisation/dashboards.md`** — leo-dashboard, 8 sources (n8n retiré 13/07/2026)
4. **`changelog.md`** — Historique des modifs
5. **`utilisation/crons.md`** — 41 crons (tous actifs), planification
6. **Cette carte** 🗺️

---

*Document mis à jour le 17/07/2026 — Michel (leo-copilot) 🔧*

---

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)


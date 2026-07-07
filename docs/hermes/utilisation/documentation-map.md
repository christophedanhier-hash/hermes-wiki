# 🗺️ Carte Documentaire — Wiki Hermes LEO

> **Usage** : quand une modification système impacte la documentation, cette carte indique **quelles pages** doivent être mises à jour.
> **Règle** : toute modification de la plateforme LEO → mettre à jour cette carte ET les pages impactées dans le même mouvement.

## 📄 Pages du wiki

| # | Page | Couvre | Pages liées | Statut |
|:-:|:-----|:-------|:------------|:------:|
| 1 | `index.md` | Portail d'accueil, résumé écosystème | Toutes | ✅ |
| 2 | `architecture.md` | Architecture système (serveur, conteneurs) | 3, 7 | ✅ |
| 3 | `architecture-communication.md` | **4 bots** (LEO, Copilot, Émile, Voyages), routage, sync mémoire | 7, 13, 20 | ✅ |
| 4 | `changelog.md` | Historique des modifications | Toutes | ✅ |
| 5 | `etat-des-lieux.md` | Installation Hermes de Christophe (inventaire) | 14, 18, 20 | ✅ |
| 6 | `interface-web.md` | Interface web Hermes | — | ✅ |
| 7 | `exemples/LEO.md` | Architecture LEO (provider, routage, dashboards) | 3, 14, 20, 21 | ✅ |
| 8 | `configuration/profiles.md` | Profils, gateways, skills | 20 | ✅ |
| 9 | `configuration/providers.md` | Providers LLM (DeepSeek, Gemini, Ollama) | 7, 14 | ✅ |
| 10 | `installation/linux.md` | Installation Linux | — | ✅ |
| 11 | `installation/windows.md` | Installation Windows | — | ✅ |
| 12 | `utilisation/quotidien.md` | Usage quotidien comme LEO | 7 | ✅ |
| 13 | `utilisation/bots-telegram.md` | **4 bots**, tokens, architecture | 3, 7, 14 | ✅ |
| 14 | `utilisation/architecture-leo.md` | Dashboard unifié, collect-v2, crons, n8n, vaults, routage LLM | 7, 15, 16, 19, 21 | ✅ |
| 15 | `utilisation/crons.md` | Tâches planifiées, collect-v2, déploiement horaire | 14, 16, 21 | ✅ |
| 16 | `utilisation/dashboards.md` | **1 dashboard unifié** (leo-dashboard), 9 sources, vaults | 14, 15, 19 | ✅ |
| 17 | `utilisation/backup-recovery.md` | Backup & recovery | 14 | ✅ |
| 18 | `utilisation/skills-catalogue.md` | Catalogue des skills BAVI LEO & Hermes | 5, 20 | ✅ |
| 19 | `services/n8n.md` | n8n — 3 workflows (Drive, Gardien, Contacts) | 14, 16 | ✅ |
| 20 | `services/spotify.md` | Contrôle musical Spotify | — | ✅ |
| 21 | `aller-plus-loin/references.md` | Aide-mémoire commandes Hermes | — | ✅ |
| 22 | `aller-plus-loin/troubleshooting.md` | Problèmes courants | — | ✅ |
| 23 | ~~`dashboards/n8n.md`~~ | **SUPPRIMÉ** (dashboard n8n 404, remplacé par leo-dashboard) | — | ❌ |
| 24 | `decisions/pourquoi-deepseek-pas-gemini.md` | Choix DeepSeek vs Gemini, prix juillet 2026 | 7, 9, 14 | ✅ |
| — | `services/gardien-drive.md` | Gardien du Drive (workflow n8n) | 19 | ✅ |

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
  → bots-telegram.md (13)        ← Architecture bots, routage 4 profils
  → architecture-leo.md (14)     ← Routage LLM, collect-v2
  → exemples/LEO.md (7)          ← Exemple concret
  → etat-des-lieux.md (5)        ← Inventaire

bots-telegram.md (13)
  → architecture-communication.md (3)  ← Cohérence 4 bots
  → exemples/LEO.md (7)               ← Routage

configuration/providers.md (9)
  → architecture-leo.md (14)     ← Providers utilisés
  → exemples/LEO.md (7)          ← Exemple config

crons.md (15)
  → dashboards.md (16)           ← Métriques des crons (collect-v2)
  → architecture-leo.md (14)     ← Watchdogs, déploiement

dashboards.md (16)
  → crons.md (15)                ← Crons associés
  → architecture-leo.md (14)     ← Architecture
  → services/n8n.md (19)         ← Source n8n du collecteur

services/n8n.md (19)
  → dashboards.md (16)           ← Monitoring via leo-dashboard
  → architecture-leo.md (14)     ← Intégration collect-v2
```

## 📋 Checklist mise à jour documentaire

Quand tu changes... | Pages à vérifier
:-------------------|:----------------
**Provider LLM** (ex: DeepSeek→autre) | 3, 7, 9, 13, 14
**Ajout/suppression bot** | 3, 5, 13, 14
**Nouveau cron** | 14, 15, 16
**Nouveau dashboard / collecteur** | 14, 16
**Modification collect-v2.py** | 14, 15, 16, 19
**Nouveau skill** | 5, 18
**Modif config serveur** | 2, 5
**Ajout/suppression vault** | 14, 16
**Modification n8n workflow** | 14, 16, 19
**Déploiement horaire** | 14, 15

## 📌 Pages critiques (toujours vérifier en premier)

1. **`architecture.md`** — Vue macro, budget, crons
2. **`architecture-communication.md`** — Vision globale, routage, 4 bots
3. **`utilisation/architecture-leo.md`** — Dashboard unifié, collect-v2, vaults, n8n
4. **`utilisation/dashboards.md`** — leo-dashboard, 9 sources
5. **`etat-des-lieux.md`** — Inventaire complet
6. **`services/n8n.md`** — Workflows n8n actuels
7. **`changelog.md`** — Historique des modifs
8. **Cette carte** 🗺️

---

*Document mis à jour le 07/07/2026 — 02:45 — Léo 🦁*

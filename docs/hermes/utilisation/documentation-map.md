# 🗺️ Carte Documentaire — Wiki Hermes LEO

> **Usage** : quand une modification système (changement de provider, ajout/suppression de bot, nouveau service) impacte la documentation, cette carte indique **quelles pages** doivent être mises à jour.

## 📄 Pages du wiki

| # | Page | Couvre | Pages liées |
|:-:|:-----|:-------|:------------|
| 1 | `index.md` | Portail d'accueil, résumé écosystème | Toutes |
| 2 | `architecture.md` | Architecture système (serveur, conteneurs) | 3, 7 |
| 3 | `architecture-communication.md` | **3 bots** (LEO, Copilot, Voyages), routage, sync mémoire | 7, 20 |
| 4 | `changelog.md` | Historique des modifications | Toutes |
| 5 | `etat-des-lieux.md` | Installation Hermes de Christophe (inventaire) | 20, 21, 22 |
| 6 | `interface-web.md` | Interface web Hermes | — |
| 7 | `exemples/LEO.md` | Architecture LEO concrète (provider, routage, dashboards) | 3, 20, 21, 22 |
| 8 | `configuration/profiles.md` | Profils, gateways, skills | 20 |
| 9 | `configuration/providers.md` | Providers LLM (DeepSeek, Gemini, Ollama) | 7, 20 |
| 10 | `installation/linux.md` | Installation Linux | — |
| 11 | `installation/windows.md` | Installation Windows | — |
| 12 | `utilisation/quotidien.md` | Usage quotidien comme LEO | 7 |
| 13 | `utilisation/bots-telegram.md` | **3 bots** (DeepSeek, Copilot→Gemini, Voyages), tokens, architecture | 3, 7, 20 |
| 14 | `utilisation/architecture-leo.md` | Dashboards, crons, n8n, routage LLM | 7, 15, 16, 21 |
| 15 | `utilisation/crons.md` | Tâches planifiées (liste complète) | 14, 16, 21 |
| 16 | `utilisation/dashboards.md` | Dashboards LEO (7 dashboards) | 14, 15, 21 |
| 17 | `utilisation/backup-recovery.md` | Backup & recovery | 14 |
| 18 | `utilisation/skills-catalogue.md` | Catalogue des skills BAVI LEO & Hermes | 5, 20 |
| 19 | `services/n8n.md` | Automatisation n8n | 14, 21 |
| 20 | `services/spotify.md` | Contrôle musical Spotify | — |
| 21 | `aller-plus-loin/references.md` | Aide-mémoire commandes Hermes | — |
| 22 | `aller-plus-loin/troubleshooting.md` | Problèmes courants | — |
| 23 | `dashboards/n8n.md` | Dashboard n8n | 14, 19 |

## 🔗 Graphe de dépendances

Quand tu modifies **cette page** → vérifie aussi celles-ci :

```
architecture-communication.md (3)
  → bots-telegram.md (13)        ← Architecture bots, routage
  → architecture-leo.md (14)     ← Routage LLM
  → exemples/LEO.md (7)          ← Exemple concret
  → etat-des-lieux.md (5)        ← Inventaire

bots-telegram.md (13)
  → architecture-communication.md (3)  ← Cohérence 3 bots
  → exemples/LEO.md (7)               ← Routage

configuration/providers.md (9)
  → architecture-leo.md (14)     ← Providers utilisés
  → exemples/LEO.md (7)          ← Exemple config

crons.md (15)
  → dashboards.md (16)           ← Métriques des crons
  → architecture-leo.md (14)     ← Watchdogs

dashboards.md (16)
  → crons.md (15)                ← Crons associés
  → architecture-leo.md (14)     ← Architecture
```

## 📋 Checklist mise à jour documentaire

Quand tu changes... | Pages à vérifier
:-------------------|:----------------
**Provider LLM** (ex: Copilot→Gemini) | 3, 7, 9, 13, 14
**Ajout/suppression bot** | 3, 5, 13, 20
**Nouveau cron** | 14, 15, 16
**Nouveau dashboard** | 14, 16
**Nouveau skill** | 5, 18
**Modif config serveur** | 2, 5

## 📌 Pages critiques (toujours vérifier en premier)

1. **`architecture-communication.md`** — Vision globale, routage, bots
2. **`exemples/LEO.md`** — Exemple concret de toute la stack
3. **`bots-telegram.md`** — Détail des bots
4. **`etat-des-lieux.md`** — Inventaire complet
5. **`architecture-leo.md`** — Architecture fonctionnelle

# Architecture LEO — Exemple concret

> **Document généré le** : 19/06/2026 | **Source** : Audit complet environnement LEO

---

## Identité

| Propriété | Valeur |
|-----------|--------|
| **Nom** | LEO |
| **Type** | Majordome numérique |
| **Hôte** | Serveur dédié (bare-metal) |
| **OS Hôte** | Ubuntu 26.04 LTS (Resolute Raccoon) |
| **Kernel** | Linux 7.0.0-22-generic |
| **Conteneur** | Docker (hermes-agent) |
| **Canal principal** | Telegram |
| **Profils** | 2 : `default` + `bavi-leo` |

---

## Matériel serveur

| Composant | Détail |
|-----------|--------|
| **CPU** | Intel Core i7-7700K (Kaby Lake, 2017) — 4 cœurs / 8 threads @ 4.2 GHz |
| **RAM** | 22,9 GiB DDR4 (~17 GiB libre) |
| **GPU** | NVIDIA RTX 3050 8GB GDDR6 (CUDA 13.2, driver 595.71.05) |
| **Disque 1** | 457 GB (sda2, ext4) — ~371 GB libre |
| **Disque 2** | 915 GB (sdb, ext4) — ~480 GB libre |
| **Swap** | 8,0 GiB (32% utilisé) |
| **Uptime** | ~15 jours (démarré ~5 juin 2026) |

---

## Docker

| Conteneur | Image | Statut | Uptime | Ports |
|-----------|-------|--------|--------|-------|
| **hermes-agent** | hermes-agent | 🟢 Running | 7 jours | 8080, 9119 |
| **ollama** | ollama/ollama | 🟢 Running | 6 jours | 11434 → host |

- **Modèle Ollama installé :** `qwen2.5:7b` (4.7 GB)
- **GPU support :** ✅ Oui (nvidia.com/gpu=0, CDI configuré)
- **Volumes :** ollama_data, open-webui
- **Network :** host (hermes-agent), bridge (ollama)

---

## Hermes Agent

| Propriété | Valeur |
|-----------|--------|
| **Version** | v0.16.0 (build 2026.6.5) |
| **Python** | 3.13.5 |
| **Installation** | `/opt/hermes` |
| **Config** | `/opt/data/config.yaml` |
| **Secrets** | `/opt/data/.env` |
| **Domaines** | 103 skills, 17 crons, 2 profils |

### Profils

| Profil | Modèle | Provider | Gateway | Usage |
|--------|--------|----------|---------|-------|
| **default** | `deepseek-chat` | DeepSeek | Telegram LEO | Conversations, analyses, maintenance |
| **bavi-leo** | `deepseek-v4-flash` | DeepSeek | Telegram bot voyages | Bot voyages partagé (@bavi_leo_voyages_bot) |

### Sessions

- **Total :** 90 sessions (62 Telegram, 3 CLI, 25 autres)
- **Messages :** 4 651
- **Base de données :** 79,1 Mo (state.db)

---

## Providers LLM

| Provider | Rôle | Coût | Statut |
|----------|------|------|--------|
| **DeepSeek 🤖** | Principal (Telegram, analyses complexes) | Payant (~$28 solde restant) | ✅ Actif |
| **Ollama 🏠** | Local gratuit (qwen2.5:7b) | Gratuit (RTX 3050) | ✅ Actif |
| **Gemini ⚡** | Fallback automatique | Gratuit (quota API) | ✅ Configuré |

---

## Crons — 17 jobs

Tous les crons tournent en `no_agent` (0 token LLM) sauf `veille-ia-quotidienne` et `gmail-classifier`.

| Horaire | Cron | Description |
|---------|------|-------------|
| **06:00** | daily-backup | Backup fichiers critiques → Google Drive |
| **08:00** | docs-update | Mise à jour docs techniques T600 |
| **08:00** | veille-ia-quotidienne | Veille IA (11 sources RSS → email) |
| **09:00** | check-hermes-update | Vérifie nouvelle version Hermes |
| **Lun 09:00** | credentials-check | Vérification validité tokens OAuth |
| **H:00** | machines-kpi | Collecte CPU/RAM/disque 3 machines |
| **H:05** | budget-check-v6 | Relevé solde DeepSeek + projection |
| **H:10** | dashboard-leo | Dashboard KPI Hermes |
| **H:15** | leo-metrics | Dashboard 3 machines |
| **H:20** | crons-dashboard | Monitoring de tous les crons |
| **H:25** | github-dashboard | Activité GitHub (20 repos) |
| **H:30** | wiki-sync | Synchronisation sources → Wiki MkDocs |
| **H:35** | wiki-oca-sync | Sync documentation T600 |
| **H:36** | t600-drive-sync | Sync Drive → T600 |
| **Every 60m** | bavi-leo-dashboard | Dashboard BAVI LEO |
| **18:00** | drive-sync | Sync bidirectionnelle Drive ↔ GitHub |
| ***/15** | gmail-classifier | Classification emails Gmail |

---

## Dashboards — 6 (+ 1 hub)

| Dashboard | URL | Cron | Technologie |
|-----------|-----|------|-------------|
| **Hub Monitoring** | [localhost:8080](http://localhost:8080) | Statique | HTML + CSS |
| **LEO KPI** | [dashboard-leo](https://christophedanhier-hash.github.io/dashboard-leo/) | H:10 | HTML + Chart.js |
| **Machines** | [leo-metrics](https://christophedanhier-hash.github.io/leo-metrics/) | H:15 | HTML + Chart.js |
| **Crons** | [crons-dashboard](https://christophedanhier-hash.github.io/crons-dashboard/) | H:20 | HTML + CSS pur |
| **GitHub** | [github-dashboard](https://christophedanhier-hash.github.io/github-dashboard/) | H:25 | HTML + CSS pur |
| **BAVI LEO** | [bavi-leo-dashboard](https://christophedanhier-hash.github.io/bavi-leo-dashboard/) | Every 60m | HTML + Chart.js |

Serveur local (s6 supervision) : dashboard interne à `localhost:9119`.

---

## Réseau et ports

### Interfaces réseau

| Interface | Type | Adresse |
|-----------|------|---------|
| **enp4s0** | Ethernet | 192.168.1.XXX |
| **tailscale0** | Tailscale | 100.92.102.28 (LEO) |
| **docker0** | Docker bridge | 172.17.0.1 |

### Machines Tailscale

| Machine | Adresse | Statut |
|---------|---------|--------|
| **LEO** | 100.92.102.28 | ✅ Connecté |
| **penguin** | 100.113.110.40 | ⚠️ Offline |
| **yoga-260-tofdan** | 100.88.78.6 | ⚠️ Offline |
| **brya** | — | ⚠️ Offline |

### Ports ouverts

| Port | Service | Interface |
|:----:|---------|-----------|
| 22 | SSH | Toutes |
| 53 | systemd-resolved | Local |
| 443 | HTTPS (LEO) | Toutes |
| 631 | CUPS | Local |
| 11434 | Ollama | localhost + Tailscale |
| 8080 | HTTP server (dashboards) | localhost |
| 9119 | s6 dashboard | localhost |
| 18791-18792 | Services Hermes | Tailscale |
| 49417 | Tailscale IPv6 | tailscale0 |

---

## GitHub — 30 repos

| Type | Nb | Exemples |
|------|:--:|----------|
| **Wikis** | 4 | hermes-wiki, BAVI_LEO, wiki-oca, voyages-wiki |
| **Dashboards** | 5 | dashboard-leo, leo-metrics, crons-dashboard, github-dashboard, bavi-leo-dashboard |
| **Drive** | 1 | hermes-christophe |
| **Guides** | 1 | hermes-guide |
| **Autres publics** | 2 | dashboard-kpi, machine-metrics |
| **Privés / forks** | ~17 | (divers) |

**GitHub Actions :** 9 workflows, tous ✅ success.
**Token scopes :** admin:org, repo, workflow, write:packages.

---

## Budget DeepSeek

| Métrique | Valeur |
|----------|--------|
| **Solde restant** | ~$28 (après ~$14 de dépenses) |
| **Tokens IN** | ~4,7M+ (14 derniers jours) |
| **Tokens OUT** | ~1,8M+ |
| **Coût estimé par jour** | ~$1,00-$1,50 (DeepSeek Flash) |
| **Coût des crons** | ~$0 (99% no_agent/Ollama) |

---

## Points d'attention (audit 19/06/2026)

| # | Alerte | Recommandation |
|---|--------|----------------|
| 1 | ⚠️ **Tailscale DNS** | Problème de résolution DNS signalé — vérifier connectivité |
| 2 | ⚠️ **GPU inutilisé** | RTX 3050 idle en permanence — aucun processus ML ne l'exploite |
| 3 | ⚠️ **npm vulns** | 5 critiques (whatsapp-bridge), 2 high (web/ui-tui) |
| 4 | ⚠️ **Clé SSH obsolète** | `hermes_leo` ne fonctionne plus — accès via mot de passe seulement |
| 5 | ⚠️ **Swap à 32%** | 2,6/8,0 GiB utilisé |
| 6 | ⚠️ **Auth providers** | Codex, Gemini, MiniMax, xAI non configurés — limitations potentielles |

---

*Document généré par LEO — 19/06/2026 | Source : Audit complet environnement LEO*

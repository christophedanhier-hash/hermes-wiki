---
archive: true
archived_date: 2026-07-03
reason: "Contient des informations obsolètes (pré-crash 30/06). Consultez le guide v3.2 pour les données à jour."
statut: archive
---

> ⚠️ **Document archivé le 03/07/2026** — ce document date d'avant la reconstruction post-crash. Les chiffres (crons, machines, GPU, skills) ne reflètent plus la réalité.  
> 📖 Référence à jour : [Guide Hermès pour les Nuls v3.2](https://christophedanhier-hash.github.io/BAVI_LEO/wiki/agent-pro/bureau-leo/guide-hermes-complet/)


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
| **CPU** | Processeur Intel moderne |
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
| **n8n** | n8nio/n8n | 🟢 Running | — | 5678 → host (network=host) |

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
| **default** | `deepseek-v4-flash` | DeepSeek | Telegram LEO | Conversations, analyses, maintenance |
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
| **H:10** | leo-dashboard | Dashboard KPI Hermes |
| **H:15** | leo-dashboard | Dashboard 3 machines |
| **H:20** | leo-dashboard | Monitoring de tous les crons |
| **H:25** | leo-dashboard | Activité GitHub (20 repos) |
| **H:30** | wiki-sync | Synchronisation sources → Wiki MkDocs |
| **H:35** | wiki-oca-sync | Sync documentation T600 |
| **H:36** | t600-drive-sync | Sync Drive → T600 |
| **Every 60m** | leo-dashboard | Dashboard BAVI LEO |
| **18:00** | drive-sync | Sync bidirectionnelle Drive ↔ GitHub |
|| **Every 30m** | Classifieur emails Christophe | Classification Gmail christophe.danhier@gmail.com via Ollama |
|| ** */15** | n8n-healthcheck | Vérification santé n8n (no_agent) |

---

## Dashboards — 6 (+ 1 hub)

| Dashboard | URL | Cron | Technologie |
|-----------|-----|------|-------------|
| **Hub Monitoring** | [localhost:8080](http://localhost:8080) | Statique | HTML + CSS |
| **LEO KPI** | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) | H:10 | HTML + Chart.js |
| **Machines** | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) | H:15 | HTML + Chart.js |
| **Crons** | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) | H:20 | HTML + CSS pur |
| **GitHub** | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) | H:25 | HTML + CSS pur |
| **BAVI LEO** | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) | Every 60m | HTML + Chart.js |
| **n8n** | [http://100.92.102.28:5678](http://100.92.102.28:5678) | */15 | Healthcheck (cron) |

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
| **5678** | **n8n** | **Tailscale** |
| 49417 | Tailscale IPv6 | tailscale0 |

---

## GitHub — 30 repos

| Type | Nb | Exemples |
|------|:--:|----------|
| **Wikis** | 4 | hermes-wiki, BAVI_LEO, wiki-oca, voyages-wiki |
| |**Dashboards** | 6 | leo-dashboard, leo-dashboard, leo-dashboard, leo-dashboard, leo-dashboard, **n8n (interface Web)** |
| |**Automation** | 1 | n8n — workflow LEO Ping (GET /webhook/ping) |
| **Drive** | 1 | hermes-christophe |
| **Guides** | 1 | hermes-guide |
| **Autres publics** | 2 | dashboard-kpi, machine-metrics |
| **Privés / forks** | ~17 | (divers) |

**GitHub Actions :** 9 workflows, tous ✅ success.
**Token scopes :** admin:org, repo, workflow, write:packages.

---

## ⚙️ n8n — Automatisation low-code

n8n est le moteur d'automatisation visuelle de LEO. Déployé en Docker `--network host`, accessible uniquement via Tailscale.

| Propriété | Valeur |
|-----------|--------|
| **Version** | v2.26.8 |
| **Conteneur** | `docker.n8n.io/n8nio/n8n:latest` |
| **Port** | 5678 (host, --network host) |
| **Volume** | `n8n_data` |
| **Accès** | [http://100.92.102.28:5678](http://100.92.102.28:5678) |
| **Owner** | leodanhier@proton.me |
| **API Key** | Hermes Agent (workflow:create/read/update/list) |
| **Credential Ollama** | `Hermes Agent - Ollama LEO` — `http://100.92.102.28:11434` (modèle `qwen2.5:7b`) |
| **Compteur** | Login via API REST (POST /rest/login) |

### Workflow principal : LEO Ping

```
GET /webhook/ping → {"response": "pong"}
```

Workflow minimal de test — utilisé comme healthcheck par le monitoring (cron `n8n-healthcheck`).

### Architecture API

| Méthode | Endpoint | Usage |
|---------|----------|-------|
| POST | /rest/login | Authentification → cookie `n8n-auth` |
| GET | /rest/workflows | Lister les workflows |
| POST | /rest/workflows | Créer un workflow |
| POST | /rest/workflows/:id/activate | Activer un workflow |
| POST | /rest/workflows/:id/deactivate | Désactiver un workflow |
| GET | /webhook/:path | Déclencher un workflow webhook |

### Classifieur Gmail — Python + Ollama (cron Hermes)

Classifieur intelligent des emails Gmail via Ollama (qwen2.5:7b). Remplace l'ancien workflow n8n (désactivé pour instabilité).

| Propriété | Valeur |
|-----------|--------|
| **Type** | Script Python + cron Hermes |
| **Fréquence** | Toutes les 30 min |
| **Modèle** | qwen2.5:7b via Ollama (RTX 3050, gratuit) |
| **Cible** | christophe.danhier@gmail.com |
| **Script** | `/opt/data/classifier_christophe.py` |
| **Labels** | 10 labels Gmail (VIP, Admin, Finances, IA&Tech, Astro, Voyages, Achats, Maison, Famille, Outlook) |
| **Nettoyage** | Archive automatique des emails lus+classifiés > 2 jours |
| **Cron ID** | `067838045e05` — Classifieur emails Christophe |

Le script utilise l'API Gmail directe (pas de credential n8n problématique) + Ollama pour la classification. Plus fiable et plus simple que le workflow n8n abandonné.

### Maintenance

```bash
# Backup du volume n8n
docker run --rm -v n8n_data:/data -v /tmp:/backup alpine tar czf /backup/n8n-$(date +%Y%m%d).tar.gz -C /data .

# Restart
docker restart n8n

# Logs
docker logs n8n --tail 100
```

### Coût

n8n est **gratuit** (self-hosted Docker, license Community Edition). Zéro abonnement, zéro coût API. Seulement le stockage du volume Docker (~50 Mo pour les workflows).

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

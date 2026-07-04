## Architecture Système

### 1. Infrastructure

L'infrastructure de LEO est composée des éléments suivants :

- **Host LEO**: i7-7700K, 22GB RAM
- **Container Debian 13 Python 3.13 DeepSeek V4 Flash**
- **Chromebook Telegram** 
- **Ollama qwen2.5:7b**

### 2. Budget API

Le budget actuel pour les API est d'environ **$19.97** (coût réel constaté). Les seuils d'alerte sont fixés à $30 et le montant minimal avant arrêt des services est de $10. Le routage des requêtes se fait selon la hiérarchie suivante : Ollama → Gemini → DeepSeek.

### 3. Crons Actifs

Les crons sont déployés via **leo-copilot** toutes les heures (`10 * * * *`). La collecte unifiée des données utilise `collect-v2.py` (9 sources : sessions, budget, crons, infra, n8n, github, bavi, services, vaults).

**Changements 04/07/2026 :**
- 🚫 **Auto-Fix Daemon supprimé** (remplacé par le déploiement horaire unifié)
- 🆕 **Deploy Unified Dashboard** → horaire (`10 * * * *`) au lieu de quotidien

### 4. Dashboards

Depuis la reconstruction post-crash (30/06/2026), **un seul dashboard** existe :
- **[leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/)** — dashboard unifié (remplace les 7 dashboards pré-crash)

Les 7 dashboards d'avant (crons, github, machines, wiki, n8n, global, BAVI) ont été consolidés en un seul portail.

### 5. Sessions & Utilisation

- **Total sessions**: 848+
- **Total messages**: 16485+
- **Sessions Telegram**: 11
- **Taille de la base de données**: 117.9 MB
*Document mis à jour le 04/07/2026 — 22:48:00 — Léo 🦁*

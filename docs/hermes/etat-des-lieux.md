# 📋 État des lieux — Installation Hermes de Christophe

> ⚠️ **Document archivé au 07/07/2026** — cette page date du 20/06. Les informations ci-dessous sont obsolètes (crash du 30/06, reconstruction). Consultez [le guide complet v3.2](https://christophedanhier-hash.github.io/BAVI_LEO/wiki/agent-pro/bureau-leo/guide-hermes-complet/) pour les données à jour.
>
> **Mise à jour 07/07/2026** : les principaux changements post-reconstruction sont :
> - **Dashboards** : 7 pré-crash → **1 seul** (leo-dashboard), puis 5 dashboards depuis la reconstruction
> - **Collecteur** : `collect-v2.py` (9 sources unifiées : sessions, budget, crons, infra, github, bavi, services, vaults) — n8n retiré
> - **Déploiement** : toutes les heures (`10 * * * *`) via leo-copilot
> - **n8n** : ❌ Retiré le 13/07/2026. Les 3 workflows ont été migrés vers des crons Hermes.
> - **Crons** : Auto-Fix Daemon supprimé, Deploy Unified Dashboard horaire. 41 crons (tous actifs).
> - **Budget** : coût réel ~$19.97 (vs $28 estimé ci-dessous)

## Configuration actuelle (03/07/2026)

| Élément | Valeur |
|---------|--------|
| **Version Hermes** | v0.18.2 |
| **Python** | 3.14.4 |
| **OS Hôte** | Ubuntu 26.04 LTS |
| **Kernel** | Linux 7.x |
| **CPU** | Processeur Intel récent (multi-cœurs) |
| **RAM** | Mémoire suffisante |
| **GPU** | NVIDIA GeForce RTX 3050 (8 Go) |
| **Stockage** | 457 Go SSD système + 1 To HDD backups |
| **Docker** | 2 conteneurs (hermes-agent + ollama) |
| **Profils actifs** | 8 (default, leo-copilot, michel, bavi-leo, emile, bureau-robert, robert, sylvia) |
| **Gateways** | 5 actifs (s6 supervision) |
| **Modèle principal** | `deepseek-v4-flash` (provider DeepSeek) |
| **Fallback** | deepseek-v4-flash → gemini-3.5-flash → qwen2.5:7b (Ollama local) |
| **Crons actifs** | 41 (tous actifs — tous consolidés dans leo-copilot) |
| **Skills installés** | 126 |
| **n8n** | ❌ Retiré le 13/07/2026 |

> 🔄 Ce document est historiquement la première page de référence. Les données sont désormais maintenues dans le [Guide Hermès pour les Nuls](https://christophedanhier-hash.github.io/BAVI_LEO/wiki/agent-pro/bureau-leo/guide-hermes-complet/) et visibles en temps réel sur le [LEO Dashboard](http://localhost:8765/dashboard).

## 🏠 Provider local (Ollama)

| Champ | Valeur |
|-------|--------|
| **URL** | `http://100.92.102.28:11434/v1` |
| **Modèle** | `qwen2.5:7b` (4.7 GB) |
| **Usage** | Tâches gratuites, docs-update |
| **Conteneur** | Docker, up depuis 6 jours |

## 🛠️ Toolsets activés (16 / 22)

| Tool | Statut |
|------|:------:|
| 🔍 Web Search & Scraping | ✅ |
| 🌐 Browser Automation | ✅ |
| 💻 Terminal & Processes | ✅ |
| 📁 File Operations | ✅ |
| ⚡ Code Execution | ✅ |
| 👁️ Vision / Image Analysis | ⚠️ Non configuré |
| 🎨 Image Generation | ⚠️ Non configuré |
| 🔊 Text-to-Speech | ✅ |
| 📚 Skills | ✅ |
| 📋 Task Planning | ✅ |
| 💾 Memory | ✅ |
| 🔎 Session Search | ✅ |
| ❓ Clarifying Questions | ✅ |
| 👥 Task Delegation | ✅ |
| ⏰ Cron Jobs | ✅ |
| 📨 Cross-Platform Messaging | ✅ |
| 🎵 Spotify | ✅ (connecté 21/06/2026 — OAuth PKCE, Pixel 8 Pro + Web Player) |
| 📋 Tracker GitHub | ✅ [leo-tracker](https://github.com/christophedanhier-hash/leo-tracker/issues/4) — Kanban Project V2, 8 issues ([détails enrichis](https://github.com/christophedanhier-hash/leo-tracker/issues/4)) |

**Désactivés :** 🖱️ Computer Use (macOS — inapplicable sur Linux), 🎬 Video Analysis, 🎬 Video Generation, 🐦 X (Twitter), 🧠 MoA, 🧩 Context Engine, 🏠 Home Assistant, 🤖 Yuanbao

## 📚 Skills installées (105)

### Autonomous AI Agents
- `claude-code`, `codex`, `hermes-agent`, `hermes-gateway`, `hermes-profiles-gateways`, `hermes-workspace`, `opencode`

### BAVI LEO
- `assurance-obligatoire`, `bavi-leo-governance`, `bureau-gerard`, `bureau-michel`, `bureau-robert`, `bureau-sophie`, `bureau-sylvie`, `bureau-versioning`

### Creative
- `architecture-diagram`, `ascii-art`, `ascii-video`, `baoyu-infographic`, `claude-design`, `comfyui`, `design-md`, `excalidraw`, `humanizer`, `manim-video`, `p5js`, `popular-web-designs`, `pretext`, `sketch`, `songwriting-and-ai-music`, `touchdesigner-mcp`

### Data Science
- `jupyter-live-kernel`

### Dogfood
- `dogfood`

### Email
- `gmail-inbox-zero`, `himalaya`, `leo-email-assistant`

### GitHub
- `codebase-inspection`, `github-auth`, `github-code-review`, `github-issues`, `github-pr-workflow`, `github-repo-management`

### Infrastructure
- `bavi-leo-bot-deployment`, `dashboard-deployment`, `dashboard-kpi`, `deepseek-pro`, `drive-github-mirror`, `gdrive-source-of-truth`, `leo-architecture`, `leo-backup-dr`, `machine-metrics`, `remote-server-ssh`, `routage-llm`, `self-hosted-services`, `shared-bot-deployment`, `system-management`

### Media
- `gif-search`, `heartmula`, `songsee`, `youtube-content`

### MLOps
- `audiocraft-audio-generation`, `evaluating-llms-harness`, `huggingface-hub`, `llama-cpp`, `ollama`, `segment-anything-model`, `serving-llms-vllm`, `weights-and-biases`

### Note-taking
- `obsidian`

### Productivity
- `agent-pro`, `airtable`, `budget-tracking`, `google-workspace`, `hermes-dashboard`, `living-documentation`, `maps`, `mkdocs-wiki`, `nano-pdf`, `notion`, `ocr-and-documents`, `powerpoint`, `roadbook-template`, `sequential-execution`, `teams-meeting-pipeline`, `voyages-wiki`

### Research
- `ai-tech-watch`, `arxiv`, `blogwatcher`, `llm-wiki`, `polymarket`, `research-paper-writing`

### Smart Home
- `openhue`

### Social Media
- `xurl`

### Software Development
- `bureau-gerard` (ancien, doublon BAVI), `hermes-agent-skill-authoring`, `node-inspect-debugger`, `plan`, `python-debugpy`, `requesting-code-review`, `simplify-code`, `spike`, `systematic-debugging`, `test-driven-development`

## ⏱️ Crons LEO

<!-- AUTO:START crons -->
<!-- AUTO:START crons -->
> **Dernière synchro : 17/07/2026**
> **39 crons Hermes** (tous consolidés dans `leo-copilot`) → **41 jobs (tous actifs)**

| Profil | Crons |
|--------|:-----:|
| `leo-copilot` (consolidateur) | 41 |
| `default` | 0 |
| `bavi-leo` | 0 |
| `emile` | 0 |
| `bureau-robert` | 0 |

**0 crons hôte** (tout est dans les profils Hermes)

**Total général : 41 jobs (tous actifs)**

📖 Détail complet : [BAVI_LEO / wiki / crons](https://christophedanhier-hash.github.io/BAVI_LEO/wiki/crons/)
<!-- AUTO:END crons -->
<!-- AUTO:END crons -->
<!-- AUTO:END crons -->

## 📧 Gestion email

<!-- AUTO:START gmail -->
| Système | Description |
|---------|-------------|
| **Veille IA** | Scan 11 sources + Le Monde IA → rapport HTML formaté → email à Christophe + John + Steve |
|| **Classifieur emails** | Script Python (`classifier_christophe.py`) + Ollama (qwen2.5:7b) — classification par IA de la boîte christophe.danhier@gmail.com. Cron Hermes toutes les 30 min. Nettoyage automatique : archive les emails lus+classifiés > 2j. |
|| **Labels** | 📁Admin(108) 📁Finances(109) 📁IA&Tech(110) 📁Astro(111) 📁Voyages(112) 📁Famille(113) 📁Achats(114) 📁Maison(115) ⭐VIP(105) 📨Outlook(103) |
| **Expéditeur** | leodanhieria@gmail.com uniquement, Christophe TOUJOURS en CC |
| **Mapping** | 19 entrées — auto-apprenant, zéro coût après premier run |
<!-- AUTO:END gmail -->

## 🔌 Plateformes connectées

| Plateforme | Statut |
|-----------|:------:|
| **Telegram** | ✅ Configuré (gateway LEO + bot voyages) |
| **Discord** | ❌ Non configuré |
| **Slack** | ❌ Non configuré |

## 📊 Dashboards

<!-- AUTO:START dashboards -->
> **Dernière synchro : 07/07/2026**
> **1 dashboard unifié : leo-dashboard**
<!-- AUTO:END dashboards -->

## 🧠 BAVI Knowledge Hub — Agent Pro

Portail de visualisation des documents produits par les bureaux BAVI LEO : [Agent Pro](https://christophedanhier-hash.github.io/BAVI_LEO/wiki/agent-pro/)

| Métrique | Valeur |
|:---------|:-------|
| **Bureaux actifs** | 5 (Gérard, Robert, Sophie, Michel, Sylvie) |
| **Analyses totales** | 5 (3 Gérard T600 + 2 Michel infra) |
| **Versioning** | ✅ v1 → vN (frontmatter + section Versions) |
| **Template** | `analyse-template.md` avec `version:` + statut |
| **Architecture** | Source unique `hermes-christophe/BAVI/` ↔ Drive (cron 18h) — plus de triplication |
| **Index auto** | `agent-pro-index.py` (sync docs + génération tables) |
| **Guide** | [📖 Guide utilisation](https://christophedanhier-hash.github.io/BAVI_LEO/guide-utilisation/) |
| **Skill** | `bureau-versioning` — workflow itération analyses |

## 💰 Budget DeepSeek

- **Solde restant estimé :** ~$19.97
- **Tokens consommés (14j) :** ~4,7M+ IN / ~1,8M+ OUT
- **Sessions :** 90 (62 Telegram, 3 CLI)
- **Messages :** 4 651
- **État DB :** 79,1 Mo

## 🔀 Règles de routage LLM

Hiérarchie d'arbitrage pour chaque tâche :

``` mermaid
flowchart TD
    Tache["Tâche à exécuter"]
    Script["Est-ce un script pur ?"]
    LLM["A besoin d'un LLM ?"]
    Ollama["Ollama 🏠 suffit ?"]
    Gemini["Résultat insuffisant ?"]
    DeepSeek["Toujours insuffisant / critique ?"]
    NoAgent["→ no_agent (0 token)"]
    OllamaOK["→ Ollama (gratuit)"]
    GeminiOK["→ Gemini ⚡ (quasi gratuit)"]
    DeepSeekOK["→ DeepSeek 🤖 (payant)"]

    Tache --> Script
    Tache --> LLM
    Script --> NoAgent
    LLM --> Ollama
    Ollama -- Oui --> OllamaOK
    Ollama -- Non --> Gemini
    Gemini -- Oui --> GeminiOK
    Gemini -- Non --> DeepSeek
    DeepSeek --> DeepSeekOK

    style Tache fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style Script fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style LLM fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style Ollama fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style Gemini fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style DeepSeek fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style NoAgent fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style OllamaOK fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style GeminiOK fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style DeepSeekOK fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    linkStyle default stroke-width:2px,fill:none
```

| Provider | Utilisation |
|----------|-------------|
| **DeepSeek 🤖** | Toute conversation Telegram, raisonnement, qualité premium |
| **Ollama 🏠** | Traitement local, batch, données privées, tâches gratuites |
| **Gemini ⚡** | Fallback automatique si DeepSeek indisponible |

## 🔴 Règles de vie critiques

### Infra
- **5 profils** (`default`, `leo-copilot`, `bavi-leo`, `emile`, `bureau-robert`)
- **NE JAMAIS** arrêter/redémarrer le gateway sans accord explicite

### Email
- **TOUJOURS** envoyer depuis `leodanhieria@gmail.com` (compte LEO)
- **JAMAIS** depuis `christophe.danhier@gmail.com`
- **Christophe TOUJOURS en CC** sur chaque email
- **1 seul envoi max** — si échec, STOP. Ne pas réessayer.

### Communication
- **Authenticité > Politesse** — pas de formules vides
- **Stop = STOP** — ne pas continuer ni proposer d'alternative
- **1 seule URL OAuth** par session (la première)

## ✅ Bonnes pratiques

### Choix du mode d'exécution

| Type de tâche | Mode |
|---------------|------|
| Script pur (collecte, backup) | **no_agent=True** (0 token LLM) |
| Réflexion simple (résumé léger) | Ollama 🏠 |
| Tâche complexe (analyse, rapport) | DeepSeek 🤖 |
| Fallback si Ollama défaillant | Gemini ⚡ puis DeepSeek 🤖 |

### Réflexe nouveau cron

1. Forcer màj monitoring leo-dashboard
2. Mettre à jour le guide Hermes
3. Sauvegarder dans les skills concernés

### Conventions scripts

- Tous les exécutables dans `~/.hermes/profiles/leo-copilot/scripts/`
- Pattern wrapper shell → `/opt/hermes/.venv/bin/python3 <script.py>`
- Crons no_agent = wrapper shell impératif (pas de .py direct)

### Vérification systématique

Tester le résultat avant de livrer :
1. Exécuter l'action
2. Vérifier le résultat (URL accessible ? Email reçu ?)
3. Si échec → signaler immédiatement

## 🛡️ Anti-régression

- **Zéro répétition** — chaque réponse va à l'essentiel
- **1 envoi max** — actions extérieures : une seule tentative
- **Pas de réessai après échec** — signaler et attendre instruction
- **Vérifier les garde-fous** avant toute action destructive
- **Corrections → skills** (procédures durables), pas mémoire (faits temporaires)
- **Utiliser les dates ISO** pour la comparaison, JJ/MM pour l'affichage
- **Dashboard** : toujours comparer les dates en ISO (`%Y-%m-%d`), afficher en `%d/%m`

---
## Leçons apprises

### 12/06/2026 — Trop de profils

**Problème :** Création d'un profil `local` pour Ollama. Arrêt du gateway `local` = perte d'accès Telegram.

**Solution :** Unifier dans un seul profil, Ollama par API directe. Fiabilité > flexibilité.

### 13/06/2026 — Précipitation

**Problème :** Actions sans réflexion préalable = régressions (mauvais token, erreur OAuth, envoi multiple d'email).

**Solution :** Règle #1 : réfléchir avant d'agir. Toujours.

### 14/06/2026 — Crons instables

**Problème :** Crons qui utilisaient le mauvais Python, scripts introuvables, identité Git manquante, push qui échoue.

**Solution :** Uniformisation : wrappers shell + no_agent + identité Git et token dans le script.
*Document mis à jour le 07/07/2026 à 00:00 — Léo 🦁*

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)


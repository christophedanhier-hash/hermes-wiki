# 📚 Catalogue des Skills — BAVI LEO & Hermes

> **Document généré le** : 19/06/2026
> **Source** : Audit complet des 103 skills installés
> **Usage** : Ce document liste et décrit tous les skills disponibles dans l'écosystème LEO.

---

## 🏛️ BAVI LEO — 6 skills (or update list)

Les **Bureaux Agentiques Virtuels** sont le cœur métier de LEO. Chaque bureau est un agent spécialisé avec son propre rôle, ses sous-experts, et son workflow standardisé en 7 phases.

### 1. 🏗️ bavi-leo
| | |
|---|---|
| **Version** | v1.4 |
| **Description** | Framework de gouvernance multi-bureaux — audit, workflow 7 phases, dispatch conditionnel, interopérabilité |
| **Quand l'utiliser** | Créer un nouveau bureau, auditer l'écosystème, optimiser un bureau existant |
| **Dépendances** | Références : audit-matrix, full-system-audit-checklist, pricing-model. Template : pdf-from-markdown |
| **Liens** | [Voir le skill](https://github.com/christophedanhier-hash/hermes-wiki) |

### 2. 🏛️ bureau-robert
| | |
|---|---|
| **Version** | v2.0 |
| **Type** | Orchestrateur Conseil Stratégique IT |
| **Sous-experts** | Architecture, Sécurité, Data, Gouvernance, Vision Stratégique, Projet & Programme, Assurance Obligatoire |
| **Interop** | → Appelle `assurance-obligatoire`, `bureau-sophie` |
| **Quand l'utiliser** | Analyses IT transversales, notes stratégiques, arbitrages pour la direction |

### 3. 💰 bureau-sophie
| | |
|---|---|
| **Version** | v2.0 |
| **Type** | Orchestrateur Pilotage Économique & Financier IT |
| **Sous-experts** | Analyste Marché & Business Case, Modélisateur Financier IT, Risques & Conformité IT |
| **Parallélisation** | Marché + Risques en parallèle |
| **Quand l'utiliser** | Business cases, TCO/ROI, 3 scenarii, analyse de rentabilité |

### 4. 📝 bureau-gerard
| | |
|---|---|
| **Version** | v2.0 |
| **Type** | Orchestrateur Documentation Technique T600 |
| **Sous-experts** | Ethnographe, Astro-optique, Hardware, Firmware, Rédacteur Technique, Formateur |
| **Croisement obligatoire** | Hardware ↔ Firmware quand les deux sont activés |
| **Quand l'utiliser** | Documentation du télescope T600 (Observatoire Centre Ardenne) |
| **Wiki** | [wiki-oca/t600](https://christophedanhier-hash.github.io/wiki-oca/t600/) |

### 5. 🧭 bureau-sylvie
| | |
|---|---|
| **Version** | v2.5 |
| **Type** | Orchestrateur Organisation de Voyages |
| **Sous-experts** | Curateur d'Expériences, Navigateur Camping-Car, Journaliste de Bord |
| **Bot Telegram** | [@bavi_leo_voyages_bot](https://t.me/bavi_leo_voyages_bot) |
| **Quand l'utiliser** | Roadbooks camping-car, planification d'itinéraires, cartes Folium |
| **Règles clés** | Pas de Google Maps, pas de photos dans le wiki, context voyageur obligatoire, distances Haversine, astuces CC (ZTL, hauteur) |

### 6. 🛡️ assurance-obligatoire
| | |
|---|---|
| **Version** | v2.0 |
| **Type** | Expert métier transverse (inter-bureaux) |
| **Domaine** | INAMI, BCSS, eHealth, MyCareNet, Intermutualité |
| **Modes** | Sous-agent de Robert OU skill autonome |
| **Quand l'utiliser** | Analyse IT avec impact métier Assurance Obligatoire |

---

## ⚙️ Skills Hermes Core — 6 skills

Les skills fondamentaux pour configurer, utiliser et étendre Hermes Agent.

| Skill | Description | Usage |
|-------|-------------|-------|
| **hermes-agent** | Référence complète CLI, config, providers, toolsets, gateway, troubleshooting | Quotidien |
| **claude-code** | Délégation de code à Claude Code CLI | Ponctuel |
| **codex** | Délégation de code à OpenAI Codex CLI | Ponctuel |
| **opencode** | Délégation de code à OpenCode CLI | Ponctuel |
| **hermes-profiles-gateways** | Gestion multi-profils et gateways simultanés | Maintenance |
| **hermes-workspace** | Bootstrap d'un workspace Hermes avec intégration Drive | Setup |

---

## 🔧 Infrastructure — 13 skills

Gestion des serveurs, déploiements, sync Drive, routage LLM et sauvegardes.

| Skill | Description | Utilisé par |
|-------|-------------|-------------|
| **deepseek-pro** | Bascule sur DeepSeek Pro (deepseek-v4-pro) pour analyses complexes via delegate_task | Tous profils |
| **dashboard-deployment** | Déploiement dashboards HTML sur GitHub Pages avec collecte horaire 0$ | Crons LEO |
| **dashboard-kpi** | Système dashboard KPI Hermes : SQLite → JSON → HTML (Chart.js) | Cron leo-dashboard |
| **machine-metrics** | Dashboard 3 machines (LEO, Yoga, Penguin) : CPU/RAM/DISK | Cron leo-dashboard |
| **leo-architecture** | Architecture LEO finale : 5 profils, 1+ gateways, DeepSeek + Ollama + Gemini | Setup |
| **leo-backup-dr** | Plan de Reprise d'Activité — backup Drive + restauration ~45min | Cron daily-backup |
| **routage-llm** | Règles de routage : DeepSeek (Telegram) vs Ollama (local) vs Gemini (fallback) | Quotidien |
| **self-hosted-services** | Installation services auto-hébergés — Docker/Tailscale (n8n retiré 13/07/2026) | Maintenance |
| **shared-bot-deployment** | Déploiement bot Telegram secondaire (amis, famille, projet) | Setup |
| **system-management** | Gestion centralisée machines distantes via Tailscale + SSH (multi-OS) | Maintenance |
| **drive-github-mirror** | Miroir versionné Drive ↔ GitHub bidirectionnel | Cron drive-sync |
| **gdrive-source-of-truth** | Workflow Drive source de vérité → GitHub → Wikis → retour calculs vers Drive | Cron drive-sync |
| **bavi-leo-bot-deployment** | Déploiement d'un bureau BAVI LEO comme bot Telegram autonome | Setup |

---

## 📊 Productivité — 16 skills

| Skill | Description | Priorité |
|-------|-------------|:--------:|
| **mkdocs-wiki** | Création de wikis MkDocs Material (pattern BAVI LEO) — 958 lignes | ⭐ Élevée |
| **voyages-wiki** | Wiki voyages BAVI LEO — roadbooks Folium, coûts | ⭐ Élevée |
| **budget-tracking** | Dashboard KPI LEO v6 — suivi solde DeepSeek | ⭐ Élevée |
| **hermes-dashboard** | Dashboard Hermes KPIs : sessions, tokens, gateway | Haute |
| **living-documentation** | Documentation vivante MkDocs + Drive — collecte + génération Ollama | Haute |
| **google-workspace** | Gmail, Calendar, Drive, Docs, Sheets via gws CLI | Haute |
| **maps** | Geocoding, POIs, routes, timezones via OpenStreetMap/OSRM | Moyenne |
| **sequential-execution** | Exécution multi-étapes avec vérification à chaque étape | Moyenne |
| **roadbook-template** | Template complet roadbook wiki Voyages (9 sections) | Moyenne |
| **teams-meeting-pipeline** | Pipeline résumés réunions Teams via Hermes CLI | Faible |
| **airtable** | API Airtable REST : CRUD records, filters, upserts | Faible |
| **notion** | Notion API + ntn CLI : pages, databases, markdown | Faible |
| **ocr-and-documents** | Extraction texte de PDFs/scans (pymupdf, marker-pdf) | Faible |
| **powerpoint** | Création/lecture/édition .pptx | Faible |
| **agent-pro** | Délégation à DeepSeek Pro depuis tout profil | Faible |
| **nano-pdf** | Édition PDF via instructions en langage naturel | Faible |

---

## 🎨 Créatif — 16 skills

| Skill | Description |
|-------|-------------|
| **comfyui** | Génération image/vidéo/audio avec ComfyUI — install, nodes, workflows |
| **claude-design** | Artifacts HTML one-shot (landing, deck, prototype) |
| **humanizer** | Humanisation de texte — suppression des marqueurs IA |
| **excalidraw** | Diagrammes hand-drawn JSON (archi, flow, séquence) |
| **architecture-diagram** | Diagrammes SVG dark theme pour architecture cloud/infra |
| **popular-web-designs** | 54 design systems réels (Stripe, Linear, Vercel) |
| **p5js** | Sketches p5.js : art génératif, shaders, 3D |
| **sketch** | Maquettes HTML jetables — 2-3 variantes |
| **ascii-art** | ASCII art : pyfiglet, cowsay, boxes |
| **ascii-video** | Vidéo/audio → ASCII colorisé MP4/GIF |
| **baoyu-infographic** | Infographies : 21 layouts × 21 styles |
| **design-md** | Authoring/validation DESIGN.md (Google token spec) |
| **manim-video** | Animations Manim CE (3Blue1Brown style) |
| **pretext** | Layout texte sans DOM — art ASCII typographique |
| **songwriting-and-ai-music** | Écriture de chansons + prompts Suno AI |
| **touchdesigner-mcp** | Contrôle TouchDesigner via MCP — 36 outils natifs |

---

## 🔬 Research — 6 skills

| Skill | Description | Statut |
|-------|-------------|:------:|
| **ai-tech-watch** | Veille IA quotidienne (11 sources RSS → email à 8h) | ✅ **Actif** (cron) |
| **arxiv** | Recherche d'articles arXiv par mot-clé, auteur, catégorie |
| **blogwatcher** | Monitoring de blogs/flux RSS |
| **llm-wiki** | Base de connaissances LLM interconnectée (Karpathy style) |
| **polymarket** | Consultation Polymarket : marchés, prix, historiques |
| **research-paper-writing** | Rédaction de papiers ML (NeurIPS/ICML/ICLR) — 2377 lignes |

---

## 💻 Software Development — 8 skills

| Skill | Description |
|-------|-------------|
| **plan** | Mode plan : fichier markdown dans .hermes/plans/ — pas d'exécution |
| **systematic-debugging** | Debug en 4 phases : comprendre avant de corriger |
| **test-driven-development** | TDD strict : RED → GREEN → REFACTOR |
| **spike** | Expériences jetables pour valider une idée |
| **requesting-code-review** | Revue pré-commit : sécurité, qualité, auto-fix |
| **hermes-agent-skill-authoring** | Authoring SKILL.md in-repo : frontmatter, validator |
| **python-debugpy** | Debug Python : pdb + debugpy remote (DAP) |
| **node-inspect-debugger** | Debug Node.js via --inspect + Chrome DevTools |

---

## 🤖 MLOps — 8 skills

| Skill | Description |
|-------|-------------|
| **weights-and-biases** | Logging ML experiments, sweeps, model registry |
| **evaluating-llms-harness** | Benchmark LLMs (MMLU, GSM8K, etc.) via lm-eval-harness |
| **llama-cpp** | Inférence GGUF locale + découverte modèles HF Hub |
| **serving-llms-vllm** | Serving haute performance vLLM (API OpenAI, quantization) |
| **ollama** | Déploiement et intégration Ollama avec Hermes (Docker GPU) |
| **huggingface-hub** | CLI HuggingFace : recherche/download/upload modèles |
| **audiocraft-audio-generation** | AudioCraft : MusicGen text-to-music, AudioGen text-to-sound |
| **segment-anything-model** | Segmentation d'images SAM (points, boxes, masks) |

---

## 🐙 GitHub — 6 skills

| Skill | Description |
|-------|-------------|
| **github-pr-workflow** | Cycle de vie PR GitHub : branch, commit, open, CI, merge |
| **github-code-review** | Revue de code : diffs, commentaires inline |
| **github-repo-management** | Clone/création/fork de repos, gestion remotes |
| **github-issues** | Création/triage/label/assignation d'issues |
| **github-auth** | Setup auth GitHub : tokens HTTPS, clés SSH, gh CLI |
| **codebase-inspection** | Inspection de codebase avec pygount (LOC, langages) |

---

## 📧 Email — 3 skills

| Skill | Description | Statut |
|-------|-------------|:------:|
| **leo-email-assistant** | Envoi d'emails via API Gmail OAuth2 — template, règles absolues, anti-régression | ✅ **Actif** |
| **gmail-inbox-zero** | Gestion Inbox Zero : archive, classification, labels | ✅ **Actif** (cron 15min) |
| **himalaya** | Client email IMAP/SMTP terminal (Himalaya CLI) | |

---

## 📱 Media & Social — 5 skills

| Skill | Description |
|-------|-------------|
| **youtube-content** | Transcripitions YouTube → résumés, threads, blogs |
| **heartmula** | Génération de chansons Suno-like (lyrics + tags) |
| **gif-search** | Recherche/Download GIFs via Tenor API |
| **songsee** | Spectrogrammes audio (mel, chroma, MFCC) |
| **xurl** | X/Twitter via CLI : post, search, DM, media |

---

## 🔗 Autres — 4 skills

| Skill | Catégorie | Description |
|-------|-----------|-------------|
| **jupyter-live-kernel** | Data Science | Python itératif via kernel Jupyter live (hamelnb) |
| **obsidian** | Note-taking | Lecture/recherche/création/édition dans le vault Obsidian |
| **openhue** | Smart Home | Contrôle Philips Hue via OpenHue CLI |
| **dogfood** | Dogfood | QA exploratoire d'applications web — bugs, rapports |

---

## 📊 Statistiques globales

| Métrique | Valeur |
|----------|:------:|
| **Total skills** | **126** |
| **Catégories** | 22 |
| **Lignes totales estimées** | ~21 000+ |
| **Lignes moyennes par skill** | ~200 |
| **Plus gros skill** | research-paper-writing (2 377 l.) |
| **Plus petit skill** | gif-search (~50 l.) |
| **Skills actifs quotidiennement** | ~15 (ai-tech-watch, leo-email, budget-check, dashboards, gmail-classifier, etc.) |

### Répartition par catégorie

```
BAVI LEO         ████████░░ 6
Productivité     ████████████████████░░ 16
Créatif          ████████████████████░░ 16
Infrastructure   █████████████████░░ 13
Software Dev     ██████████░░ 8
MLOps            ██████████░░ 8
Hermes Core      ████████░░ 6
Research         ████████░░ 6
GitHub           ████████░░ 6
Media            ██████░░ 4
Email            ████░░ 3
Autres           ██████░░ 4
```

---

## 🔄 Workflow de mise à jour

Les skills sont automatiquement maintenus par le **Curator** Hermes :
- Fréquence : toutes les 168h (1 semaine)
- Skills inactifs > 30 jours → marqués "stale"
- Skills inactifs > 90 jours → archivés
- Les sauvegardes sont conservées (5 dernières)

Pour forcer une mise à jour :
```bash
hermes curator run
```

Pour lister les skills :
```bash
hermes skills list
```

---

*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

> 🤖 Dernier audit : 22 July 2026 à 09:00 (UTC+2)


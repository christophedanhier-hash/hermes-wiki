# 📋 État des lieux — Installation Hermes de Christophe

Page générée le **14/06/2026** — configuration actuelle du serveur **LEO**.

---

## 🖥️ Informations système

| Élément | Valeur |
|---------|--------|
| **Version Hermes** | v0.16.0 (2026.6.5) |
| **Python** | 3.13.5 |
| **OpenAI SDK** | 2.24.0 |
| **Installation** | `/opt/hermes` |
| **Config** | `/opt/data/config.yaml` |
| **Secrets** | `/opt/data/.env` |
| **Profile actif** | `default` |
| **Timezone** | Europe/Brussels |

## 🤖 Modèle principal

| Champ | Valeur |
|-------|--------|
| **Modèle** | `deepseek-v4-flash` |
| **Provider** | DeepSeek (`api.deepseek.com`) |
| **Turns max** | 60 |
| **Gateway** | 🟢 Actif (PID 26649) |

## ⚡ Fallback

```yaml
fallback_providers:
  - provider: google
    model: gemini-2.0-flash-001
```

## 🏠 Provider local (Ollama)

| Champ | Valeur |
|-------|--------|
| **URL** | `http://100.92.102.28:11434/v1` |
| **Modèle** | `qwen2.5:7b` (4.7 GB) |
| **Usage** | Tâches gratuites, docs-update |

## 🛠️ Toolsets activés (16 / 22)

| Tool | Statut |
|------|:------:|
| 🔍 Web Search & Scraping | ✅ |
| 🌐 Browser Automation | ✅ |
| 💻 Terminal & Processes | ✅ |
| 📁 File Operations | ✅ |
| ⚡ Code Execution | ✅ |
| 👁️ Vision / Image Analysis | ✅ |
| 🎨 Image Generation | ✅ |
| 🔊 Text-to-Speech | ✅ |
| 📚 Skills | ✅ |
| 📋 Task Planning | ✅ |
| 💾 Memory | ✅ |
| 🔎 Session Search | ✅ |
| ❓ Clarifying Questions | ✅ |
| 👥 Task Delegation | ✅ |
| ⏰ Cron Jobs | ✅ |
| 📨 Cross-Platform Messaging | ✅ |
| 🖱️ Computer Use (macOS) | ✅ |

**Désactivés :** 🎬 Video Analysis, 🎬 Video Generation, 🐦 X (Twitter), 🧠 MoA, 🧩 Context Engine, 🏠 Home Assistant, 🎵 Spotify, 🤖 Yuanbao

## 📚 Skills installées (93)

### Autonomous AI Agents
- `claude-code`, `codex`, `hermes-agent`, `hermes-profiles-gateways`, `hermes-workspace`, `opencode`

### Creative
- `architecture-diagram`, `ascii-art`, `ascii-video`, `baoyu-infographic`, `claude-design`, `comfyui`, `design-md`, `excalidraw`, `humanizer`, `manim-video`, `p5js`, `popular-web-designs`, `pretext`, `sketch`, `songwriting-and-ai-music`, `touchdesigner-mcp`

### Data Science
- `jupyter-live-kernel`

### Dogfood
- `dogfood`

### Email
- `himalaya`

### GitHub
- `codebase-inspection`, `github-auth`, `github-code-review`, `github-issues`, `github-pr-workflow`, `github-repo-management`

### Infrastructure
- `dashboard-deployment`, `dashboard-kpi`, `leo-architecture`, `machine-metrics`, `remote-server-ssh`, `routage-llm`, `system-management`

### Media
- `gif-search`, `heartmula`, `songsee`, `youtube-content`

### MLOps
- `huggingface-hub`, `evaluating-llms-harness`, `weights-and-biases`, `llama-cpp`, `serving-llms-vllm`, `audiocraft-audio-generation`, `segment-anything-model`

### Note-taking
- `obsidian`

### Productivity
- `airtable`, `budget-tracking`, `google-workspace`, `hermes-dashboard`, `living-documentation`, `maps`, `nano-pdf`, `notion`, `ocr-and-documents`, `powerpoint`, `sequential-execution`, `teams-meeting-pipeline`

### Research
- `arxiv`, `blogwatcher`, `llm-wiki`, `polymarket`

### Smart Home
- `openhue`

### Social Media
- `xurl`

### Software Development
- `bureau-gerard`, `hermes-agent-skill-authoring`, `node-inspect-debugger`, `plan`, `python-debugpy`, `requesting-code-review`, `simplify-code`, `spike`, `systematic-debugging`, `test-driven-development`

### Autres
- `orchestrateur-gerard`, `yuanbao`

## ⏰ Crons programmés (11)

| Cron | Horaire | Type | Statut |
|------|---------|------|:------:|
| **daily-backup** | 06:00 quotidien | 🔧 Script | ✅ |
| **docs-update** | Lun 08:00 hebdo | 🧠 Ollama | ⚠️ |
| **machines-kpi** | H:00 chaque heure | 🔧 Script | ✅ |
| **budget-check-v6** | H:05 chaque heure | 🔧 Script | ✅ |
| **dashboard-deploy** | H:10 chaque heure | 🔧 Script | ✅ |
| **leo-metrics** | H:15 chaque heure | 🔧 Script | ✅ |
| **crons-dashboard** | H:20 chaque heure | 🔧 Script | ✅ |
| **drive-sync** | 18:00 quotidien | 🔧 Script | ✅ |
| **github-dashboard** | H:25 chaque heure | 🔧 Script | ✅ |
| **wiki-sync** | H:30 chaque heure | 🔧 Script | ✅ |
| **wiki-oca-sync** | H:35 chaque heure | 🔧 Script | ✅ |

Tous les crons livrent en **local** (fichiers, pas Telegram).

## 🔌 Plateformes connectées

| Plateforme | Statut |
|-----------|:------:|
| **Telegram** | ✅ Configuré |
| **Discord** | ❌ Non configuré |
| **Slack** | ❌ Non configuré |

## 📊 Dashboards

| Dashboard | URL |
|-----------|-----|
| **LEO KPI** | [dashboard-leo](https://christophedanhier-hash.github.io/dashboard-leo/) |
| **Machines** | [leo-metrics](https://christophedanhier-hash.github.io/leo-metrics/) |
| **Crons** | [crons-dashboard](https://christophedanhier-hash.github.io/crons-dashboard/) |
| **GitHub** | [github-dashboard](https://christophedanhier-hash.github.io/github-dashboard/) |

## 💰 Budget DeepSeek

- **Balance actuelle :** ~$40.39
- **Tokens consommés :** ~3,9M IN / 1,5M OUT
- **Sessions :** 41

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
- **NE JAMAIS** créer un second profil — tout dans `default`
- **NE JAMAIS** arrêter/redémarrer le gateway sans accord explicite
- **1 seul gateway**, 1 seul profil, 3 providers disponibles

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

1. Forcer màj monitoring crons-dashboard
2. Mettre à jour le guide Hermes
3. Sauvegarder dans les skills concernés

### Conventions scripts

- Tous les exécutables dans `/opt/data/scripts/`
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

# 🏗️ Architecture de Communication — Écosystème LEO

> **3 profils Hermes, 3 gateways Telegram, 1 mémoire unifiée. 100% DeepSeek.**

---

## Les 3 entités

```mermaid
flowchart TD
    User["👤 Christophe<br/>━━━━━━━━━━"]

    subgraph LEO_MAIN["🦁 LEO — Agent Hermes Principal"]
        direction LR
        Agent["🤖 Hermes Agent<br/>Profil: default"]
        DS_Flash["⚡ DeepSeek Flash<br/>Dialogue quotidien"]
        DS_Pro_Sub["🧠 DeepSeek Pro<br/>Sous-agents"]
    end

    subgraph LEO_COP["🔧 Leo Copilot — Infrastructure"]
        direction LR
        Agent2["🤖 Hermes Agent<br/>Profil: leo-copilot"]
        DS_Pro["🧠 DeepSeek Pro<br/>Code · Infra · n8n"]
    end

    subgraph BAVI["🧭 BAVI LEO — Voyages"]
        direction LR
        Agent3["🤖 Hermes Agent<br/>Profil: bavi-leo"]
        DS_Flash2["⚡ DeepSeek Flash<br/>Roadbooks"]
    end

    MEM["📁 Mémoire Partagée<br/>sync-memory.py · 30min"]

    User -->|"DM Telegram"| LEO_MAIN
    User -->|"@hermes_leo_copilot_bot"| LEO_COP
    User -->|"@bavi_leo_voyages_bot"| BAVI

    LEO_MAIN -.-> MEM
    LEO_COP -.-> MEM
    BAVI -.-> MEM

    Agent --> DS_Flash
    Agent -.->|"délégation"| DS_Pro_Sub

    Agent2 --> DS_Pro

    Agent3 --> DS_Flash2

    style User fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    style LEO_MAIN fill:#e3f2fd,stroke:#1976d2,stroke-width:3px,color:#0d47a1
    style Agent fill:#bbdefb,stroke:#1976d2,color:#0d47a1
    style DS_Flash fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20
    style DS_Pro_Sub fill:#fce4ec,stroke:#c62828,color:#b71c1c
    style LEO_COP fill:#ede7f6,stroke:#5e35b1,stroke-width:3px,color:#311b92
    style Agent2 fill:#d1c4e9,stroke:#5e35b1,color:#311b92
    style DS_Pro fill:#fce4ec,stroke:#c62828,color:#b71c1c
    style BAVI fill:#e8f5e9,stroke:#388e3c,stroke-width:3px,color:#1b5e20
    style Agent3 fill:#c8e6c9,stroke:#388e3c,color:#1b5e20
    style DS_Flash2 fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20
    style MEM fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
```

---

## 1. 🦁 LEO — L'Agent Hermes Principal

**LEO** est l'agent **Hermes Agent** — ton majordome IA. Pas de handle Telegram : tu lui parles en DM, le gateway fait le pont.

```mermaid
flowchart TB
    subgraph SERVEUR["🖥️ LEO — Profil default"]
        direction TB
        Gateway["🌐 Gateway DeepSeek<br/>DM Telegram → Agent"]
        Hermes["🦁 Hermes Agent<br/>DeepSeek Flash"]
        SubAgent["🧠 Sous-agents<br/>DeepSeek Pro<br/>(tâches complexes)"]
        Ollama["🏠 Ollama<br/>qwen2.5:7b<br/>(tâches locales gratuites)"]

        Gateway <--> Hermes
        Hermes -.->|"délégation auto"| SubAgent
        Hermes -.->|"API directe"| Ollama
    end

    TG["📱 Telegram<br/>DM @tofdan"]

    TG --> Gateway
    Gateway --> TG

    style SERVEUR fill:#e3f2fd,stroke:#1976d2,stroke-width:3px,color:#0d47a1
    style Hermes fill:#bbdefb,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style Gateway fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style SubAgent fill:#fce4ec,stroke:#c62828,stroke-width:2px,color:#b71c1c
    style Ollama fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style TG fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
```

### Comment ça marche

1. **Tu parles à LEO via Telegram** — le Gateway DeepSeek fait le pont
2. **LEO n'a pas de handle** — réponse en DM direct
3. **Tâches complexes** → sous-agents DeepSeek Pro automatiquement
4. **Tâches locales** → Ollama (gratuit, classification, parsing)

---

## 2. 🔧 @hermes_leo_copilot_bot — Infrastructure

Bot spécialisé **infrastructure** (n8n, serveurs, déploiements, watchdogs, dashboards). Propulsé par **DeepSeek Pro**.

```mermaid
flowchart TB
    subgraph COPILOT["🔧 Profil leo-copilot"]
        direction TB
        P1["📋 Profil: leo-copilot"]
        B1["📱 @hermes_leo_copilot_bot"]
        M1["🧠 DeepSeek Pro<br/>(deepseek-v4-pro)"]
        F1["⚡ Fallback DeepSeek Flash"]
        SKILLS["📚 Skills<br/>n8n · dashboards · drive<br/>watchdogs · budget"]
    end

    subgraph EXTERNE["🌐 Services gérés"]
        N8N["🔧 n8n :5678"]
        DASH["📊 7 Dashboards<br/>GitHub Pages"]
        CRONS["⏰ 30 Crons Hermes"]
        GH["🐙 GitHub<br/>5 repos"]
    end

    MEM["📁 Sync mémoire<br/>avec default + bavi-leo<br/>toutes les 30min"]

    B1 --> M1
    B1 -.->|"si Pro down"| F1
    B1 --> SKILLS
    MEM -.-> P1

    SKILLS --> N8N
    SKILLS --> DASH
    SKILLS --> CRONS
    SKILLS --> GH

    style COPILOT fill:#ede7f6,stroke:#5e35b1,stroke-width:3px,color:#311b92
    style P1 fill:#d1c4e9,stroke:#5e35b1,stroke-width:2px,color:#311b92
    style B1 fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    style M1 fill:#fce4ec,stroke:#c62828,stroke-width:2px,color:#b71c1c
    style F1 fill:#fff3e0,stroke:#e65100,stroke-width:2px,stroke-dasharray:5,color:#bf360c
    style SKILLS fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style MEM fill:#fce4ec,stroke:#c62828,color:#b71c1c
    style N8N fill:#e8eaf6,stroke:#3949ab,color:#1a237e
    style DASH fill:#e8eaf6,stroke:#3949ab,color:#1a237e
    style CRONS fill:#e8eaf6,stroke:#3949ab,color:#1a237e
    style GH fill:#e8eaf6,stroke:#3949ab,color:#1a237e
```

**Particularités :**
- **Mémoire partagée** : sync `default ↔ leo-copilot ↔ bavi-leo` toutes les 30min via `sync-memory.py`
- **100% DeepSeek** : plus de dépendance Gemini — réflexion supérieure, pas de quota
- **Focus** : infrastructure uniquement, sauf demande explicite de Christophe

---

## 3. 🧭 @bavi_leo_voyages_bot — Voyages

Bot isolé pour les roadbooks camping-car. Les amis et la famille l'utilisent.

```mermaid
flowchart LR
    subgraph BOT2["🧭 Profil bavi-leo"]
        direction TB
        P2["📋 Profil: bavi-leo"]
        B2["📱 @bavi_leo_voyages_bot"]
        M2["⚡ DeepSeek Flash"]
        S2["📝 Skills<br/>Sylvie · Maps · Wiki"]
        E2["📄 Export PDF / DOCX"]
    end

    style BOT2 fill:#e8f5e9,stroke:#388e3c,stroke-width:3px,color:#1b5e20
    style P2 fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#1b5e20
    style B2 fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    style M2 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style S2 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style E2 fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
```

---

## 4. Schéma complet — Flux de données

```mermaid
flowchart TB
    User["👤 Christophe"]

    subgraph TELEGRAM["📱 Telegram"]
        DM["DM @tofdan<br/>→ LEO"]
        COP["@hermes_leo_copilot_bot<br/>→ Copilot"]
        VOY["@bavi_leo_voyages_bot<br/>→ Voyages"]
    end

    subgraph HERMES["🖥️ Hermes (3 profils)"]
        DEF["default<br/>DeepSeek Flash"]
        LCP["leo-copilot<br/>DeepSeek Pro"]
        BAV["bavi-leo<br/>DeepSeek Flash"]
    end

    subgraph API["☁️ API Externes"]
        DS["DeepSeek API"]
    end

    subgraph OUTPUT["📊 Output"]
        DASH["7 Dashboards<br/>GitHub Pages"]
        N8N["5 Workflows n8n"]
        CRON["30 Crons"]
        ISSUES["leo-tracker<br/>GitHub Issues"]
    end

    User --> DM
    User --> COP
    User --> VOY

    DM --> DEF
    COP --> LCP
    VOY --> BAV

    DEF --> DS
    LCP --> DS
    BAV --> DS

    LCP --> DASH
    LCP --> N8N
    LCP --> CRON
    LCP --> ISSUES

    style User fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    style TELEGRAM fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    style HERMES fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style API fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style OUTPUT fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
```

---

## 5. Routage

| Tâche | Vers qui | Modèle | Profil |
|:------|:---------|:-------|:-------|
| Dialogue général, config, veille | **LEO** (DM) | DeepSeek Flash | `default` |
| Code, API, debug, analyses complexes | Sous-agent auto | DeepSeek Pro | `default` |
| Infrastructure (n8n, dashboards, déploiements) | → `@hermes_leo_copilot_bot` | **DeepSeek Pro** | `leo-copilot` |
| Roadbooks, voyages camping-car | → `@bavi_leo_voyages_bot` | DeepSeek Flash | `bavi-leo` |
| Classification emails, parsing local | Ollama (LEO) | qwen2.5:7b | API directe |

---

## Résumé

| Concept | C'est quoi ? | Handle Telegram ? | Moteur | Profil |
|:--------|:-------------|:------------------|:-------|:-------|
| **LEO** | Agent Hermes principal | Non — DM direct | DeepSeek Flash + Pro | `default` |
| **@hermes_leo_copilot_bot** | Bot infrastructure | Oui | **DeepSeek Pro** | `leo-copilot` |
| **@bavi_leo_voyages_bot** | Bot voyages | Oui | DeepSeek Flash | `bavi-leo` |

**LEO n'est pas un bot Telegram. LEO est ton majordome IA.** Les bots sont des extensions spécialisées avec leurs propres profils, mémoires et accès.

---

*Document mis à jour le 04/07/2026 — 00:00:00 — Modèles DeepSeek unifiés 🦁*

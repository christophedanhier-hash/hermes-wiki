# 🤖 Bots Telegram — Écosystème LEO

> **3 bots, 3 missions, 1 mémoire partagée** — chaque bot a un modèle, un profil Hermes et un rôle dédié.

---

## 🗺️ Architecture globale

```mermaid
flowchart TB
    User["👤 Christophe"]

    subgraph BOTS["🤖 Bots Telegram"]
        direction LR
        LeoFlash["🦁 @hermes_leo_bot<br/>━━━━━━━━━━<br/>DeepSeek Flash<br/>Chat quotidien"]
        Copilot["🔧 @hermes_leo_copilot_bot<br/>━━━━━━━━━━<br/>DeepSeek Pro<br/>Infrastructure"]
        Voyages["🧭 @bavi_leo_voyages_bot<br/>━━━━━━━━━━<br/>DeepSeek Flash<br/>Voyages"]
    end

    subgraph PROVIDERS["☁️ Providers"]
        DS["DeepSeek API<br/>Flash + Pro"]
    end

    subgraph MEMORY["📁 Mémoire partagée"]
        SYNC["sync-memory.py<br/>toutes les 30min"]
        M1["MEMORY.md<br/>default"]
        M2["MEMORY.md<br/>leo-copilot"]
        M3["MEMORY.md<br/>bavi-leo"]
    end

    User -->|"chat quotidien"| LeoFlash
    User -->|"code, infra, n8n"| Copilot
    User -->|"roadbooks, voyages"| Voyages

    LeoFlash --> DS
    Copilot --> DS
    Voyages --> DS

    SYNC --> M1
    SYNC --> M2
    SYNC --> M3
    M1 <-.->|"réplication"| M2
    M2 <-.->|"réplication"| M3

    style User fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    style LeoFlash fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    style Copilot fill:#ede7f6,stroke:#5e35b1,color:#311b92
    style Voyages fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
    style DS fill:#fff3e0,stroke:#e65100,color:#bf360c
    style SYNC fill:#fce4ec,stroke:#c62828,color:#b71c1c
```

---

## 1️⃣ 🦁 `@hermes_leo_bot` — Leo Hermes (Dialogue)

|||
|--|--|
| **Rôle** | Chat quotidien, conversation générale, veille |
| **Modèle** | **DeepSeek Flash** (deepseek-v4-flash) |
| **Provider** | DeepSeek API directe |
| **Profil Hermes** | `default` |
| **Latence** | ⚡ < 2s |
| **Coût** | $0.15/M tokens — suivi dashboard budget |
| **Fallback** | DeepSeek Pro si Flash indisponible |

### Flux de communication

```mermaid
flowchart LR
    TG["📱 Telegram DM<br/>@tofdan"]
    GW["🌐 Gateway<br/>profil default"]
    HERMES["🦁 Hermes Agent<br/>LEO"]
    DS_API["☁️ DeepSeek API<br/>Flash"]

    TG --> GW --> HERMES --> DS_API
    DS_API --> HERMES --> GW --> TG

    style TG fill:#e0f7fa,stroke:#00838f,color:#004d40
    style GW fill:#f3e5f5,stroke:#7b1fa2,color:#4a148c
    style HERMES fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    style DS_API fill:#fff3e0,stroke:#e65100,color:#bf360c
```

---

## 2️⃣ 🔧 `@hermes_leo_copilot_bot` — Leo Copilot (Infrastructure)

||:--|:--|
| **Rôle** | Code, infrastructure, n8n, dashboards, déploiements |
| **Modèle** | **DeepSeek Pro** (deepseek-v4-pro) |
| **Provider** | DeepSeek API directe |
| **Profil Hermes** | `leo-copilot` (isolé, dédié) |
| **Latence** | ⚡ < 3s |
| **Coût** | $ pay-as-you-go — suivi dashboard budget |
| **Fallback** | DeepSeek Flash si Pro indisponible |
| **Sync mémoire** | Cron `sync-memory` toutes les 30min — partage mémoire entre profils |

### Architecture technique

```mermaid
flowchart TB
    subgraph COPILOT["🔧 Profil leo-copilot"]
        direction TB
        GW2["🌐 Gateway<br/>@hermes_leo_copilot_bot"]
        AGENT["🤖 Agent Hermes<br/>Leo Copilot"]
        SKILLS["📚 Skills<br/>n8n, dashboards,<br/>drive, watchdogs"]
    end

    DS_PRO["☁️ DeepSeek API<br/>Pro (deepseek-v4-pro)"]
    DS_FLASH["☁️ DeepSeek API<br/>Flash (fallback)"]
    MEM["📁 Sync mémoire<br/>← default + bavi-leo<br/>toutes les 30min"]
    DASH["📊 Dashboards<br/>GitHub Pages"]
    N8N["🔧 n8n<br/>:5678"]

    GW2 --> AGENT
    AGENT --> SKILLS
    AGENT --> DS_PRO
    AGENT -.->|fallback| DS_FLASH
    MEM -.-> AGENT
    AGENT --> DASH
    AGENT --> N8N

    style COPILOT fill:#ede7f6,stroke:#5e35b1,stroke-width:3px,color:#311b92
    style GW2 fill:#e0f7fa,stroke:#00838f,color:#004d40
    style AGENT fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    style SKILLS fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20
    style DS_PRO fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style DS_FLASH fill:#fff3e0,stroke:#e65100,stroke-dasharray:5,color:#bf360c
    style MEM fill:#fce4ec,stroke:#c62828,color:#b71c1c
    style DASH fill:#e8eaf6,stroke:#3949ab,color:#1a237e
    style N8N fill:#e8eaf6,stroke:#3949ab,color:#1a237e
```

### Pourquoi DeepSeek Pro et plus Gemini ?

- **Qualité de réflexion supérieure** pour les tâches d'infrastructure complexes
- **Mémoire partagée** avec les autres profils via `sync-memory.py`
- **Pas de limite de quota** (Gemini API tier gratuit = 60 req/min max)
- **Un seul provider** simplifie la gestion des clés et le suivi budgétaire

---

## 3️⃣ 🧭 `@bavi_leo_voyages_bot` — Voyages

|||
|--|--|
| **Rôle** | Organisation de voyages camping-car |
| **Modèle** | DeepSeek Flash (deepseek-v4-flash) |
| **Profil Hermes** | `bavi-leo` (isolé) |
| **Accès** | Christophe + invités (accès limité aux skills voyage) |
| **Skills** | `bureau-sylvie`, `voyages-wiki`, `maps` |
| **Wiki** | [🧭 Voyages](https://christophedanhier-hash.github.io/voyages-wiki/) |

---

## 📊 Comparatif

| Critère | 🦁 Leo Hermes | 🔧 Leo Copilot | 🧭 Voyages |
|:--------|:------------:|:-----------:|:-------:|
| **Modèle** | DeepSeek Flash | **DeepSeek Pro** | DeepSeek Flash |
| **Latence** | ⚡ < 2s | ⚡ < 3s | ⚡ < 2s |
| **Coût** | $0.15/M tokens | $ pay-as-you-go | $0.15/M tokens |
| **Usage principal** | Chat quotidien | **Infra, code, n8n** | Voyages |
| **Profil** | `default` | `leo-copilot` | `bavi-leo` |
| **Provider** | DeepSeek | DeepSeek | DeepSeek |
| **Accès invités** | ❌ | ❌ | ✅ |
| **Sync mémoire** | ✅ 30min | ✅ 30min | ✅ 30min |

---

## 🔧 Maintenance

| Action | Commande / Cron |
|:-------|:----------------|
| **Redémarrer Leo Copilot** | `hermes -p leo-copilot gateway restart` |
| **Vérifier sync mémoire** | `python3 /opt/data/scripts/sync-memory.py --check` |
| **Dashboards** | Tous auto-déployés via GH Pages |

---

*Document mis à jour le 04/07/2026 — 00:00:00 — Modèles DeepSeek unifiés 🦁*

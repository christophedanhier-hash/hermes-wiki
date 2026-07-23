# 🤖 Bots Telegram — Écosystème LEO

> **5 bots, 5 missions, mémoire unifiée default↔michel** — chaque bot a un profil Hermes et un rôle dédié.

---

## 🗺️ Architecture globale

```mermaid
flowchart TB
    User["👤 Christophe"]

    subgraph BOTS["🤖 Bots Telegram"]
        direction LR
        LeoFlash["🦁 @hermes_leo_bot<br/>━━━━━━━━━━<br/>DeepSeek Flash<br/>Chat quotidien"]
        Michel["🔧 @hermes_leo_copilot_bot<br/>━━━━━━━━━━<br/>DeepSeek Pro<br/>Infrastructure"]
        Sylvia["🧭 @bavi_leo_voyages_bot<br/>━━━━━━━━━━<br/>DeepSeek Flash<br/>Voyages"]
        Emile["👤 @Bureau_ia_emilie_bot<br/>━━━━━━━━━━<br/>DeepSeek Flash<br/>Assistant pédagogique"]
        Robert["🏛️ @bureau_robert_bot<br/>━━━━━━━━━━<br/>DeepSeek Pro<br/>Conseil stratégique"]
    end

    subgraph PROVIDERS["☁️ Providers"]
        DS["DeepSeek API<br/>Flash + Pro"]
        GF["Gemini API<br/>3.5 Flash"]
        OL["Ollama local<br/>qwen2.5:7b"]
    end

    subgraph MEMORY["📁 Mémoire"]
        SYNC["sync-memory.py<br/>toutes les 30min"]
        M1["MEMORY.md<br/>default"]
        M2["MEMORY.md<br/>michel"]
    end

    User -->|"chat quotidien"| LeoFlash
    User -->|"code, infra, scripts"| Michel
    User -->|"roadbooks, voyages"| Sylvia
    User -->|"assistant perso"| Emile
    User -->|"conseil stratégique"| Robert

    LeoFlash --> DS
    Michel --> DS
    LeoFlash -.->|fallback| GF
    LeoFlash -.->|fallback| OL
    Sylvia --> DS
    Emile --> DS
    Robert --> DS

    SYNC --> M1
    SYNC --> M2
    M1 <-.->|"réplication"| M2

    style User fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    style LeoFlash fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    style Michel fill:#ede7f6,stroke:#5e35b1,color:#311b92
    style Sylvia fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
    style Emile fill:#fff8e1,stroke:#f57f17,color:#e65100
    style Robert fill:#fce4ec,stroke:#c62828,color:#b71c1c
    style DS fill:#fff3e0,stroke:#e65100,color:#bf360c
    style GF fill:#e0f2f1,stroke:#00695c,color:#004d40
    style OL fill:#f3e5f5,stroke:#6a1b9a,color:#4a148c
    style SYNC fill:#fce4ec,stroke:#c62828,color:#b71c1c
```

---

## 1️⃣ 🦁 `@hermes_leo_bot` — Leo Hermes (Dialogue)

| | |
|---|---|
| **Rôle** | Chat quotidien, conversation générale, veille |
| **Modèle** | **DeepSeek Flash** (deepseek-v4-flash) |
| **Provider** | DeepSeek API directe |
| **Profil Hermes** | `default` |
| **Latence** | ⚡ < 2s |
| **Coût** | DeepSeek V4 Flash: $0.14/1M input, $0.28/1M output |
| **Fallback** | Gemini 3.5 Flash → Ollama local qwen2.5:7b |

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

## 2️⃣ 🔧 `@hermes_leo_copilot_bot` — Michel (Infrastructure)

> Ce bot correspond au profil **`michel`** (ex-leo-copilot, renommé juillet 2026).

| | |
|:---|:---|
| **Rôle** | Code, infrastructure, dashboards, déploiements, audits |
| **Modèle** | **DeepSeek Pro** (deepseek-v4-pro) |
| **Provider** | DeepSeek API directe |
| **Profil Hermes** | `michel` (isolé, mémoire unifiée avec `default`) |
| **Latence** | ⚡ < 3s |
| **Coût** | $ pay-as-you-go |
| **Fallback** | deepseek-v4-flash → gemini-3.5-flash → qwen2.5:7b |
| **Crons** | 41 jobs (tous actifs) |

---

## 3️⃣ 🧭 `@bavi_leo_voyages_bot` — Sylvia (Voyages)

> Ce bot correspond au profil **`sylvia`** (ex-bavi-leo).

| | |
|---|---|
| **Rôle** | Roadbooks, itinéraires, organisation voyages camping-car |
| **Modèle** | DeepSeek Flash (deepseek-v4-flash) |
| **Profil Hermes** | `sylvia` (isolé) |
| **Accès** | Christophe uniquement |
| **Wiki** | [🧭 Voyages](https://christophedanhier-hash.github.io/voyages-wiki/) |

---

## 4️⃣ 👤 `@Bureau_ia_emilie_bot` — Émile (Pédagogie)

| | |
|---|---|
| **Rôle** | Assistant pédagogique pour mémoire de fin d'études |
| **Modèle** | DeepSeek Flash (deepseek-v4-flash) |
| **Profil Hermes** | `emile` (isolé) |
| **Accès** | Christophe uniquement |

---

## 5️⃣ 🏛️ `@bureau_robert_bot` — Robert (Conseil Stratégique)

> Ce bot correspond au profil **`robert`** (ex-bureau-robert).

| | |
|---|---|
| **Rôle** | Conseil stratégique IT, audits, analyses |
| **Modèle** | DeepSeek Pro (deepseek-v4-pro) |
| **Profil Hermes** | `robert` (isolé) |
| **Accès** | Christophe uniquement |

---

## 📊 Comparatif

| Critère | 🦁 Leo Hermes | 🔧 Michel | 🧭 Sylvia | 👤 Émile | 🏛️ Robert |
|:--------|:------------:|:-----------:|:-------:|:------:|:-------:|
| **Modèle** | DeepSeek Flash | **DeepSeek Pro** | DeepSeek Flash | DeepSeek Flash | DeepSeek Pro |
| **Latence** | ⚡ < 2s | ⚡ < 3s | ⚡ < 2s | ⚡ < 2s | ⚡ < 3s |
| **Profil** | `default` | `michel` | `sylvia` | `emile` | `robert` |
| **Provider** | DeepSeek (+ Gemini/Ollama fallback) | DeepSeek | DeepSeek | DeepSeek | DeepSeek |
| **Mémoire** | Unifiée (default+michel) | Unifiée (default+michel) | Séparée | Séparée | Séparée |
| **Crons** | 0 | **41 (tous actifs)** | 0 | 0 | 0 |

> **Note** : Les profils `leo-copilot`, `bavi-leo`, `bureau-robert` ont été renommés respectivement en `michel`, `sylvia`, `robert` lors de la consolidation de juillet 2026. Les noms de bots Telegram sont restés inchangés.

---

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)

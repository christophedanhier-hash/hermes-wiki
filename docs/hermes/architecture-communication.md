# 🏗️ Architecture de Communication

## Les 3 entités

```
👤 Toi (Christophe)
   │
   ├── 🤖 LEO (moi, Hermes Agent)
   │     DeepSeek Flash + Pro ← toi via DM Telegram
   │     └── Délègue les sous-tâches → DeepSeek Pro
   │
   ├── 🤖 @hermes_leo_copilot_bot
   │     Gemini 3.5 Flash ← focus infrastructure
   │     Mémoire synchronisée avec LEO (30min)
   │
   └── 🤖 @bavi_leo_voyages_bot
         DeepSeek v4 Flash ← voyages camping-car
         Profil Hermes isolé (bavi-leo)
```

---

## 1. LEO — L'Agent Hermes principal

**LEO** est l'agent **Hermes Agent** lui-même — ton majordome IA. Pas de handle Telegram : tu me parles en DM, le gateway fait le pont.

```mermaid
flowchart TD
    subgraph SERVEUR["🖥️ SERVEUR LEO"]
        direction TB
        Hermes["🤖 Hermes Agent<br/>(LEO — Majordome)"]
        Gateway["🌐 Gateway DeepSeek<br/>(point d'entrée)"]
        Ollama["🏠 Ollama local<br/>qwen2.5:7b<br/>(tâches gratuites)"]
        SubAgent["🧠 Sous-agents<br/>DeepSeek Pro<br/>(tâches complexes)"]
        
        Hermes <--> Gateway
        Ollama -->|◀ gateway| Gateway
        Hermes -.->|délégation| SubAgent
    end
    
    Gateway --> Telegram["📱 Telegram<br/>(DM @tofdan)"]
    
    style SERVEUR fill:#e8f5f9,stroke:#0288d1,stroke-width:3px,color:#01579b
    style Hermes fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style Gateway fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style Ollama fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style SubAgent fill:#fce4ec,stroke:#c62828,stroke-width:2px,color:#b71c1c
    style Telegram fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    linkStyle default stroke-width:2px,fill:none
```

### Comment ça marche

1. **Tu parles à LEO via Telegram** — le Gateway DeepSeek fait le pont
2. **LEO n'a pas de handle** — réponse en DM
3. **Tâches complexes** → sous-agents DeepSeek Pro automatiquement
4. **Tâches trop lourdes** → proposition de déléguer à `@hermes_leo_copilot_bot`

---

## 2. @hermes_leo_copilot_bot — Infrastructure

Bot spécialisé **infrastructure** (n8n, serveurs, déploiements, watchdogs, dashboards). Propulsé par **Gemini 3.5 Flash** (API Google directe).

```mermaid
flowchart LR
    subgraph BOT1["🤖 Leo Copilot Bot"]
        direction TB
        P1["📋 Profil Hermes : leo-copilot"]
        B1["📱 @hermes_leo_copilot_bot"]
        M1["⚡ Gemini 3.5 Flash"]
        F1["🔄 Fallback DeepSeek Flash"]
        SYNC["📁 Sync mémoire<br/>avec LEO (30min)"]
    end
    
    B1 --> GEM["☁️ Google Gemini API"]
    GEM --> M1
    SYNC -.->|MEMORY.md| P1
    
    style BOT1 fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#1b5e20
    style P1 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style B1 fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    style M1 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style F1 fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style SYNC fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    style GEM fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
```

**Particularités :**
- **Mémoire partagée** : sync `default → leo-copilot` toutes les 30min via `sync-memory.py`
- **Pas de Copilot** : ancien proxy `copilot-proxy.py` supprimé, remplacé par API Gemini directe
- **Focus** : infrastructure uniquement, sauf demande explicite de ta part

---

## 3. @bavi_leo_voyages_bot — Voyages

Bot isolé pour les roadbooks camping-car. Les amis et la famille l'utilisent.

```mermaid
flowchart LR
    subgraph BOT2["🤖 BAVI LEO Voyages Bot"]
        direction TB
        P2["📋 Profil Hermes : bavi-leo"]
        B2["📱 @bavi_leo_voyages_bot"]
        M2["🧠 DeepSeek v4 Flash"]
        S2["📝 Skill : Sylvie (Voyages)"]
        A2["🔑 SSH → voyages-wiki"]
        E2["📄 Export PDF / DOCX"]
    end
    
    style BOT2 fill:#fff3e0,stroke:#e65100,stroke-width:3px,color:#bf360c
    style P2 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style B2 fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    style M2 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style S2 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style A2 fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style E2 fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
```

---

## 4. Schéma complet

```mermaid
flowchart TD
    Toi["👤 Toi (Christophe)"] --> DM["📱 Telegram DM"]
    DM --> Gateway2["🌐 Gateway DeepSeek"]
    
    Gateway2 --> LEO["🤖 LEO Agent<br/>(DeepSeek Flash+Pro)"]
    Gateway2 --> Ollama2["🏠 Ollama<br/>qwen2.5"]
    
    LEO --> Dash["📊 Dashboards<br/>(GitHub Pages)"]
    LEO --> Wiki["📚 Wikis<br/>(MkDocs sur GH)"]
    LEO --> Crons["⏰ Crons<br/>(automatisés)"]
    LEO --> BAVI["🏢 Bureaux Virtuels<br/>(BAVI PRO/PRIVÉ)"]
    LEO --> Sub["🧠 Sous-agents<br/>DeepSeek Pro"]
    
    subgraph BOT_INFRA["🤖 Bot Infrastructure"]
        COP["📱 @hermes_leo_copilot_bot"] --> GEMAPI["☁️ Gemini 3.5 Flash API"]
        COP -.->|Fallback| DSFALL["DeepSeek Flash"]
    end
    
    subgraph BOT_VOY["🤖 Bot Voyages"]
        BOTV["📱 @bavi_leo_voyages_bot"] --> DS["🧠 DeepSeek v4 Flash"]
    end
    
    Toi --> COP
    Amis["👨‍👩‍👧‍👦 Amis & Famille"] --> BOTV
    
    MEM["📁 Sync mémoire<br/>(30min)"] -.->|MEMORY.md| COP
    
    style Toi fill:#e8f5f9,stroke:#0288d1,stroke-width:2px,color:#01579b
    style DM fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    style Gateway2 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style LEO fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style Ollama2 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style Sub fill:#fce4ec,stroke:#c62828,stroke-width:2px,color:#b71c1c
    style Dash fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    style Wiki fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    style Crons fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    style BAVI fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    style BOT_INFRA fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#1b5e20
    style COP fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    style GEMAPI fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style DSFALL fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style BOT_VOY fill:#fff3e0,stroke:#e65100,stroke-width:3px,color:#bf360c
    style BOTV fill:#fbe9e7,stroke:#d84315,stroke-width:2px,color:#bf360c
    style DS fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style MEM fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    style Amis fill:#e8f5f9,stroke:#0288d1,stroke-width:2px,color:#01579b
    linkStyle default stroke-width:2px,fill:none
```

---

## 5. Routage

| Tâche | Vers qui | Modèle |
|:------|:---------|:-------|
| Dialogue général, config, veille | **LEO** (moi) | DeepSeek Flash |
| Code, API, debug, analyses complexes | Sous-agent automatique | DeepSeek Pro |
| Infrastructure (n8n, serveurs, déploiements) | → `@hermes_leo_copilot_bot` | Gemini 3.5 Flash |
| Roadbooks, voyages camping-car | → `@bavi_leo_voyages_bot` | DeepSeek v4 Flash |
| Tâches lourdes hors-scope DeepSeek | Proposition → `@hermes_leo_copilot_bot` | Gemini 3.5 Flash |

---

## Résumé

| Concept | C'est quoi ? | Handle Telegram ? | Moteur |
|:--------|:-------------|:------------------|:-------|
| **LEO** | Agent Hermes principal | Non — DM direct | DeepSeek Flash + Pro |
| **@hermes_leo_copilot_bot** | Bot infrastructure isolé | Oui | Gemini 3.5 Flash |
| **@bavi_leo_voyages_bot** | Bot voyages isolé | Oui | DeepSeek v4 Flash |

**LEO n'est pas un bot Telegram. LEO est ton majordome IA.** Les bots sont des extensions spécialisées avec leurs propres profils, mémoires et accès.

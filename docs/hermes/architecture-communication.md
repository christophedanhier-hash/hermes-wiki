# 🏗️ Architecture de Communication

## LEO n'est pas un bot Telegram

**LEO** est l'agent **Hermes Agent** lui-même — votre majordome IA qui tourne sur le serveur du même nom. Il n'existe pas de « bot LEO » séparé.

``` mermaid
flowchart TD
    subgraph SERVEUR["🖥️ SERVEUR LEO"]
        direction TB
        Hermes["🤖 Hermes Agent<br/>(LEO — Majordome)"]
        Gateway["🌐 Gateway DeepSeek v4<br/>(point d'entrée)"]
        Ollama["🏠 Ollama local<br/>qwen2.5:7b<br/>(tâches gratuites)"]
        Gemini["⚡ Gemini fallback<br/>(API externe)"]
        
        Hermes <--> Gateway
        Ollama -->|◀ gateway| Gateway
        Gemini -.->|fallback| Gateway
    end
    
    Gateway --> Telegram["📱 Telegram<br/>(DM @tofdan)"]
    
    style SERVEUR fill:#e8f5f9,stroke:#0288d1,stroke-width:3px,color:#01579b
    style Hermes fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style Gateway fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style Ollama fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style Gemini fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style Telegram fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    linkStyle default stroke-width:2px,fill:none
```

### Comment ça marche

1. **Tu parles à LEO via Telegram** — le Gateway DeepSeek fait le pont entre Telegram et l'agent Hermes
2. **LEO n'a pas de handle Telegram** — tu me parles en DM, je suis l'agent qui répond via le gateway
3. **Le canal Telegram** est mon interface principale, au même titre que le terminal local

---

## Les vrais bots Telegram

Un **bot Telegram** (`@quelque_chose_bot`) est un profil Hermes **isolé** avec sa propre personnalité et ses propres accès.

### BAVI LEO Voyages Bot

``` mermaid
flowchart LR
    subgraph BOT["🤖 BAVI LEO Voyages Bot"]
        direction TB
        P["📋 Profil Hermes : bavi-leo"]
        B["📱 @bavi_leo_voyages_bot"]
        M["🧠 DeepSeek v4 Flash"]
        S["📝 Skill : Sylvie (Voyages)"]
        A["🔑 SSH → voyages-wiki"]
        E["📄 Export PDF / DOCX"]
    end
    
    style BOT fill:#fff3e0,stroke:#e65100,stroke-width:3px,color:#bf360c
    style P fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style B fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    style M fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style S fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style A fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style E fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
```

**Usage** : Les amis et la famille l'utilisent pour créer des roadbooks camping-car. LEO ne délègue pas au bot — chaque entité travaille indépendamment.

### Pourquoi un bot séparé ?

- **Isolation** — le bot a sa propre mémoire, ses propres skills, son propre budget DeepSeek
- **Accès restreint** — le bot ne peut que écrire sur `voyages-wiki`, rien d'autre
- **Personnalité dédiée** — le bot a son propre SOUL.md (sa « personnalité »), distincte de LEO

---

## Schéma complet

``` mermaid
flowchart TD
    Toi["👤 Toi (Christophe)"] --> DM["📱 Telegram DM"]
    DM --> Gateway2["🌐 Gateway DeepSeek<br/>(1 seul profil)"]
    
    Gateway2 --> LEO["🤖 LEO Agent<br/>(Hermes)"]
    Gateway2 --> Ollama2["🏠 Ollama<br/>qwen2.5"]
    Gateway2 -.->|fallback| Gemini2["⚡ Gemini<br/>(API externe)"]
    
    LEO --> Dash["📊 Dashboards<br/>(GitHub Pages)"]
    LEO --> Wiki["📚 Wikis<br/>(MkDocs sur GH)"]
    LEO --> Crons["⏰ Crons<br/>(automatisés)"]
    LEO --> BAVI["🏢 Bureaux Virtuels<br/>(BAVI PRO/PRIVÉ)"]
    
    subgraph BOT2["🤖 Bot Telegram séparé"]
        direction LR
        Bot["🧭 @bavi_leo_voyages_bot"] -->|Profil Hermes isolé| Skill3["📝 Skill: Sylvie<br/>(Voyages)"]
    end
    
    Amis["👨‍👩‍👧‍👦 Amis & Famille"] --> Bot
    
    style Toi fill:#e8f5f9,stroke:#0288d1,stroke-width:2px,color:#01579b
    style DM fill:#e0f7fa,stroke:#00838f,stroke-width:2px,color:#004d40
    style Gateway2 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
    style LEO fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style Ollama2 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style Gemini2 fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#bf360c
    style Dash fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    style Wiki fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    style Crons fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    style BAVI fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#1a237e
    style BOT2 fill:#fff3e0,stroke:#e65100,stroke-width:3px,color:#bf360c
    style Bot fill:#fbe9e7,stroke:#d84315,stroke-width:2px,color:#bf360c
    style Skill3 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style Amis fill:#e8f5f9,stroke:#0288d1,stroke-width:2px,color:#01579b
    linkStyle default stroke-width:2px,fill:none
```

---

## Résumé

| Concept | C'est quoi ? | Handle Telegram ? |
|---------|-------------|-------------------|
| **LEO** | Agent Hermes principal (toi + moi) | Non — DM direct via gateway |
| **BAVI LEO Voyages Bot** | Profil Hermes isolé pour les voyages | Oui — `@bavi_leo_voyages_bot` |
| **Autres bots** | Pas de bots supplémentaires | — |

**LEO n'est pas un bot Telegram. LEO est ton majordome IA.**

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
    
    style SERVEUR fill:#1a1a2e,stroke:#7c4dff,color:#e8e8ff
    style Hermes fill:#16213e,stroke:#4fc3f7,color:#e8e8ff
    style Gateway fill:#0f3460,stroke:#7c4dff,color:#e8e8ff
    style Ollama fill:#1b5e20,stroke:#4caf50,color:#e8e8ff
    style Gemini fill:#e65100,stroke:#ff9800,color:#e8e8ff
    style Telegram fill:#004d40,stroke:#26c6da,color:#e8e8ff
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
    
    style BOT fill:#1a1a2e,stroke:#7c4dff,color:#e8e8ff
    style P fill:#16213e,stroke:#4fc3f7,color:#e8e8ff
    style B fill:#0f3460,stroke:#7c4dff,color:#e8e8ff
    style M fill:#1a237e,stroke:#536dfe,color:#e8e8ff
    style S fill:#004d40,stroke:#26c6da,color:#e8e8ff
    style A fill:#e65100,stroke:#ff9800,color:#e8e8ff
    style E fill:#1b5e20,stroke:#4caf50,color:#e8e8ff
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
    Gateway2 -.-> Gemini2["⚡ Gemini<br/>(fallback)"]
    
    LEO --> Dash["📊 Dashboards<br/>(GitHub Pages)"]
    LEO --> Wiki["📚 Wikis<br/>(MkDocs sur GH)"]
    LEO --> Crons["⏰ Crons<br/>(automatisés)"]
    LEO --> BAVI["🏢 Bureaux Virtuels<br/>(BAVI PRO/PRIVÉ)"]
    
    subgraph BOT2["🤖 Bot Telegram séparé"]
        direction LR
        Bot["🧭 @bavi_leo_voyages_bot"] -->|Profil Hermes isolé| Skill["📝 Skill: Sylvie<br/>(Voyages)"]
    end
    
    Amis["👨‍👩‍👧‍👦 Amis & Famille"] --> Bot
    
    style Toi fill:#1a1a2e,stroke:#7c4dff,color:#e8e8ff
    style DM fill:#004d40,stroke:#26c6da,color:#e8e8ff
    style Gateway2 fill:#0f3460,stroke:#7c4dff,color:#e8e8ff
    style LEO fill:#16213e,stroke:#4fc3f7,color:#e8e8ff
    style Ollama2 fill:#1b5e20,stroke:#4caf50,color:#e8e8ff
    style Gemini2 fill:#e65100,stroke:#ff9800,color:#e8e8ff
    style Dash fill:#1a237e,stroke:#536dfe,color:#e8e8ff
    style Wiki fill:#1a237e,stroke:#536dfe,color:#e8e8ff
    style Crons fill:#1a237e,stroke:#536dfe,color:#e8e8ff
    style BAVI fill:#1a237e,stroke:#536dfe,color:#e8e8ff
    style BOT2 fill:#1a1a2e,stroke:#ff7043,color:#e8e8ff
    style Bot fill:#bf360c,stroke:#ff7043,color:#e8e8ff
    style Skill fill:#4e342e,stroke:#ffab91,color:#e8e8ff
    style Amis fill:#1a1a2e,stroke:#7c4dff,color:#e8e8ff
```

---

## Résumé

| Concept | C'est quoi ? | Handle Telegram ? |
|---------|-------------|-------------------|
| **LEO** | Agent Hermes principal (toi + moi) | Non — DM direct via gateway |
| **BAVI LEO Voyages Bot** | Profil Hermes isolé pour les voyages | Oui — `@bavi_leo_voyages_bot` |
| **Autres bots** | Pas de bots supplémentaires | — |

**LEO n'est pas un bot Telegram. LEO est ton majordome IA.**

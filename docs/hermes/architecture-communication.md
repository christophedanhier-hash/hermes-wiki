# 🏗️ Architecture de Communication

## LEO n'est pas un bot Telegram

**LEO** est l'agent **Hermes Agent** lui-même — votre majordome IA qui tourne sur le serveur du même nom. Il n'existe pas de « bot LEO » séparé.

```
┌─────────────────────────────────────────────────────────┐
│                  SERVEUR LEO                             │
│                                                          │
│   ┌──────────────────┐     ┌──────────────────────────┐  │
│   │  Hermes Agent     │────▶│  Gateway DeepSeek v4    │  │
│   │  (LEO — Majordome)│◀────│  (point d'entrée)       │  │
│   └──────────────────┘     └──────────┬───────────────┘  │
│                                       │                  │
│   ┌──────────────────┐               │                  │
│   │  Ollama local     │  qwen2.5:7b  │                  │
│   │  (tâches gratuites)│◀────────────┘                  │
│   └──────────────────┘                                  │
│                                                          │
│   ┌──────────────────┐                                   │
│   │  Gemini fallback  │  (API externe)                   │
│   └──────────────────┘                                   │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
                   ┌──────────────┐
                   │   Telegram    │
                   │   (DM @tofdan)│
                   └──────────────┘
```

### Comment ça marche

1. **Tu parles à LEO via Telegram** — le Gateway DeepSeek fait le pont entre Telegram et l'agent Hermes
2. **LEO n'a pas de handle Telegram** — tu me parles en DM, je suis l'agent qui répond via le gateway
3. **Le canal Telegram** est mon interface principale, au même titre que le terminal local

---

## Les vrais bots Telegram

Un **bot Telegram** (`@quelque_chose_bot`) est un profil Hermes **isolé** avec sa propre personnalité et ses propres accès.

### BAVI LEO Voyages Bot

```
┌─────────────────────────────────────────┐
│  Profil Hermes : bavi-leo               │
│  Bot Telegram : @bavi_leo_voyages_bot   │
│  Modèle : DeepSeek v4 Flash             │
│  Skill : Sylvie (Voyages)              │
│  Accès : SSH → voyages-wiki (deploy key)│
│  Export : PDF/DOCX (weasyprint)        │
└─────────────────────────────────────────┘
```

**Usage** : Les amis et la famille l'utilisent pour créer des roadbooks camping-car. LEO ne délègue pas au bot — chaque entité travaille indépendamment.

### Pourquoi un bot séparé ?

- **Isolation** — le bot a sa propre mémoire, ses propres skills, son propre budget DeepSeek
- **Accès restreint** — le bot ne peut que écrire sur `voyages-wiki`, rien d'autre
- **Personnalité dédiée** — le bot a son propre SOUL.md (sa « personnalité »), distincte de LEO

---

## Schéma complet

```
                    ┌─────────────────┐
                    │   Telegram DM   │◀──── Toi (Christophe)
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Gateway DeepSeek│
                    │  (1 seul profil) │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
       ┌──────▼──────┐ ┌────▼───┐  ┌──────▼──────┐
       │  LEO Agent   │ │ Ollama │  │  Gemini     │
       │  (Hermes)    │ │ qwen2.5│  │  (fallback) │
       └──────┬───────┘ └────────┘  └─────────────┘
              │
     ┌────────┼────────┬──────────┐
     │        │        │          │
     ▼        ▼        ▼          ▼
  Dashboards  Wikis  Crons  Bureaux Virtuels
  (GitHub    (MkDocs  (auto-   (BAVI PRO/PRIVÉ)
   Pages)    sur GH)  matisés)

                    ┌──────────────────┐
                    │  Telegram Bot    │
                    │@bavi_leo_voyages │◀──── Amis & Famille
                    └──────────────────┘
                    Profil Hermes isolé
                    Skill : Sylvie (Voyages)
```

---

## Résumé

| Concept | C'est quoi ? | Handle Telegram ? |
|---------|-------------|-------------------|
| **LEO** | Agent Hermes principal (toi + moi) | Non — DM direct via gateway |
| **BAVI LEO Voyages Bot** | Profil Hermes isolé pour les voyages | Oui — `@bavi_leo_voyages_bot` |
| **Autres bots** | Pas de bots supplémentaires | — |

**LEO n'est pas un bot Telegram. LEO est ton majordome IA.**

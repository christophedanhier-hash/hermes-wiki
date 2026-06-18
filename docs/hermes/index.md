# Guide Hermes Agent — L'IA qui travaille pour vous

Bienvenue dans le guide d'installation et d'utilisation d'**Hermes Agent**, la plateforme d'agent IA open source qui vous permet de déléguer des tâches à un assistant personnel automatisé.

Ce guide vous accompagne pas à pas, de l'installation à l'utilisation avancée, en prenant **LEO** (l'assistant de Christophe) comme exemple concret.

## Pourquoi Hermes Agent ?

Hermes Agent est un agent IA qui peut :

- **Exécuter des tâches** — écrire du code, analyser des documents, gérer des emails
- **Planifier des actions** — backups quotidiens, collecte de métriques, rapports automatiques
- **S'intégrer partout** — Telegram, email, Google Drive, GitHub, et bien plus
- **Travailler sans vous** — une fois configuré, il tourne 24/7

Contrairement à ChatGPT ou Claude (simples chatbots), Hermes Agent **agit** : il a accès à vos outils, fichiers et services.

## La philosophie LEO

> *"Un assistant n'est pas un chatbot. C'est quelqu'un qui anticipe, qui agit, et qui ne vous fait pas répéter deux fois."*

LEO a été construit pour être :
- **Efficace** — pas de blabla, des actions
- **Fiable** — des garde-fous contre les erreurs
- **Économe** — utilise le meilleur LLM pour chaque tâche (local gratuit ou cloud payant)
- **Discret** — tourne en arrière-plan, ne dérange que quand c'est important

## Structure du guide

``` mermaid
flowchart LR
    README["📖 README.md<br/>Introduction et philosophie"]

    subgraph INSTALL["📁 01-installation/"]
        direction TB
        Linux["linux.md<br/>Installation sur Debian/Ubuntu"]
        Windows["windows.md<br/>Installation sur Windows (WSL)"]
    end

    subgraph CONFIG["📁 02-configuration/"]
        direction TB
        Providers["providers.md<br/>Configuration LLM (DeepSeek, Ollama, Gemini)"]
        Profiles["profiles.md<br/>Profils, gateways, skills"]
    end

    subgraph UTIL["📁 03-utilisation/"]
        direction TB
        Quotidien["quotidien.md<br/>Usage quotidien (comme LEO)"]
        Crons["crons.md<br/>Tâches planifiées"]
        Dashboards["dashboards.md<br/>Monitoring et KPIs"]
    end

    subgraph PLUS["📁 04-aller-plus-loin/"]
        direction TB
        Troubleshooting["troubleshooting.md<br/>Problèmes courants et solutions"]
    end

    subgraph EXEMPLES["📁 exemples/"]
        direction TB
        LEO_ARCH["LEO.md<br/>Architecture complète de LEO"]
    end

    subgraph REFS["📁 references/"]
        direction TB
        Commandes["commandes.md<br/>Aide-mémoire des commandes"]
    end

    style README fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style INSTALL fill:#e8f5f9,stroke:#0288d1,stroke-width:3px,color:#01579b
    style CONFIG fill:#e8f5f9,stroke:#0288d1,stroke-width:3px,color:#01579b
    style UTIL fill:#e8f5f9,stroke:#0288d1,stroke-width:3px,color:#01579b
    style PLUS fill:#e8f5f9,stroke:#0288d1,stroke-width:3px,color:#01579b
    style EXEMPLES fill:#e8f5f9,stroke:#0288d1,stroke-width:3px,color:#01579b
    style REFS fill:#e8f5f9,stroke:#0288d1,stroke-width:3px,color:#01579b
    linkStyle default stroke-width:2px,fill:none
```

## Public visé

- **Débutant·e** — les pages d'installation vous guident pas à pas
- **Intermédiaire** — la configuration et les skills vous ouvrent les possibilités
- **Expert·e** — le troubleshooting et l'architecture LEO vous inspirent

## Licence

Ce guide est en licence libre — libre à vous de le partager, l'adapter et l'enrichir.

---

**Projet vivant** — ce guide évolue avec Hermes Agent. N'hésitez pas à contribuer !

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

```text
📖 hermes/index.md              → Présentation — introduction et philosophie
📁 hermes/installation/
   └── linux.md                 → Installation Linux
📁 hermes/configuration/
   ├── providers.md             → Providers LLM (DeepSeek, Ollama, Gemini)
   └── profiles.md              → Profils, gateways, skills
📁 hermes/utilisation/
   ├── quotidien.md             → Usage quotidien
   ├── dashboards.md            → Monitoring et KPIs
   ├── architecture-leo.md      → Architecture LEO (dashboard, vaults, crons)
   ├── bots-telegram.md         → Les 5 bots Telegram
   ├── securite.md              → Sécurité documentaire
   └── backup-recovery.md       → Backup & Recovery
📁 hermes/decisions/
   └── pourquoi-deepseek-pas-gemini.md  → Choix du modèle
📁 hermes/services/
   └── spotify.md               → Contrôle Spotify
📁 hermes/
   ├── interface-web.md         → Interface web Hermes
   └── architecture-communication.md  → Architecture & Communication
```

## Public visé

- **Débutant·e** — les pages d'installation vous guident pas à pas
- **Intermédiaire** — la configuration et les skills vous ouvrent les possibilités
- **Expert·e** — le troubleshooting et l'architecture LEO vous inspirent

## Licence

Ce guide est en licence libre — libre à vous de le partager, l'adapter et l'enrichir.

---

*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

> 🤖 Dernier audit : 26/07/2026 à 12:00 (UTC+2)

# Table des matières

## 📖 Hermès pour les Nuls

```
┌────────────────────────────────────────────────────────────┐
│  HERMÈS POUR LES NULS                                      │
│  Construire son propre assistant IA avec LEO              │
│                                                            │
│  Partie I  — Découvrir Hermès          🏁                  │
│  Partie II — Configurer son Assistant  ⚙️                  │
│  Partie III — Les Bureaux BAVI         🏛️                  │
│  Partie IV — La Puissance des Skills   🧠                  │
│  Partie V — Dashboards et Monitoring   📊                  │
│  Partie VI — Automatisation et Crons   ⏱️                  │
│  Partie VII — La Partie des Dix        💡                  │
│  Annexes                                📚                 │
└────────────────────────────────────────────────────────────┘
```

---

## Partie I — Découvrir Hermès 🏁
*Commencer par le commencement*

- ****Ch.1 — Un agent IA, c'est quoi ?****
  - Chatbot vs agent : la différence fondamentale
  - Ce que LEO fait que ChatGPT ne peut pas faire
  - Les briques d'un agent : modèle, outils, mémoire, actions

- ****Ch.2 — Pourquoi Hermès ?****
  - Hermes vs Claude Code vs Codex vs OpenCode
  - Multi-provider : DeepSeek, Gemini, Ollama, 15+ autres
  - Skills : le super-pouvoir qui rend Hermes unique
  - Plateformes : Telegram, Discord, Slack, email, et plus

- ****Ch.3 — L'architecture LEO****
  - Vue d'ensemble : 3 bots, 3 profils, providers dédiés
  - Le Gateway DeepSeek : pont entre Telegram et l'agent
  - Hiérarchie des providers : quand utiliser quoi
  - Les chiffres clés de LEO (dashboards, crons, skills)

- ****Ch.4 — Installation rapide****
  - Installation sur Linux (Debian/Ubuntu)
  - Installation sur Windows (WSL)
  - Premier lancement et configuration minimale
  - Vérification : le diagnostic

---

## Partie II — Configurer son Assistant ⚙️
*Moteur, on tourne !*

- ****Ch.5 — Le Gateway : connecter Telegram****
  - Créer un bot Telegram avec @BotFather
  - Configurer le gateway Hermes
  - Gérer les profils : default, michel, sylvia
  - La gestion s6 en environnement Docker

- ****Ch.6 — Providers : le moteur de votre agent****
  - DeepSeek : le pilier principal
  - Ollama : l'IA locale et gratuite
  - Gemini : le fallback silencieux
  - Hiérarchie et fallback : comment Hermes choisit

- ****Ch.7 — Multi-bots : pourquoi plusieurs valent mieux qu'un****
  - L'architecture multi-profil de LEO
  - Quand créer un nouveau bot vs tout dans le même
  - Synchronisation de mémoire entre profils
  - Gérer ses tokens et cred pools

- ****Ch.8 — Skills : le super-pouvoir d'Hermès****
  - Qu'est-ce qu'un skill ?
  - Les 28 skills de LEO : classification et navigation
  - Installer, charger, et utiliser des skills
  - Skills système vs skills utilisateur

- ****Ch.9 — Mémoire persistante****
  - Pourquoi un agent a besoin de mémoire
  - Memory vs User Profile
  - Configurer et utiliser la mémoire
  - Le cron sync-memory entre profils

---

## Partie III — Les Bureaux BAVI 🏛️
*La force de l'organisation*

- ****Ch.10 — Architecture bureaux****
  - Le concept BAVI : organiser ses connaissances par bureau
  - Les 10 bureaux : qui fait quoi
  - La gouvernance : comment les bureaux collaborent

- ****Ch.11 — Bureau Michel : l'infrastructure****
  - Déploiement et configuration des workflows
  - Gestion système, watchdogs, scripts
  - La checklist de déploiement

- ****Ch.12 — Bureau Sylvia : les voyages****
  - Le bot voyages dédié (@bavi_leo_voyages_bot)
  - Roadbooks et wiki voyages
  - Agence de voyage complète (camping-car, hôtels, itinéraires)

- ****Ch.13 — Bureau Emile : assistant professionnel d'Émilie****
  - Assistant professionnel dans My Émile IA Workbench (développé via Avenyra)
  - Rédaction, structuration et gestion documentaire avec validation humaine

- ****Ch.14 — Bureau Robert : le conseil stratégique****
  - Analyses concurrentielles
  - Recommandations stratégiques IT
  - Gouvernance et architectures cibles

- ****Ch.15 — Les autres bureaux****
  - Bureau Sophie : pilotage économique et financier
  - Bureau Gérard : astronomie, astrophotographie et documentation
  - Bureau Virginie : orchestration médicale
  - Bureau LEO : le fourre-tout personnel
  - Assurance Obligatoire : le bureau transverse

---

## Partie IV — La Puissance des Skills 🧠
*Le savoir-faire réutilisable*

- ****Ch.16 — Skills système****
  - hermes-agent, hermes-gateway, hermes-profiles
  - Configuration et troubleshooting
  - Les profils multi-agents

- ****Ch.17 — Skills productivité****
  - Dashboards : hermes-dashboard, dashboard-kpi
  - Documentation : mkdocs-wiki, living-documentation
  - Google Workspace, Airtable, Notion
  - Email : inbox-zero, leo-email-assistant

- ****Ch.18 — Skills DevOps****
  - GitHub PR workflow, code review, issues
  - Code-server VS Code dans le navigateur
  - Déploiement de dashboards

- ****Ch.19 — Skills créatifs****
  - ASCII art, architecture diagrams, Excalidraw
  - ComfyUI, p5.js, manim-video
  - Songwriting et musique IA

- ****Ch.20 — Skills recherche et veille****
  - AI Tech Watch : 17 sources RSS
  - arXiv, blogwatcher, Polymarket
  - Llm-wiki : base de connaissances LLM

- ****Ch.21 — Écrire ses propres skills****
  - Le format SKILL.md : frontmatter et contenu
  - Les bonnes pratiques
  - Versionner et partager ses skills

---

## Partie V — Dashboards et Monitoring 📊
*Voir l'invisible*

| ****Ch.22 — L'écosystème de dashboards****
|  - Architecture : 7 dashboards pré-crash → **1 dashboard unifié** (leo-dashboard)
|  - Navigation interconnectée
  - Cycle de vie d'une donnée : du chat Telegram au graphique

- ****Ch.23 — Métriques machines****
  - CPU, RAM, disque, GPU : collecte et visualisation
  - Les 3 machines de LEO : LEO, Yoga, Penguin
  - Alertes et seuils

- ****Ch.24 — Monitoring des crons****
  - Le tableau de bord des 25 tâches planifiées
  - Historique 7 jours, durée d'exécution, taux de succès
  - Détection des crons bloqués ou en échec

- ****Ch.25 — Budget et tracking****
  - Suivi du solde DeepSeek en temps réel
  - Projection de consommation
  - Dashboards LEO KPI et BAVI LEO KPI

---

## Partie VI — Automatisation et Crons ⏱️
*Que ça roule tout seul*

- ****Ch.26 — Le scheduler Hermes****
  - no_agent vs LLM-driven : quel mode pour quelle tâche ?
  - Script vs prompt : les critères de choix
  - Syntaxe cron, delivery, workdir

- ****Ch.27 — Les crons horaires****
  - La vague H:00-H:30 : 8 crons qui s'enchaînent
  - Machines KPI, budget, dashboards
  - Le staggered scheduling

- ****Ch.28 — Les crons quotidiens et spéciaux****
  - Backup automatique (06:00)
  - Veille IA (08:00)
  - Drive sync (18:00)
  - Classifieur emails (toutes les 15 min)
  - Auto-commit repos (toutes les 2h)

- ****Ch.29 — Watchdogs et alertes****
  - Dashboard Watch : vérification automatique du contenu
  - Auto-Heal : détection et correction des erreurs
  - Code-server watchdog
  - Le double filet : Hermes + scripts Python

- ****Ch.30 — Drive ↔ GitHub Sync****
  - Synchronisation bidirectionnelle Drive ↔ GitHub
  - Résolution de conflits
  - Le Drive Guardian en script Python

---

## Partie VII — La Partie des Dix 💡
*Les listes qui sauvent*

- ****Ch.31 — 10 astuces pour ne pas galérer****
  - Les pièges à éviter absolument
  - Astuces de configuration et d'usage quotidien

- ****Ch.32 — 10 commandes à connaître absolument****
  - Les essentiels du CLI Hermes
  - Commandes slash en session interactive

- ****Ch.33 — 10 façons d'étendre Hermès****
  - MCP servers, plugins, webhooks
  - Intégrations avec d'autres outils

- ****Ch.34 — 10 ressources pour aller plus loin****
  - Documentation officielle, skills hub, communauté

---

## Annexes 📚

- **[Annexe A — Glossaire](annexes/glossaire.md)**
- **[Annexe B — Guide de démarrage rapide](annexes/guide-rapide.md)**
- ****Annexe C — Arbre de décision des providers****
- ****Annexe D — Check-list déploiement****
- **[Annexe E — Aide-mémoire des commandes](annexes/commandes.md)**
- **[Annexe F — Exemple : architecture complète de LEO](annexes/exemple-leo-complet.md)**
- **[Annexe G — Troubleshooting](annexes/troubleshooting.md)**

---

**Légende :** 📝 = écrit | 🔄 = en cours | ⬜ = à rédiger
*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

> 🤖 Dernier audit : 26/07/2026 à 12:00 (UTC+2)

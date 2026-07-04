# 🌐 Interface Web Hermes Agent

Page mise à jour le **04/07/2026** — Documentation de l'interface utilisateur Hermes Agent v0.18.0.

---

## Accès

L'interface web Hermes Agent est accessible à l'adresse :

```
http://localhost:9119
```

Depuis l'extérieur (Tailscale) :

```
http://100.92.102.28:9119
```

---

## Navigation générale

La barre latérale gauche est organisée en sections :

- **Profil actif** : sélecteur de profil en haut (`default`, `leo-copilot`, `bavi-leo`, `emile`)
- **Navigation principale** : toutes les sections listées ci-dessous
- **Plugins** : extensions installées (Kanban, Achievements)
- **System** : statut du gateway, boutons Restart/Update, thème, langue

---

## Sections

### 💬 CHAT

Terminal de conversation interactif avec l'agent.

| Élément | Description |
|---------|-------------|
| **Zone de saisie** | Terminal input — tapez vos messages |
| **Modèle actif** | Affiche le modèle utilisé (ex: `deepseek-v4-flash`) |
| **Outils** | Liste des tool calls effectués pendant la session |
| **Copy last response** | Bouton pour copier la dernière réponse |

Permet de dialoguer directement avec Hermes depuis le navigateur, comme sur Telegram.

---

### 📋 SESSIONS

Gestionnaire de sessions de conversation.

| Fonctionnalité | Description |
|----------------|-------------|
| **Vue Overview** | Statistiques globales : total sessions, messages, sources (cron, telegram, cli, tui) |
| **Vue History** | Historique chronologique des sessions |
| **Recent Sessions** | Liste des dernières sessions avec horodatage, modèle, nombre de messages |
| **Prune old sessions** | Bouton pour nettoyer les vieilles sessions |
| **Filtre** | Par source (cron, telegram, cli, tui) |

---

### 📁 FILES

Gestionnaire de fichiers sur le serveur. Permet de :
- Parcourir les dossiers du serveur
- Télécharger / uploader des fichiers
- Visualiser le contenu

---

### 🤖 MODELS

Configuration et sélection des modèles LLM.

| Fonctionnalité | Description |
|----------------|-------------|
| **Liste des modèles** | Modèles disponibles par provider |
| **Provider** | DeepSeek, Ollama, Google/Gemini |
| **Sélection** | Choix du modèle par défaut pour le profil actif |

Permet de basculer entre modèles sans toucher au fichier de config.

---

### 📜 LOGS

Visualisation des journaux système.

- Logs en temps réel de l'agent Hermes
- Filtrage par niveau (info, warning, error)
- Horodatage précis

---

### ⏰ CRON

Gestion des tâches planifiées. **Section la plus utilisée pour LEO.**

| Fonctionnalité | Description |
|----------------|-------------|
| **Liste des jobs** | Jobs listés avec nom, statut, schedule, derniers/prochains runs |
| **CREATE** | Créer un nouveau job cron |
| **Trigger now** | Exécution immédiate d'un job |
| **Pause/Resume** | Activer/désactiver un job |
| **Edit job** | Modifier nom, prompt, schedule, skills, livraison |
| **Delete** | Supprimer un job |
| **Filtre par profil** | Voir les jobs d'un profil spécifique |
| **Blueprints** | Templates de jobs réutilisables |

Chaque job affiche :
- Statut (scheduled, running, paused)
- Profil associé
- Expression cron
- Dernière exécution
- Prochaine exécution

---

### 🧩 SKILLS

Gestion des compétences (skills) installées.

| Fonctionnalité | Description |
|----------------|-------------|
| **Liste des skills** | Skills installées, avec description |
| **Catégories** | Autonomous AI Agents, BAVI LEO, Creative, Email, GitHub, etc. |
| **Recherche** | Filtre par nom de skill |

---

### 🔌 PLUGINS

Extensions de l'agent Hermes.

Actuellement installés :
- **Kanban** — gestion de tâches visuelle
- **Achievements** — badges et réalisations

---

### 🔗 MCP

Model Context Protocol — outils et connecteurs externes.

Permet de configurer des outils MCP (serveurs externes, API) que l'agent peut utiliser.

---

### 📡 CHANNELS

Configuration des plateformes de messagerie connectées.

| Plateforme | Statut LEO |
|------------|:----------:|
| **Telegram** | ✅ Connecté (4 bots : default, leo-copilot, bavi-leo, emile) |
| **CLI** | ✅ Connecté |
| **Discord** | ❌ Non configuré |
| **Slack** | ❌ Non configuré |

Permet d'ajouter, configurer ou supprimer des canaux de communication.

---

### 🔗 WEBHOOKS

Gestion des webhooks entrants.

Permet de créer des endpoints HTTP que des services externes peuvent appeler pour déclencher des actions Hermes.

---

### 🔐 PAIRING

Appairage de dispositifs.

Permet de connecter des appareils supplémentaires (smartphones, tablettes) à l'agent Hermes via QR code ou code d'appairage.

---

### 👥 PROFILES

Gestion des profils Hermes.

| Profil | Modèle | Usage |
|--------|--------|-------|
| **default** | deepseek-v4-flash | Hub central — conversations, analyses, documentation |
| **leo-copilot** | deepseek-v4-pro | Infrastructure — crons, déploiements, maintenance |
| **bavi-leo** | deepseek-v4-flash | Bot voyages Telegram (Sylvia) |
| **emile** | deepseek-v4-flash | Assistant pédagogique |

Chaque profil a sa propre configuration : modèle, provider, skills, plugins, crons, gateway Telegram.

---

### ⚙️ CONFIG

Configuration YAML de l'agent (fichier `config.yaml`).

Affichage et édition en direct de la configuration Hermes.

---

### 🔑 KEYS

Gestion des clés API.

Visualisation et rotation des tokens :
- DeepSeek API key
- Google OAuth tokens
- GitHub token
- Autres providers LLM

---

### 🖥️ SYSTEM

Informations système et diagnostics.

| Métrique | Valeur (LEO) |
|----------|--------------|
| **Version Hermes** | v0.18.0 |
| **Python** | 3.13.5 |
| **OS** | Ubuntu 26.04 LTS |
| **Gateway** | Running |
| **Profils actifs** | 4 (default, leo-copilot, emile, bavi-leo) |

---

## Barre d'état système

Présente dans toutes les pages :

| Élément | Description |
|---------|-------------|
| **Gateway Status** | Running / Stopped |
| **Active Sessions** | Nombre de sessions en cours |
| **Restart Gateway** | Redémarrage du gateway |
| **Update Hermes** | Mise à jour de l'agent |
| **Theme** | HERMES TEAL (défaut) |
| **Language** | EN/FR |
| **Version** | v0.18.0 |

---

## Plugins

### 📋 KANBAN

Tableau Kanban pour la gestion de tâches. Permet de créer des cartes, les classer par colonnes (À faire, En cours, Fait) et suivre l'avancement.

### 🏆 ACHIEVEMENTS

Système de badges et réalisations. Débloque des succès en fonction de l'utilisation d'Hermes.

---

## Raccourcis

- **Switch theme** : bascule entre thème TEAL et sombre
- **Switch language** : bascule entre anglais et français
- **Collapse** : réduit la barre latérale pour plus d'espace

---

*Document mis à jour le 04/07/2026 — 00:00:00 — Modèles DeepSeek unifiés 🦁*

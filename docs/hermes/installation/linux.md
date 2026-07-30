# Installation sur Linux (Debian/Ubuntu)

## 🎯 Objectif

Ce guide vous permet d'installer Hermes Agent sur Linux. Deux approches :

| Méthode | Difficulté | Usage | Idéal pour |
|:--------|:-----------|:------|:-----------|
| **Directe** (officielle) | ⭐ Facile | Poste personnel, test | Débutants, usage individuel |
| **Docker** (conteneur) | ⭐⭐ Intermédiaire | Serveur 24/7, gateway | Usage serveur, production |

---

## 📦 Méthode 1 : Installation directe (officielle)

### 1. Prérequis

- **Python 3.11+**
- **Git**
- **Curl**
- Un compte chez un fournisseur LLM (DeepSeek, OpenAI, Anthropic…)

```bash
# Installer les dépendances système
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

### 2. Installer Hermes

```bash
# Méthode recommandée — script officiel
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Alternative : depuis les sources
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 3. Configuration

```bash
# Assistant de configuration
hermes setup

# Vérifier que tout est OK
hermes doctor
```

Le wizard vous guide pour :
- Choisir votre fournisseur LLM (DeepSeek, Ollama, OpenAI…)
- Configurer Telegram (optionnel)
- Créer votre profil

### 4. Connecter un LLM

**DeepSeek** (recommandé pour débuter) :
```bash
hermes config set DEEPSEEK_API_KEY "votre_clé"
hermes model
# → Choisir deepseek dans la liste
```

**Ollama** (local, gratuit) :
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:7b
hermes config set providers.custom.ollama.base_url "http://localhost:11434/v1"
```

### 5. Lancer

```bash
# Mode interactif
hermes

# Avec Telegram
hermes gateway start
```

---

## 🐳 Méthode 2 : Installation via Docker

### 1. Installer Docker

```bash
# Docker Engine
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# déconnexion/reconnexion
```

### 2. Lancer Hermes

```bash
# Méthode simple — tout-en-un
docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -e HERMES_UID=$(id -u) \
  -e HERMES_GID=$(id -g) \
  nousresearch/hermes-agent:latest
```

> ⚠️ **Important** : le conteneur utilise `network_mode: host` pour le gateway Telegram.
> Sur macOS/Windows, des adaptations de ports sont nécessaires.

### 3. Configuration initiale

```bash
# Entrer dans le conteneur pour configurer
docker exec -it hermes hermes setup
```

---

## 🔧 Exemple : LEO (serveur de production)

LEO est l'assistant personnel de Christophe. Il tourne sur un **serveur Linux** en conteneur Docker, accessible 24/7. Le serveur est équipé d'un processeur moderne avec mémoire suffisante pour l'inférence IA locale.

### Architecture du déploiement

LEO tourne via **systemd** (`hermes-dashboard.service`) qui lance `server.py` depuis `~/Projets_Dev/BAVI_LEO/`. Le serveur sert à la fois l'interface web (port 9119) et le wiki local (port 8765).

```mermaid
graph TB
    subgraph HOST["HOST — Ubuntu 26.04 LTS"]
        Ollama["Ollama :11434<br/>qwen2.5:7b"]
        subgraph Docker["Hermes (Docker)"]
            GW["5 profils Gateway<br/>default · michel · sylvia · emile · robert"]
            Crons["47 crons (tous actifs)"]
        end
    end
    
    Telegram["📱 Telegram"] -->|"5 bots"| GW
    GW -->|"déploie"| GH["GitHub Pages<br/>1 dashboard unifié"]
    GW -->|"utilise"| Google["Google APIs<br/>Drive · Gmail · Calendar · Sheets"]
    GW -->|"appelle"| Ollama
    null
```

### Services système

LEO utilise un service systemd unique :

```ini
# /home/tofdan/.config/systemd/user/hermes-dashboard.service
[Unit]
Description=LEO Dashboard Panel
After=network.target

[Service]
Type=simple
WorkingDirectory=/home/tofdan/Projets_Dev/BAVI_LEO
ExecStart=/usr/bin/python3 /home/tofdan/Projets_Dev/BAVI_LEO/server.py
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
```

Le service `server.py` gère à la fois :
- Le **dashboard web** (port 8765) — wiki local + interface
- Les **gateways Telegram** des 5 profils
- La **gestion des crons**

## Services connectés

| Service | Rôle | Connexion |
|:--------|:-----|:----------|
| **Ollama** | LLM local (qwen2.5:7b) | API `http://host:11434/v1` |
| **DeepSeek** | LLM principal (via Telegram) | Clé API |
| **Tailscale** | Réseau privé (VPN mesh) | IPs 100.x.x.x |

---

## Dépannage

| Problème | Solution |
|----------|----------|
| `ModuleNotFoundError` | Vérifier que le venv est activé (`source .venv/bin/activate`) |
| Permission docker | `sudo usermod -aG docker $USER` puis déconnexion/reconnexion |
| Port déjà utilisé | `docker stop hermes && docker rm hermes` puis relancer |
| Gateway ne démarre pas | Vérifier `~/.hermes/logs/gateway.log` |

## Ressources

- [Documentation officielle](https://hermes-agent.nousresearch.com/docs)
- [GitHub](https://github.com/NousResearch/hermes-agent)
- [Docker Hub](https://hub.docker.com/r/nousresearch/hermes-agent)
*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

> 🤖 Dernier audit : 30/07/2026 à 06:00 (UTC+2)

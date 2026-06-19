# ⚡ n8n — Automatisation Low-Code

**n8n** est un outil d'automatisation visuelle qui connecte vos services entre eux : email, bases de données, API, Slack, Telegram, Google Sheets, etc.

## 🎯 Objectif

Ce guide couvre l'installation de n8n sur Linux et Windows, avec l'exemple concret de LEO.

| Méthode | Difficulté | Usage | Idéal pour |
|:--------|:-----------|:------|:-----------|
| **npm** (global) | ⭐ Facile | Poste local, test rapide | Développeurs Node.js |
| **npx** (sans install) | ⭐ Facile | Test ponctuel | Découverte |
| **Docker** | ⭐⭐ Intermédiaire | Serveur 24/7 | Production |
| **Docker Compose** | ⭐⭐ Intermédiaire | Stack complète (+ Postgres) | Usage avancé |

---

## 📦 Méthode 1 : npm (installation globale)

### 1. Installer Node.js

```bash
# Linux (Debian/Ubuntu)
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs

# Vérifier
node --version   # v22+
npm --version
```

### 2. Installer n8n

```bash
npm install n8n -g
```

### 3. Lancer

```bash
# Mode développement (http://localhost:5678)
n8n start

# Mode production
N8N_SECURE_COOKIE=false n8n start
```

> Sur **Windows**, même commande dans PowerShell ou CMD.

---

## 🚀 Méthode 2 : npx (sans installation)

```bash
# Lancement direct sans installer
npx n8n

# Avec options
npx n8n start --tunnel
```

> Idéal pour découvrir n8n. Les données sont perdues à l'arrêt.

---

## 🐳 Méthode 3 : Docker (recommandé pour la production)

### 1. Installer Docker

```bash
# Linux
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# Déconnexion/reconnexion

# Windows → Docker Desktop
```

### 2. Lancer n8n

```bash
# Créer le volume de données
mkdir -p ~/n8n-data

# Lancer le conteneur
docker run -d \
  --name n8n \
  --restart unless-stopped \
  -p 5678:5678 \
  -v ~/n8n-data:/home/node/.n8n \
  -e N8N_SECURE_COOKIE=false \
  n8nio/n8n:latest
```

### 3. Accéder

Ouvrez `http://localhost:5678` dans votre navigateur.

---

## 🏗️ Méthode 4 : Docker Compose (stack complète)

```yaml
services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    restart: unless-stopped
    ports:
      - "5678:5678"
    volumes:
      - ./n8n-data:/home/node/.n8n
    environment:
      - N8N_SECURE_COOKIE=false
      - WEBHOOK_URL=https://votre-domaine.com:5678/
```

---

## 🔧 Exemple : LEO (serveur de production)

Sur LEO, n8n tourne en conteneur Docker aux côtés d'Hermes, exposé via Tailscale.

### Architecture

```
Internet (tailnet)
     │
     ▼
https://tofdan-system-product-name.tailbf5837.ts.net/
     │
     ├── /chat  → Hermes Dashboard (port 9119)
     └── /      → n8n              (port 5678)
```

### Installation sur LEO

```bash
# 1. Volume persistant
sudo mkdir -p /opt/n8n-data
sudo chown -R 1000:1000 /opt/n8n-data   # UID du conteneur n8n

# 2. Lancer le conteneur
sudo docker run -d \
  --name n8n \
  --restart unless-stopped \
  -p 5678:5678 \
  -v /opt/n8n-data:/home/node/.n8n \
  -e N8N_SECURE_COOKIE=false \
  -e WEBHOOK_URL=https://tofdan-system-product-name.tailbf5837.ts.net:5678/ \
  n8nio/n8n:latest

# 3. Exposer via Tailscale
sudo tailscale serve --bg --set-path=/ 5678
```

### Données persistantes

Tout est stocké dans `/opt/n8n-data/` sur le serveur :
- `database.sqlite` — workflows, credentials, historique
- `config` — clé de chiffrement
- `nodes/` — nœuds personnalisés
- `storage/` — fichiers et clés

### Mise à jour

```bash
docker pull n8nio/n8n:latest
docker rm -f n8n
# Réexécuter la commande docker run ci-dessus
```

---

## Premier démarrage

1. Ouvrez `http://localhost:5678` (ou l'URL Tailscale)
2. Créez votre **compte administrateur** (email + mot de passe)
3. Découvrez l'interface :
   - 📊 **Workflows** — créez vos automatisations visuelles
   - 🔗 **Credentials** — connectez vos services (Gmail, Sheets, etc.)
   - 📡 **Webhooks** — déclenchez des workflows depuis Hermes

## Idées de workflows

| Workflow | Déclencheur | Actions |
|:---------|:------------|:--------|
| 📬 Email important → Telegram | Webhook Hermes | Envoyer notification |
| 📊 Alerte métrique | Cron n8n | Email + notification |
| 🔄 Sync feuille de calcul | Modification sheet | Sauvegarde automatique |
| 🤖 Agent déclenché | Webhook entrant | Lancer Hermes sur une tâche |

## Ressources

- **Version installée :** 2.26.7
- **Site officiel :** [n8n.io](https://n8n.io/)
- **Documentation :** [docs.n8n.io](https://docs.n8n.io/)
- **Docker Hub :** [n8nio/n8n](https://hub.docker.com/r/n8nio/n8n)
- **Communauté :** [community.n8n.io](https://community.n8n.io/)

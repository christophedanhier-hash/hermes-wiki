# Installation sur Windows

## 🎯 Objectif

Hermes Agent est conçu pour Linux. Sur Windows, la méthode recommandée est **WSL 2** (sous-système Linux), qui offre ~95% des performances natives.

| Méthode | Difficulté | Usage |
|:--------|:-----------|:------|
| **WSL 2** (recommandé) | ⭐ Facile | Usage individuel, développement |
| **Docker Desktop** | ⭐⭐ Intermédiaire | Test, environnements isolés |

---

## 📦 Méthode 1 : WSL 2 (recommandée)

### 1. Installer WSL 2

Ouvrez **PowerShell en mode Administrateur** :

```powershell
# Installation complète
wsl --install

# Vérifier
wsl --status
wsl --list --verbose
```

> Cette commande installe WSL 2 + Ubuntu. Redémarrez si demandé.

### 2. Installer Hermes dans WSL

Ouvrez Ubuntu (menu Démarrer ou `wsl` dans PowerShell) :

```bash
# Dépendances système
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl

# Installation officielle
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
hermes setup
hermes doctor
```

### 4. Lancer Hermes

```powershell
# Depuis PowerShell/CMD
wsl
cd ~/hermes-agent
source .venv/bin/activate
hermes
```

💡 **Recommandation :** utilisez [**Windows Terminal**](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701) pour une meilleure expérience (onglets, couleurs, emojis).

### 5. (Optionnel) Ollama sur Windows

Ollama a une version Windows native :

1. Téléchargez depuis [ollama.com/download](https://ollama.com/download)
2. Installez et lancez
3. Dans WSL, configurez Hermes :

```bash
hermes config set providers.custom.ollama.base_url "http://host.docker.internal:11434/v1"
```

---

## 🐳 Méthode 2 : Docker Desktop

### 1. Installer Docker Desktop

Téléchargez depuis [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)

### 2. Lancer Hermes

```powershell
docker run -d ^
  --name hermes ^
  --restart unless-stopped ^
  -v %USERPROFILE%\.hermes:/opt/data ^
  nousresearch/hermes-agent:latest
```

> **Limitations** : pas de `network_mode: host` sur Windows → le gateway Telegram devra être configuré avec un port mapping explicite.

---

## 🔧 Exemple : LEO (serveur de production)

LEO tourne sur un serveur Linux 7.0.0-27-generic conteneurisé via Docker Compose.  
→ Voir [l'exemple LEO sur Linux](./linux.md)

Les principes sont identiques, seuls changent :
- Le gestionnaire de paquets : `apt` → `choco` / `winget` sur Windows
- Le réseau : `network_mode: host` → port mapping (`-p 9119:9119`)
- Les chemins : `~/.hermes` → `C:\Users\...\.hermes`

---

## Différences clés

| Aspect | Linux natif | WSL Windows | Docker Windows |
|--------|-------------|-------------|----------------|
| Performances | ✅ Optimal | ✅ ~95% | ⚠️ Léger overhead |
| GPU (Ollama) | ✅ Direct CUDA | ⚠️ CUDA dans WSL | ❌ Complexe |
| Démarrage | ✅ Systemd | 🔄 Manuel ou planifié | ✅ Auto |
| Réseau | ✅ Direct | ⚠️ `host.docker.internal` | ❌ Pas de host mode |

## Ressources

- [Installer WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install)
- [Windows Terminal](https://github.com/microsoft/terminal)
- [Ollama pour Windows](https://ollama.com/download)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

> 🤖 Dernier audit : 20 July 2026 à 09:14 (UTC+2)


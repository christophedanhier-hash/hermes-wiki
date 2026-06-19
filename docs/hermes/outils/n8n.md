# ⚡ n8n — Automatisation Low-Code

**n8n** est un outil d'automatisation visuelle qui connecte tes services entre eux. Installé sur LEO, il complète Hermes pour les tâches répétitives.

## Accès

| Méthode | URL | Accès |
|:--------|:----|:------|
| 🌐 **Tailnet** | `https://tofdan-system-product-name.tailbf5837.ts.net/` | Chromebook + app Tailscale |
| 🤖 **Dashboard Hermes** | `https://tofdan-system-product-name.tailbf5837.ts.net/chat` | Interface web Hermes |
| 🔒 **Local LEO** | `http://localhost:5678/` | Depuis LEO uniquement |
| 🐧 **Penguin** | `http://100.92.102.28:5678/` | Depuis Crostini |

**Login :** christophe.danhier@gmail.com

## Installation

n8n tourne dans un conteneur Docker sur LEO :

```bash
# Créer le volume de données
sudo mkdir -p /opt/n8n-data
sudo chown -R 1000:1000 /opt/n8n-data

# Lancer le conteneur
sudo docker run -d \
  --name n8n \
  --restart unless-stopped \
  -p 5678:5678 \
  -v /opt/n8n-data:/home/node/.n8n \
  -e N8N_SECURE_COOKIE=false \
  n8nio/n8n:latest
```

**Données persistantes :** `/opt/n8n-data/` sur le host LEO

## Configuration

### Exposition via Tailscale Serve

```bash
# Configurer les deux services
sudo tailscale serve --bg --set-path=/ n8n 5678
sudo tailscale serve --bg --set-path=/chat 9119
```

**Résultat :**
- `https://tofdan-system-product-name.tailbf5837.ts.net/` → n8n
- `https://tofdan-system-product-name.tailbf5837.ts.net/chat` → Dashboard Hermes

### Variables d'environnement

| Variable | Valeur | Rôle |
|:---------|:-------|:-----|
| `N8N_SECURE_COOKIE` | `false` | Permet l'accès HTTP (tailnet) |
| `WEBHOOK_URL` | `https://tofdan-system-product-name.tailbf5837.ts.net:5678/` | URL publique pour les webhooks |

## Utilisation avec Hermes

### Webhook Hermes → n8n

1. Dans n8n, crée un workflow avec un nœud **Webhook**
2. Configure la méthode POST et l'URL
3. Depuis Hermes, appelle ce webhook avec `curl` ou le tool `web`

**Exemple — alerte de métrique :**

```n8n
Webhook (POST) → If (condition) → Gmail (envoyer email)
                                 → Telegram (notification)
                                 → Google Sheets (logger)
```

### Webhook n8n → Hermes

1. Configure un **Webhook Hermes** via `hermes webhook subscribe`
2. n8n peut déclencher une action Hermes automatiquement

## Maintenance

```bash
# Voir les logs
docker logs n8n

# Redémarrer
docker restart n8n

# Mettre à jour
docker pull n8nio/n8n:latest
docker rm -f n8n
# ré-exécuter la commande docker run ci-dessus

# Surveiller les ressources
docker stats n8n --no-stream
```

## Idées de workflows

| Workflow | Déclencheur | Actions |
|:---------|:------------|:--------|
| 📬 **Email important → Telegram** | Nouveau email Gmail (label VIP) | Envoyer notification Telegram |
| 📊 **Alerte disque** | Webhook Hermes (métrique anormale) | Email + notification Telegram |
| 📅 **Rappel automatique** | Cron n8n (chaque jour à 9h) | Envoyer résumé du jour |
| 🔄 **Sync Google Sheets → Drive** | Modification sheet | Sauvegarde automatique |
| 🤖 **Agent déclenché** | Webhook entrant | Lancer Hermes sur une tâche |

## Ressources

- **Version installée :** 2.26.7
- **Site officiel :** [n8n.io](https://n8n.io/)
- **Documentation :** [docs.n8n.io](https://docs.n8n.io/)
- **Docker Hub :** [n8nio/n8n](https://hub.docker.com/r/n8nio/n8n)

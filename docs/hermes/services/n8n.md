# 🔧 n8n — Automatisation LEO

> **📦 ARCHIVE — Service retiré le 13/07/2026.** n8n Docker a été arrêté et supprimé. Les workflows (Drive→Issue, Gardien du Drive, Save Contacts) ont été migrés vers des crons Hermes no_agent. Cette page est conservée pour référence historique.

## 🌐 Historique

[n8n](https://n8n.io) (v2.26.8, Community Edition) était notre orchestrateur de workflows auto-hébergé. Il tournait **dans un conteneur Docker** (`docker.n8n.io/n8nio/n8n:latest`) et gérait les automatisations nécessitant des **intégrations natives** (Google Drive, GitHub).

> **Doctrine LEO (obsolète)** : ~~Hermes gère les scripts planifiés (crons no_agent), n8n gère les workflows événementiels et les intégrations complexes.~~ → Depuis le 13/07/2026, tout est géré par les crons Hermes.

---

## 🏗️ Architecture

*(Architecture obsolète : n8n a été retiré le 13/07/2026)*

### Accès

| Info | Valeur (obsolète) |
|:-----|:-------|
| URL locale | http://localhost:5678 *(service supprimé)* |
| URL Tailscale | http://100.92.102.28:5678 *(service supprimé)* |
| Email | leodanhieria@gmail.com *(non utilisé)* |
| Password | `~/Projets_Dev/.n8n_pass` *(fichier supprimé)* |
| Version | 2.26.8 *(retiré)* |
| Mode | Docker (conteneur supprimé) |

> **Note** : Le collecteur `collect-v2.py` utilise `localhost:5678` (corrigé le 04/07/2026, était `100.92.102.28:5678`).

---

## ⚡ Workflows (historique)

Les workflows suivants ont été migrés vers des crons Hermes no_agent le 13/07/2026 :
- Drive → Issue GitHub (ID : `KPoilIuXhkw0pjGU`)
- Gardien du Drive (ID : `aRNg1FQMfptLu9Wt`)
- Save Contacts to GitHub (ID : `G73KASTP4EyUneMX`)

---

## 📊 Monitoring (obsolète)

n8n étant retiré le 13/07/2026, les métriques associées ne sont plus collectées. La section n8n a été supprimée du leo-dashboard.

---

## 🛡️ Maintenance

| Tâche | Commande |
|:------|:---------|
| Vérifier le conteneur | `docker ps --filter name=n8n` |
| Voir les logs | `docker logs n8n --tail 50` |
| Healthcheck | `curl -s http://localhost:5678/healthz` |
| Refresh credentials | Login via API : `curl -X POST http://localhost:5678/rest/login` |

---

*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

---

> 🤖 Dernier audit : 20/07/2026 à 07:26 (UTC+2)



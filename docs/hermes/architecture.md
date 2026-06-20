## Architecture Système

### 1. Infrastructure
- **Host LEO** (i7-7700K, 22GB RAM, 457GB, Ubuntu 26.04)
- **Container Hermes** (Debian 13, Python 3.13, DeepSeek V4 Flash)
- **Interface Chromebook** (Telegram)
- **Ollama local** (qwen2.5:7b sur http://100.92.102.28:11434)

### 2. Budget API
- **Balance DeepSeek actuelle**: $31.25
- **Seuil alerte**: < $30
- **Seuil stop**: < $10
- **Routage**: Ollama (gratuit) → Gemini (fallback) → DeepSeek (payant)

### 3. Crons Actifs (18)
| Nom | Horaire | Description |
| --- | ------- | ----------- |
| daily-backup | `0 6 * * *` | Backup Drive quotidien (fichiers plats) |
| docs-update | `0 8 * * *` | Mise à jour hebdo wiki + guide + changelog (Ollama) |
| machines-kpi | `0 * * * *` | Métriques CPU/RAM/disque 3 machines → Sheet |
| budget-check-v6 | `5 * * * *` | Solde DeepSeek → Sheet Budget |
| dashboard-leo | `10 * * * *` | run-dashboard.sh |
| leo-metrics | `15 * * * *` | Métriques machines → dashboard HTML (GH Pages) |
| crons-dashboard | `20 * * * *` | Statut des 10 crons → dashboard HTML (GH Pages) |
| drive-sync | `0 18 * * *` | Sync Drive → hermes-christophe (bidirectionnel) |
| github-dashboard | `25 * * * *` | Activité GitHub repos → dashboard HTML (GH Pages) |
| wiki-sync | `30 * * * *` | Sync fichiers sources → Wiki MkDocs |
| wiki-oca-sync | `35 * * * *` | Sync fichiers Cowork Drive → wiki OCA + push |
| bavi-leo-dashboard | `every 60m` | run-bavi-leo-dashboard.sh |
| credentials-check | `0 9 * * 1` | check-credentia |

### 4. Dashboards
- **Crons**: https://christophedanhier-hash.github.io/crons-dashboard/
- **GitHub**: https://christophedanhier-hash.github.io/github-dashboard/
- **Machines**: https://christophedanhier-hash.github.io/dashboard-leo/
- **Wiki**: https://christophedanhier-hash.github.io/hermes-wiki/

### 5. Sessions & Utilisation
- **Total sessions**: 99
- **Total messages**: 5306
- **Sessions CLI**: 3
- **Sessions Telegram**: 70
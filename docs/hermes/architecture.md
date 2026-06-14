## 1. Infrastructure

### Host LEO
- **Spécifications**: i7-7700K, 22GB RAM, 457GB, Ubuntu 26.04

### Container Hermes
- **Système d'exploitation**: Debian 13
- **Interpréteur Python**: Python 3.13
- **Version DeepSeek**: V4 Flash

### Interface Chromebook
- **Plateforme**: Telegram

### Ollama Local
- **Modèle**: qwen2.5:7b
- **Adresse**: http://100.92.102.28:11434

## 2. Budget API

- **Balance DeepSeek actuelle**: $41.97
- **Seuil d'alerte**: < $30
- **Seuil de stop**: < $10
- **Routage**: Ollama (gratuit) → Gemini (fallback) → DeepSeek (payant)

## 3. Crons Actifs (10)

| Nom | Horaire | Description |
| --- | ------- | ----------- |
| daily-backup | `0 6 * * *` | Backup Drive quotidien (fichiers plats) |
| docs-update | `0 8 * * 1` | Mise à jour hebdo wiki + guide + changelog (Ollama) |
| machines-kpi | `0 * * * *` | Métriques CPU/RAM/disque 3 machines → Sheet |
| budget-check-v6 | `5 * * * *` | Solde DeepSeek → Sheet Budget |
| dashboard-deploy | `10 * * * *` | Sheet KPI → dashboard HTML (GH Pages) |
| leo-metrics | `15 * * * *` | Métriques machines → dashboard HTML (GH Pages) |
| crons-dashboard | `20 * * * *` | Statut des 10 crons → dashboard HTML (GH Pages) |
| drive-sync | `0 18 * * *` | Sync Drive → hermes-christophe (bidirectionnel) |
| github-dashboard | `25 * * * *` | Activité GitHub repos → dashboard HTML (GH Pages) |
| wiki-sync | `30 * * * *` | Sync fichiers sources → Wiki MkDocs |

## 4. Dashboards

- **Crons**: https://christophedanhier-hash.github.io/crons-dashboard/
- **GitHub**: https://christophedanhier-hash.github.io/github-dashboard/
- **Machines**: https://christophedanhier-hash.github.io/dashboard-leo/
- **Wiki**: https://christophedanhier-hash.github.io/hermes-wiki/

## 5. Sessions & Utilisation

- **Total sessions**: 41
- **Total messages**: 2965
- **Sessions cli**: 3
- **Sessions telegram**: 17
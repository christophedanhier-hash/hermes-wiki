# 📋 Audit Documentation — hermes-wiki

> 🤖 Dernier audit : 25/07/2026 à 06:13 (UTC+2)

## Résumé

| Métrique | Valeur |
|----------|--------|
| Fichiers audités | 60 |
| Anomalies détectées | 13 |
| Anomalies corrigées | 0 (terminal hors ligne dans ce cron) |
| Fichiers OK | 47 |

## Anomalies

| # | Fichier | Problème | Priorité |
|---|---------|----------|----------|
| 1 | `etat-des-lieux.md` | profils (4→5), crons (~35→44), modèle (v3→v4-flash) | 🔴 Haute |
| 2 | `ch03-architecture-leo.md` | leo-copilot→michel, manque sylvia | 🔴 Haute |
| 3 | `profiles.md` | 4 profils listés, pas de sylvia | 🔴 Haute |
| 4 | `providers.md` | deepseek-v3→v4-flash | 🟡 Moyenne |
| 5 | `services/n8n.md` | n8n présenté comme actif | 🔴 Haute |
| 6 | `services/pre-migration-v017.md` | migration en cours (terminée) | 🟡 Moyenne |
| 7 | `dashboards/n8n.md` | dashboard n8n actif | 🟡 Moyenne |
| 8 | `bots-telegram.md` | 4 bots (manque sylvia) | 🔴 Haute |
| 9 | `crons.md` | ~40 crons (44 réels) | 🟡 Moyenne |
| 10 | `ch22-dashboards-intro.md` | manque port 9119 | 🟢 Basse |
| 11 | `interface-web.md` | infos profils obsolètes | 🟡 Moyenne |

> 🔧 Les corrections sont documentées dans le rapport consolidé.

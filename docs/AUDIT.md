# 📝 AUDIT — hermes-wiki

> Dernier audit : 18/07/2026 à 08:45 (UTC+2) — correction massive 36 anomalies

## Résultat

| Pages auditées | Anomalies | Corrigées auto |
|:--------------:|:---------:|:--------------:|
| 55 fichiers | 36 (6 🔴 + 5 🟠 + 13 🟡 + 12 🟢) | 30 auto-fix |

## 🔴 Critiques corrigées (6/6)

- ✅ **configurer/ch05-gateway-profils.md** : "un seul profil" → "5 profils spécialisés, 1 mémoire unifiée"
- ✅ **decouvrir/ch03-architecture-leo.md** : +emile +bureau-robert dans le tableau des bots
- ✅ **utilisation/documentation-map.md** : 44→38 crons, 9→8 sources (n8n retiré)
- ✅ **interface-web.md** : +bureau-robert dans le sélecteur de profil
- ✅ **configurer/ch07-multi-bots.md** : "(et bientôt quatre)" supprimé, n8n→scripts Python

## 🟠 Majeures corrigées (5/5)

- ✅ **automatisation/ch28-crons-quotidiens.md** : 11→17 sources RSS
- ✅ **dashboards/ch25-budget-tracking.md** : prix DeepSeek Pro $1.50/$5.00→$0.435/$0.87, solde vs coût clarifié
- ✅ **dashboards/ch22-dashboards-intro.md** : 9→8 sources collect-v2
- ✅ **architecture.md** : tous les modèles listés, solde+coût distingués
- ✅ **etat-des-lieux.md** : 4→5 gateways

## 🟡 Modérées corrigées

- ✅ **dashboards/ch23-metriques-machines.md** : n8n retiré de docker ps, auto-heal→health-check
- ✅ **automatisation/ch29-watchdogs.md** : auto-heal marqué supprimé, n8n retiré partout
- ✅ **configurer/ch07-multi-bots.md** : Gemini 2.5→3.5 Flash
- ✅ **bureaux/ch11-bureau-michel.md** : n8n→scripts Python
- ✅ **utilisation/architecture-leo.md** : 9→8 sources, n8n retiré
- ✅ **utilisation/dashboards.md** : 9→8 sources
- ✅ **services/pre-migration-v017.md** : crons 38/38

## 🟢 Mineures corrigées

- ✅ **utilisation/bots-telegram.md** : @emile_bot→@Bureau_ia_emilie_bot
- ✅ **utilisation/backup-recovery.md** : 4→5 gateways
- ✅ **services/gestion-releases.md** : 3→5 gateways, +emile +robert
- ✅ **decisions/pourquoi-deepseek-pas-gemini.md** : diagramme +Robert, 22→38 crons

## Vérité terrain (18/07/2026)

- 5 profils, 5 bots Telegram
- 38 crons (leo-copilot exclusif)
- Dashboards : 1 unifié (leo-dashboard) + Hermes interne (9119)
- n8n : retiré le 13/07/2026 — tous les docs mis à jour
- 17 sources RSS (veille IA)
- Prix DeepSeek Pro : $0.435/$0.87 par 1M tokens

---

> 🤖 Dernier audit : 18/07/2026 à 08:45 (UTC+2) — correction massive 36 anomalies

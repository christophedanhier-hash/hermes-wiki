# 📋 AUDIT — Journal des corrections

> Dernier audit : 20/07/2026 à 06:13 (UTC+2) — 20 anomalies corrigées (28 patches)

## 20/07/2026 — Audit massif (regex + DeepSeek V4 Flash)

### 🔴 Erreurs factuelles corrigées (8)
- 3× journaux quotidiens : 36/37 crons → 39
- Rapport audit Michel : 38 crons → 39, 4 profils → 5, 4 gateways → 5
- BAVI pour les nuls : 4 profils → 5
- Prompts NotebookLM : 4 bots → 5
- Guide Hermes ch01 : deepseek-chat → deepseek-v4-pro
- État des lieux : 38 crons → 39

### 🟠 Obsolescences corrigées (12)
- 5× gemini-2.5-flash → gemini-3.5-flash (providers, multi-bots, install rapide, skills système)
- 6× n8n référencé comme actif/Docker → marqué retiré 13/07 (dashboards, skills catalogue, dashboards-intro)
- 1× skills.md : n8n service marqué retiré

### 📊 Stats
- **171 fichiers audités** (2 wikis)
- **47 fichiers avec patterns suspects** (regex pre-scan)
- **20 anomalies** (8 wrong + 12 outdated)
- **28 patches** appliqués
- **124 fichiers sans anomalie** (72% conformes)

---

*Journal maintenu automatiquement par le cron d'audit rédactionnel.*

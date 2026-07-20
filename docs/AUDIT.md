# 📋 AUDIT — Journal des corrections

> Dernier audit : 20/07/2026 à 00:50 (UTC+2) — 21 anomalies corrigées (21 patches)

## 20/07/2026 — Audit rédactionnel unifié (2 wikis, 1 passage)

### 🔴 Anomalies corrigées (21)

**Crons count 38→39** (5 fichiers) :
- architecture.md, profiles.md, ch05, ch03-architecture-leo.md, etat-des-lieux.md

**Chemins /opt/data/→~/.hermes/ ou ~/Projets_Dev/** (8 fichiers) :
- ch22-dashboards-intro.md, ch26-crons-intro.md, ch28-crons-quotidiens.md
- ch29-watchdogs.md, ch30-drive-github-sync.md, ch16-skills-systeme.md
- securite.md, ch11-bureau-michel.md

**Profils manquants** (2 fichiers) :
- backup-recovery.md, ch28-crons-quotidiens : ajout bureau-robert

**Artifacts n8n** (1 fichier) :
- BAVI_LEO crons.md : H5 n8n backup → leo-daily-maintenance

### 📊 Stats
- **171 fichiers audités** (2 wikis)
- **21 anomalies corrigées** (18 outdated + 2 missing + 1 minor)
- **21 patches** appliqués
- **150 fichiers sans anomalie** (88% conformes)
- **0 anomalies résiduelles**

### 🔍 Vérifications
- 5 profils Hermes : ✅ (default, leo-copilot, bavi-leo, emile, bureau-robert)
- 5 bots Telegram : ✅
- 39 crons : ✅ (tous dans leo-copilot, 0 ailleurs)
- Modèles : ✅ deepseek-v4-flash, fallback gemini-3.5-flash, ollama qwen2.5:7b
- n8n : ✅ retiré 13/07/2026, marqué dans tous les docs
- Ports dashboards : ✅ 8765 + 9119

---

*Journal maintenu automatiquement par le cron d'audit rédactionnel.*

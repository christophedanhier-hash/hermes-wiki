## 🤖 Audit Rédactionnel — 17/07/2026 à 22:17 (UTC+2)

> Audit complet par DeepSeek Chat · 156 fichiers (94 infra + 62 contenu) · Coût: $0.05

| Page | Section | Statut | Correction |
|------|---------|--------|------------|
| architecture.md | Container | ✅ fixed | Python 3.13→3.14 |
| architecture.md | Budget API | ✅ fixed | Routage Ollama→Gemini→DeepSeek corrigé en DeepSeek→Gemini→Ollama |
| architecture.md | Crons | ✅ fixed | 29→38 crons |
| etat-des-lieux.md | Header + Tableau | ✅ fixed | 39→38 crons (x3 occurrences) |
| skills/ch16-skills-systeme.md | Profils table | ✅ fixed | bavi-leo "Voyages"→"Bureaux BAVI", ajout bureau-robert |
| configuration/profiles.md | Vérification | ✅ ok | 5 profils, 5 bots, crons exclusifs leo-copilot |
| configuration/providers.md | Vérification | ✅ ok | qwen2.5:7b, fallback DeepSeek→Gemini→Ollama |
| automatisation/ch26-crons-intro.md | Vérification | ✅ ok | Watchdogs actifs, n8n déprécié |

### Vérité terrain (réf.)

| Élément | Valeur |
|---------|--------|
| Profils | 5 (bavi-leo, bureau-robert, default, emile, leo-copilot) |
| Bots Telegram | 5 |
| Crons actifs | 38 (tous leo-copilot, ZÉRO ailleurs) |
| Ollama | qwen2.5:7b |
| Fallback | DeepSeek → Gemini → Ollama |
| n8n | ❌ Retiré 13/07/2026 |
| Python | 3.14 |
| Ports | 8765, 9119, 11434, 7681, 8123 |

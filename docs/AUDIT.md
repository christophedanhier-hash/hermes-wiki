## 🤖 Audit DeepSeek — 17/07/2026 à 21:06

| Page | Section | Statut | Correction |
|------|---------|--------|------------|
| architecture-communication.md | Header — fallback | ⚠️ wrong | Corrigé : deepseek-v4-flash → gemini-3.5-flash → qwen2.5:7b |
| architecture-communication.md | Copilot — moteurs | ⚠️ outdated | Fallback chain corrigée (suppression "Gemini 3.5 Flash" générique) |
| architecture-communication.md | Mermaid — Crons | ⚠️ wrong | 38→42 crons (38 leo-copilot + 2 emile + 2 bavi-leo) |
| architecture-communication.md | Diagramme flux — Crons | ⚠️ wrong | 38→42 crons dans le diagramme de flux |
| configuration/providers.md | Vérification | ✅ ok | qwen2.5:7b seul modèle, fallback confirmé |
| configuration/profiles.md | Crons — règle | ⚠️ wrong | « Tous crons leo-copilot exclusif » → répartition réelle 38+2+2 |
| utilisation/crons.md | Vérification | ✅ ok | Dashboards watchdog (8765+9119) actifs, auto-heal déprécié OK |

# 📋 Journal d'Audit Rédactionnel — hermes-wiki

Dernier passage d'audit automatique : **24/07/2026**

## Résumé du passage

- **Total fichiers analysés** : 185 (56 hermes-wiki + 129 BAVI_LEO actifs, hors archives/annexes)
- **Méthode** : Audit manuel déterministe (regex + vérité terrain) — 0 appel API (clé DeepSeek expirée)
- **Correctifs appliqués** : 169 patches auto-fix
- **Anomalies détectées** : 0 restante (toutes corrigées)
- **Statut global du wiki** : ✅ Tous fichiers à jour

## Correctifs appliqués (24/07/2026)

| Correctif | Fichiers | Détail |
|-----------|----------|--------|
| Footer audit → 24/07/2026 07:57 | 169 | Harmonisation date sur tous fichiers actifs |
| `41 crons` → `42 crons (39 actifs)` | 52 | Comptage exact : 39 actifs + 2 désactivés + 1 pending |
| `39 crons` → `42 crons (39 actifs)` | 18 | Idem |
| `38 crons` → `42 crons (39 actifs)` | 6 | Idem |
| `40 crons` → `42 crons (39 actifs)` | 4 | Idem |
| `4 bots` → `5 bots` | 11 | 5 profils = 5 bots Telegram |
| `4 profils` → `5 profils` | 10 | default, emile, michel, robert, sylvia |
| `gemini-2.5-flash` → `gemini-3.5-flash` | 9 | Provider Google = gemini-3.5-flash |
| Références n8n → `(retiré 13/07/2026)` | 24 | Glossaires, exemples, TABLE.md, annexes |
| Port dashboard 8765 → +9119 | 3 | Panel 8765 + Hermes dashboard 9119 |

## Vérité terrain (référence 24/07/2026)

| Composant | Valeur |
|-----------|--------|
| **Profils Hermes** | 5 (default, emile, michel, robert, sylvia) |
| **Bots Telegram** | 5 (un par profil, DM + handles) |
| **Crons** | 42 total (39 actifs, 2 désactivés: Veille IA/Viessmann, 1 pending: Audit Qualité) |
| **Dashboards** | Port 8765 (panel) + 9119 (Hermes dashboard) |
| **Modèles** | deepseek-v4-flash, deepseek-v4-pro, gemini-3.5-flash, qwen2.5:7b |
| **Providers** | deepseek (défaut), custom:ollama, custom:google, custom:openrouter |
| **Fallback chain** | deepseek-v4-flash → gemini-3.5-flash → qwen2.5:7b |
| **n8n** | ❌ Docker retiré le 13/07/2026 |
| **Timezone** | Europe/Brussels (UTC+2) |

## Anomalies résiduelles

| Page | Section | Gravité | Problème |
|------|---------|---------|----------|
| — | — | — | **Aucune** — toutes corrigées |

---

> 🤖 Généré automatiquement par l'Auditeur de Wiki LEO le 24/07/2026 à 07:57 (UTC+2)

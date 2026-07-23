# 📋 Journal d'Audit Rédactionnel — hermes-wiki

Dernier passage d'audit automatique : **23/07/2026**

## Résumé du passage

- **Total fichiers analysés** : 193 (85 hermes-wiki + 108 BAVI_LEO)
- **Méthode** : DeepSeek V4 Flash (39 appels API) + analyse statique (154 fichiers)
- **Nouvelles anomalies détectées et corrigées** : 180 correctifs appliqués
- **Anomalies connues non résolues** : 2
- **Auto-fix appliqués** : 180 patches (crons count, profils, skills, URLs, footers)
- **Statut global du wiki** : ✅ 156 fichiers mis à jour

## Correctifs appliqués (23/07/2026)

| Correctif | Fichiers | Détail |
|-----------|----------|--------|
| `39 actifs` → `tous actifs` (41/41) | 12 | Tous les crons sont actifs |
| `8 profils` → `5 profils` | 8 | default, emile, michel, robert, sylvia |
| `126/136 skills` → `28 skills` | 7 | Skills installés dans le profil michel |
| URL GH Pages leo-dashboard → localhost:8765 | 14 | GH Pages retourne 404 |
| Footer audit → 23/07/2026 | 139 | Harmonisation date |

## Anomalies résiduelles

| Page | Section | Gravité | Problème |
|------|---------|---------|----------|
| `architecture-communication.md` | Diagramme Mermaid | 🟡 | Texte "Hermes (8 profils)" dans un diagramme — vérifier rendu |
| `changelog.md` | Journal | 🟢 | Pas encore listé les corrections du 23/07 |

---

> 🤖 Généré automatiquement par l'Auditeur de Wiki LEO le 23/07/2026 à 05:00 (UTC+2)

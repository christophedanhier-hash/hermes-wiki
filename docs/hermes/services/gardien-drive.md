# 🧠 Gardien du Drive — Workflow n8n

> Classification automatique Google Drive via Ollama qwen2.5:7b local. **Coût : 0 €.**

---

## Architecture

```
⏰ Schedule (toutes les heures)
  │
  └─ 🧠 Code Node (Gardien du Drive)
       │
       ├─ 🔐 Refresh token Google OAuth
       ├─ 🔍 PHASE 1 : Détection des doublons
       ├─ 📥 PHASE 2 : Inbox → Classement
       ├─ 📦 PHASE 2.5 : Archives → Reclasser ou 100-Corbeille
       ├─ 🗑️ PHASE 3 : Obsolètes → Corbeille
       └─ 🩺 PHASE 4 : Rapport de santé
```

---

## Les 5 phases

### 🔍 Phase 1 — Doublons
Détecte les fichiers en double dans tout le Drive. Rapport uniquement.

### 📥 Phase 2 — Inbox + Racine
Surveille `📥 À classer` et la racine du Drive. Ollama classe → déplace automatiquement.

### 📦 Phase 2.5 — Archives (deep scan)
Analyse les dossiers `99_ARCHIVES` et `Archives` :
- Si Ollama trouve un dossier pertinent → **reclassé**
- Sinon → déplacé dans **`100 - Corbeille`** (révision manuelle)

### 🗑️ Phase 3 — Obsolètes
Fichiers > 3 mois non modifiés → `🗑️ Corbeille Drive` (max 10/run).

### 🩺 Phase 4 — Santé
Résumé global : doublons, inbox, archives, conseils.

---

## Dossiers gérés

| Dossier | Rôle | Action |
|:---|:---|:---|
| **📥 À classer** | Dépôt des fichiers à classer | Classement auto |
| **99_ARCHIVES** | Archives à trier | Reclasser ou → 100-Corbeille |
| **Archives** | Archives générales | Reclasser ou → 100-Corbeille |
| **100 - Corbeille** | Révision manuelle avant suppression | À vérifier régulièrement |
| **🗑️ Corbeille Drive** | Fichiers obsolètes auto | À vérifier + supprimer |
| **📚 Backups** | Librairie EPUB Calibre | 🛡️ Zone protégée |

---

## Technique

| Propriété | Valeur |
|:---|:---|
| Workflow | `🧠 Gardien du Drive` (ID: `sTly8jZ2dHWcJQ3w`) |
| Déclencheur | Toutes les heures |
| LLM | Ollama qwen2.5:7b (LEO, port 11434) |
| API | Google Drive v3 (OAuth leodanhieria) |
| Coût | **0 €** |

---

*Document créé le 24/06/2026 — LEO 🦁*

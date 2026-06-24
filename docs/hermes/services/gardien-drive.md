# 🧠 Gardien du Drive — Workflow n8n

> Classification automatique des fichiers Google Drive via Ollama local (qwen2.5:7b). **Coût : 0 €.**

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
       ├─ 🗑️ PHASE 3 : Obsolètes → Corbeille
       └─ 🩺 PHASE 4 : Rapport de santé
```

---

## Les 4 phases

### 🔍 Phase 1 — Doublons
Détecte les fichiers en double (même nom) dans tout le Drive. Rapport uniquement — pas de suppression automatique.

### 📥 Phase 2 — Inbox → Classement
Surveille 2 sources :
- **📥 À classer** : dossier où tu déposes les fichiers à classer
- **Racine du Drive** : fichiers déposés directement à la racine

Ollama analyse le nom + type → choisit le dossier cible → déplace automatiquement.

### 🗑️ Phase 3 — Obsolètes → Corbeille
Détecte les fichiers non modifiés depuis **3 mois** → les déplace dans `🗑️ Corbeille Drive` (max 10 par run).
**Suppression manuelle** : tu vérifies la corbeille et supprimes ce qui est bon à jeter.

### 🩺 Phase 4 — Rapport de santé
Résumé global : nombre de fichiers, doublons, inbox en attente, conseils.

---

## Dossiers créés

| Dossier | Rôle |
|:---|:---|
| **📥 À classer** | Déposes-y les fichiers → classés automatiquement |
| **🗑️ Corbeille Drive** | Fichiers obsolètes → à vérifier avant suppression |

---

## Technique

| Propriété | Valeur |
|:---|:---|
| Workflow n8n | `🧠 Gardien du Drive` (ID: `sTly8jZ2dHWcJQ3w`) |
| Déclencheur | Schedule — toutes les heures |
| LLM | Ollama qwen2.5:7b (local, LEO) |
| API Google | Drive v3 (token OAuth leodanhieria) |
| Timeout | 300 secondes |
| Coût | **0 €** |

---

## Utilisation

1. Dépose un fichier dans **📥 À classer** (ou à la racine du Drive)
2. Dans l'heure qui suit, le workflow le classe automatiquement
3. Vérifie régulièrement **🗑️ Corbeille Drive** et supprime ce qui doit l'être

## 🛡️ Zones protégées (jamais touchées)

| Dossier | Contenu | Protection |
|:---|:---|:---|
| **Backups** | 📚 Librairie EPUB Calibre (livres français) + backups LEO | Aucune action automatique |

---

*Document créé le 24/06/2026 — LEO 🦁*

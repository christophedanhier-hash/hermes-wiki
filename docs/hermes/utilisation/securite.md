# 🛡️ Sécurité — Bonnes pratiques documentaires

> **Règle d'or** : tout ce qui est publié sur GitHub Pages est **public**. Un attaquant potentiel lit aussi le wiki.

## 🔴 Données à NE JAMAIS publier

| Donnée | Risque | Alternative |
|--------|--------|------------|
| **Mots de passe, tokens, clés API** | Accès direct aux services | Variables d'environnement (`.env`), vault |
| **IDs et mots de passe AnyDesk/TeamViewer** | Accès remote desktop complet | "À demander au responsable" |
| **Adresse personnelle, GSM** | Doxing, harcèlement | `[coordonnées privées]` |
| **Emails personnels** | Spam ciblé, phishing | Comptes dédiés si nécessaire |
| **Modèle exact CPU, RAM, kernel** | Ciblage d'exploit connu | "Processeur récent", "RAM suffisante" |
| **Version exacte des logiciels** | CVE connue → attaque ciblée | "Version récente" |
| **IP publiques, noms de domaine** | Attaque directe | `[serveur]` |
| **Structure interne (ports, services)** | Préparation d'attaque | Décrire l'architecture sans les détails |

## 🟡 Ce qui peut être publié avec précautions

| Donnée | Précautions |
|--------|-------------|
| Architecture générale (profils, bots) | OK — c'est la valeur pédagogique du wiki |
| Noms de modèles LLM, providers | OK — information publique |
| Workflows, processus métier | OK — sans tokens ni URLs internes |
| Statistiques d'usage (sessions, messages) | OK — sans données personnelles |

## 📋 Checklist avant publication

- [ ] Pas de mot de passe, token ou clé API en clair
- [ ] Pas d'adresse personnelle, GSM ou email privé
- [ ] Pas de version exacte de logiciel ou modèle CPU
- [ ] Pas d'IP publique ou URL d'accès interne
- [ ] Les mots de passe AnyDesk/SSH sont remplacés par "À demander"
- [ ] Les signatures utilisent `[coordonnées privées]` au lieu des vraies

## 🔍 Vérification automatique

Le script `doc-security-scan.py` peut être exécuté pour scanner tout le wiki à la recherche de patterns sensibles :

```bash
python3 ~/.hermes/profiles/leo-copilot/scripts/doc-security-scan.py
```

Patterns recherchés : `mot de passe`, `password`, `token`, `-----BEGIN`, `anydesk`, `teamviewer`, `192.168\.`, r`[0-9]{3,4}\.[0-9]{3,4}\.[0-9]{4}` (GSM), etc.

---

*Document créé le 07/07/2026 — Léo 🦁*

---

> 🤖 Dernier audit : 22 July 2026 à 09:00 (UTC+2)



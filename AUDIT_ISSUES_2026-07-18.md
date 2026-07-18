# 🔍 AUDIT hermes-wiki — Écarts vs Réalité Infrastructure LEO

**Date audit** : 18/07/2026  
**Fichiers audités** : 55  
**Réalité terrain** : profils=5, bots=5, crons=38, n8n=❌ retiré 13/07/2026  

---

## 🔴 CRITIQUES — Données factuellement fausses

### 1. `configuration/profiles.md` (L46)
- **Doc dit** : `Crons : 39 dans leo-copilot`
- **Réalité** : **38 crons** dans leo-copilot
- **Fix** : Remplacer 39 → 38

### 2. `configurer/ch05-gateway-profils.md` (L31-34)
- **Doc dit** : `Règle LEO : un seul profil — « Un seul profil, un seul gateway, tout dedans. »`
- **Réalité** : **5 profils** (default, leo-copilot, bavi-leo, emile, bureau-robert). Ce chapitre contredit totalement l'architecture multi-profils documentée partout ailleurs.
- **Fix** : Remplacer par la règle réelle : "5 profils spécialisés, 1 mémoire unifiée"

### 3. `decouvrir/ch03-architecture-leo.md` (L23-28)
- **Doc dit** : Table des bots ne montre que **3 bots** (leo, leo-copilot, bavi-leo) alors que le titre dit "5 bots Telegram"
- **Réalité** : **5 bots** — manquent `emile` et `bureau-robert`
- **Fix** : Ajouter emile + bureau-robert dans le tableau

### 4. `utilisation/documentation-map.md` (L15)
- **Doc dit** : `44 crons (38 leo-copilot + 2 emile + 2 bavi-leo + 6 hôte)`
- **Réalité** : **38 crons actifs** au total
- **Fix** : Corriger à 38 (vérifier si emile/bavi-leo/hôte ont vraiment des crons)

### 5. `interface-web.md` (L27)
- **Doc dit** : Sélecteur de profil : `default, leo-copilot, bavi-leo, emile`
- **Réalité** : **5 profils** — manque `bureau-robert`
- **Fix** : Ajouter bureau-robert

### 6. `configurer/ch07-multi-bots.md` (L3)
- **Doc dit** : `cinq bots spécialisés (et bientôt quatre)`
- **Réalité** : 5 bots, et la parenthèse "(et bientôt quatre)" suggère une réduction qui n'a pas eu lieu
- **Fix** : Supprimer `(et bientôt quatre)`

---

## 🟠 MAJEURES — Incohérences entre documents

### 7. Nombre de sources RSS (Veille IA)
| Fichier | Nb sources |
|---------|-----------|
| `automatisation/ch28-crons-quotidiens.md` (L17) | **11** sources |
| `skills/ch20-skills-recherche.md` (L24) | **15** sources |
| `decouvrir/ch01-cest-quoi-un-agent.md` (L62) | **17** sources |
- **Réalité** : 17 sources (selon contexte)
- **Fix** : Uniformiser à 17

### 8. Prix DeepSeek Pro (IN/OUT par 1M tokens)
| Fichier | Input | Output |
|---------|-------|--------|
| `decisions/pourquoi-deepseek-pas-gemini.md` (L21) | **$0.435** | **$0.87** |
| `dashboards/ch25-budget-tracking.md` (L62) | **$1.50** | **$5.00** |
- **Réalité** : $0.435/$0.87 (source api-docs.deepseek.com juillet 2026)
- **Fix** : Corriger budget-tracking.md

### 9. Nombre de dashboards
| Fichier | Nb dashboards |
|---------|--------------|
| `dashboards/ch22-dashboards-intro.md` (L21) | **1** dashboard unifié |
| `utilisation/architecture-leo.md` (L5) | **5** dashboards GitHub Pages |
| `architecture.md` (L34) | **4** (crons, github, machines, wiki) |
- **Réalité** : 1 dashboard unifié (leo-dashboard) + dashboard Hermes (port 9119)
- **Fix** : Uniformiser à 1 dashboard principal + dashboard Hermes interne

### 10. Nombre de skills
| Fichier | Nb skills |
|---------|----------|
| `etat-des-lieux.md` (L31) | **126** |
| `etat-des-lieux.md` (L70) | **105** (dans la section détaillée) |
| `configurer/ch08-skills.md` (L42) | **126** |
| `utilisation/skills-catalogue.md` (L4) | **103** (daté 19/06/2026) |
| `bureaux/ch15-bureau-leo.md` (L25) | **112** |
- **Réalité** : ~126 skills
- **Fix** : Uniformiser à 126 et mettre à jour les sections détaillées

### 11. Solde DeepSeek
| Fichier | Solde |
|---------|-------|
| `architecture.md` (L10) | **$41.83** |
| `configurer/ch09-memoire.md` (L17) | **$60.31** |
| `dashboards/ch25-budget-tracking.md` (L15) | **~$19.97** (coût réel) |
| `decisions/pourquoi-deepseek-pas-gemini.md` (L30) | **~1.50 USD/jour** |
- **Réalité** : $41.83 balance, ~$19.97 coût total
- **Fix** : Distinguer clairement "solde actuel" vs "coût cumulé" et uniformiser

---

## 🟡 MODÉRÉES — Références à n8n/Docker non nettoyées

### 12. `dashboards/ch23-metriques-machines.md` (L52)
- **Doc dit** : `docker ps → hermes-agent, n8n, ollama : tous UP`
- **Réalité** : n8n retiré — ne doit plus apparaître comme service UP
- **Fix** : `docker ps → hermes-agent, ollama : tous UP`

### 13. `dashboards/ch23-metriques-machines.md` (L80)
- **Doc dit** : `L'auto-heal détecte ces seuils toutes les 30 minutes`
- **Réalité** : Auto-heal supprimé le 04/07/2026 (selon ch29-watchdogs.md L49)
- **Fix** : Remplacer par le mécanisme actuel (health-check ou dashboard-watch)

### 14. `automatisation/ch29-watchdogs.md` (L30 vs L49)
- L30 dit : `Toutes les 30 minutes: Auto-heal complet`
- L49 dit : `Auto-Heal supprimé le 04/07/2026`
- **Contradiction interne** dans le même fichier
- **Fix** : Supprimer la ligne 30 ou la marquer comme obsolète

### 15. `automatisation/ch29-watchdogs.md` (L53)
- **Doc dit** : `n8n: healthz 200 ?` dans la checklist auto-heal
- **Réalité** : n8n retiré
- **Fix** : Supprimer la ligne n8n

### 16. `automatisation/ch29-watchdogs.md` (L70)
- **Doc dit** : Vérifie dashboards incluant `n8n`
- **Réalité** : Dashboard n8n archivé
- **Fix** : Retirer n8n de la liste des dashboards

### 17. `configurer/ch07-multi-bots.md` (L26)
- **Doc dit** : `Léo Copilote: crons, dashboards, n8n, budget, système`
- **Réalité** : n8n retiré
- **Fix** : Remplacer n8n par "scripts Python (ex-n8n)"

### 18. `bureaux/ch11-bureau-michel.md` (L3)
- **Doc dit** : `gère tout ce qui touche au fonctionnement de l'infrastructure : crons, dashboards, n8n...`
- **Réalité** : n8n retiré
- **Fix** : Remplacer n8n par "scripts Python"

### 19. `utilisation/architecture-leo.md` (L66)
- **Doc dit** : `5. n8n — workflows et exécutions` comme source de collect-v2
- **Réalité** : n8n retiré, collect-v2.py a 8 sources (pas 9)
- **Fix** : Retirer la source n8n, ajuster le compteur à 8

### 20. `dashboards/ch22-dashboards-intro.md` (L21) — "9 sources"
- **Doc dit** : `collect-v2.py (9 sources)`
- **Réalité** : 8 sources (n8n retiré)
- **Fix** : 9 → 8

### 21. `utilisation/dashboards.md` (L21) — "9 sources"
- Même problème que ci-dessus
- **Fix** : 9 → 8

### 22. `services/pre-migration-v017.md` (L15-16)
- **Doc dit** : `Crons leo-copilot: 1/1` et `Crons default: 29/29`
- **Réalité** : 38 crons dans leo-copilot, 0 ailleurs
- **Fix** : Mettre à jour (document historique, mais devrait refléter l'état pré-migration correct)

---

## 🟢 MINEURES — Détails à corriger

### 23. `utilisation/bots-telegram.md` (L18)
- **Doc dit** : `👤 @emile_bot`
- **Réalité** : `@Bureau_ia_emilie_bot` (selon ch13-bureau-emile.md L33)
- **Fix** : Corriger le nom du bot

### 24. `configurer/ch07-multi-bots.md` (L36)
- **Doc dit** : `Fallback: Gemini 2.5 Flash`
- **Réalité** : Gemini **3.5** Flash
- **Fix** : 2.5 → 3.5

### 25. `etat-des-lieux.md` (L27)
- **Doc dit** : `Gateways: 4 actifs`
- **Réalité** : 5 gateways (default, leo-copilot, bavi-leo, emile, bureau-robert)
- **Fix** : 4 → 5

### 26. `etat-des-lieux.md` (L25)
- **Doc dit** : `Docker: 2 conteneurs (hermes-agent + ollama)`
- **Réalité** : hermes-agent + ollama ; code-server est mentionné ailleurs (ch11 L55) — à vérifier
- **Fix** : Vérifier si code-server tourne encore

### 27. `services/gestion-releases.md` (L47, L55)
- L47 : `gateways default + leo-copilot + bavi-leo` → manquent emile et bureau-robert
- L55 : `3 gateways UP` → devrait être 5
- **Fix** : Mettre à jour les checklists

### 28. `utilisation/backup-recovery.md` (L14)
- **Doc dit** : `Redémarrage des 4 gateways`
- **Réalité** : 5 gateways
- **Fix** : 4 → 5

### 29. `architecture.md` (L7)
- **Doc dit** : `Model AI: Ollama qwen2.5:7b` (comme SEUL modèle listé)
- **Réalité** : 4 modèles (qwen2.5:7b, deepseek-v4-flash, deepseek-v4-pro, gemini-3.5-flash)
- **Fix** : Lister tous les modèles ou renvoyer vers providers.md

### 30. `architecture.md` (L14) — Table des crons
- N'affiche que **14 crons** sur 38 — table incomplète
- **Fix** : Soit lister les 38, soit renvoyer vers la doc crons dédiée

### 31. `dashboards/ch23-metriques-machines.md` (L44)
- **Doc dit** : `nvidia-smi → Aucun (CPU), 8 Go VRAM`
- **Réalité** : RTX 3050 avec 8 Go — le GPU existe mais est décrit comme "pas de GPU (CPU)" dans ch11-bureau-michel.md L43
- **Fix** : Clarifier si le GPU est utilisé ou pas

### 32. `utilisation/skills-catalogue.md` (L3)
- **Doc dit** : `Document généré le : 19/06/2026`
- **Réalité** : Document non mis à jour depuis presque 1 mois
- **Fix** : Mettre à jour la date

---

## 📊 RÉSUMÉ

| Sévérité | Nombre | Fichiers concernés |
|----------|--------|-------------------|
| 🔴 Critique | 6 | profiles.md, ch05-gateway-profils.md, ch03-architecture-leo.md, documentation-map.md, interface-web.md, ch07-multi-bots.md |
| 🟠 Majeure | 5 | ch28-crons-quotidiens, budget-tracking, ch22-dashboards-intro, divers skills, divers budget |
| 🟡 Modérée | 13 | ch23-metriques-machines, ch29-watchdogs, ch07-multi-bots, ch11-bureau-michel, architecture-leo.md, dashboards-intro, dashboards.md, pre-migration-v017, pourquoi-deepseek-pas-gemini (×2), documentation-map (×2) |
| 🟢 Mineure | 10 | bots-telegram, ch07-multi-bots, etat-des-lieux, gestion-releases, backup-recovery, architecture.md, skills-catalogue |

**Total issues** : **36**

### Issues additionnelles découvertes en analyse approfondie

33. `decisions/pourquoi-deepseek-pas-gemini.md` (L138-139) — Diagramme Mermaid
    - **Doc dit** : 4 bots (LEO, Copilot, BAVI, Émile) — **manque bureau-robert**
    - **Fix** : Ajouter bureau-robert dans le diagramme

34. `decisions/pourquoi-deepseek-pas-gemini.md` (L184)
    - **Doc dit** : `Crons quotidiens (22 jobs)`
    - **Réalité** : **38 crons**
    - **Fix** : 22 → 38

35. `utilisation/documentation-map.md` (L94)
    - **Doc dit** : `leo-dashboard, 9 sources`
    - **Réalité** : **8 sources** (n8n retiré)
    - **Fix** : 9 → 8

36. `utilisation/documentation-map.md` (L98)
    - **Doc dit** : `44 crons, planification`
    - **Réalité** : **38 crons**
    - **Fix** : 44 → 38

### Top 5 à corriger en priorité
1. `configurer/ch05-gateway-profils.md` — Contredit l'architecture 5 profils (règle "un seul profil")
2. `configuration/profiles.md` — 39 crons au lieu de 38
3. `decouvrir/ch03-architecture-leo.md` — Table des bots incomplète (3/5)
4. `utilisation/documentation-map.md` — 44 crons au lieu de 38
5. `interface-web.md` — 4 profils au lieu de 5

### Fichiers SANS issue
Parmi les 55 fichiers, **23 fichiers** sont conformes ou ne présentent que des imprécisions négligeables : ch26-crons-intro, ch30-drive-github-sync, ch10-architecture-bureaux, ch12-bureau-sylvia, ch13-bureau-emile, ch14-bureau-robert, ch15-bureau-leo, ch06-providers, ch08-skills, ch09-memoire, ch25-budget-tracking (détail prix déjà capturé), dashboards/n8n.md (archivé), ch01-cest-quoi-un-agent, ch02-pourquoi-hermes, ch04-installation-*, installation/linux.md, installation/windows.md, services/gardien-drive.md (archivé), services/n8n.md (archivé), services/spotify.md, ch16-skills-systeme, ch19-skills-creatifs, ch21-ecrire-ses-skills, quotidien.md, securite.md, index.md (portail), docs/index.md.

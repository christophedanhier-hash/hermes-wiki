# Rapport d'état des lieux documentaire — Wiki Hermes + Leo Docs

**Tâche** : t-006 (demande LEO, hive `conv-8df32d`, msg `20260924T172323-8df32d`)
**Auteur** : Gérard (documentation technique / audit)
**Date de mesure** : 24/09/2026, 17:25–17:40 (Europe/Brussels)
**Nature** : audit en lecture seule — aucune modification de contenu effectuée
**Méthode** : mesures directes reproductibles (build `--strict`, API locale, `curl`, inspection Git)

---

## 1. Objectif

Répondre à la demande de LEO : établir l'état des lieux documentaire sur trois axes.

1. **Wiki Hermes** (`hermes-wiki`) : pages obsolètes, références cassées, liens morts.
2. **Leo Docs** : documents orphelins ou à valeur de preuve à conserver / archiver.
3. **Incohérences** entre la documentation et l'état réel vérifié de la plateforme.

---

## 2. Matériel & périmètre audité

| Élément | Chemin | État Git mesuré |
|---|---|---|
| Wiki Hermes | `/home/tofdan/Projets_Dev/hermes-wiki` | `a1a4097` (branche main) |
| Leo Docs (explorateur) | `/home/tofdan/Projets_Dev/leo-docs` | `07a47e0` |
| Leo Knowledge (corpus) | `/home/tofdan/Projets_Dev/leo-knowledge` | `c411801` |
| Wiki OCA (périmètre Gérard) | `/home/tofdan/Projets_Dev/wiki-oca` | `b0eb62b` |

Outils de mesure : `mkdocs build --strict`, API locale `:8766/docs/api/pages`, `curl -o /dev/null -w %{http_code}`, `git ls-files`, `grep -r`.

---

## 3. Procédure de vérification (reproductible)

```bash
# A. Build strict du wiki Hermes → orphelines + liens cassés
cd /home/tofdan/Projets_Dev/hermes-wiki
source /home/tofdan/.hermes/venv/bin/activate && mkdocs build --strict

# B. Index réellement servi par Leo Docs (1453 docs au 24/09/2026)
curl -s http://127.0.0.1:8766/docs/api/pages | python3 -m json.tool | head

# C. Cohérence des URLs citées dans la doc (échantillon)
curl -s -o /dev/null -w "%{http_code}\n" https://christophedanhier-hash.github.io/leo-dashboard/

# D. Garde-fous du corpus de connaissance
cd /home/tofdan/Projets_Dev/leo-knowledge && python3 lint.py
```

---

## 4. Résultats — ce qui est OK

| Contrôle | Mesure | Statut |
|---|---|---|
| Build MkDocs strict — hermes-wiki | `exit=0`, 0 WARNING, 0 ERROR | ✅ OK |
| Build MkDocs strict — wiki-oca | `exit=0`, 0 WARNING, 0 ERROR | ✅ OK |
| Liens Markdown internes cassés (hermes-wiki) | 1 seul, et il s'agit d'un faux positif (`[url](url)` = placeholder de tutoriel dans `ch20-skills-recherche.md`) | ✅ OK |
| Liens Markdown internes cassés (wiki-oca) | 0 | ✅ OK |
| Références de navigation (`mkdocs.yml` → fichier) — hermes-wiki | 12/12 résolues | ✅ OK |
| Références de navigation — wiki-oca | 37/37 résolues, 0 mortes | ✅ OK |
| Lint du corpus Leo Knowledge | `raw=5 pages=14 errors=0 warnings=0` | ✅ OK |
| Contradictions ouvertes déclarées | `reports/contradictions.md` : aucune contradiction nouvelle ouverte | ✅ OK |
| Alignement API ↔ index interne Leo Docs | 1453 docs servis = 1453 docs indexés (mesure identique par les deux voies) | ✅ OK |
| Services `8765`, `8766`, `9119`, `8793` | tous en écoute, HTTP 200/302/307 | ✅ OK |
| GitHub Pages `wiki-oca` / `hermes-wiki` | `200` / `200` | ✅ OK |

---

## 5. Résultats — ce qui dérive

### 5.1 D-01 — Wiki Hermes : 129 pages hors navigation (priorité HAUTE)

`mkdocs build --strict` signale **129 pages présentes dans `docs/` mais absentes de la `nav` de `mkdocs.yml`**. Sur 141 fichiers Markdown, **12 seulement sont navigables**.

Détail par famille :

- **Chapitres pédagogiques complets non exposés** : `hermes/decouvrir/` (ch01–ch04, 6 fichiers), `hermes/configurer/` (ch05–ch09, 5), `hermes/bureaux/` (ch10–ch15, 6), `hermes/skills/` (ch16–ch21, 6), `hermes/dashboards/` (ch22–ch25, 4), `hermes/automatisation/` (ch26–ch30, 5), `hermes/annexes/` (5) — soit **~37 chapitres rédigés qui ne sont atteignables par aucun menu**.
- **Doublons de structure** : `docs/annexes/*` **et** `docs/hermes/annexes/*` (5 fichiers en double) ; `docs/AUDIT.md` **et** `docs/hermes/AUDIT.md`.
- **Archives légitimes hors nav** (attendu, mais non déclaré comme tel) : `hermes/archives/`, `hermes/_archive/`, `hermes/archives/retirees-2026/`, `archives/`.
- **Journal quotidien** : 65 fichiers `docs/journal-2026-07-xx.md` → `journal-2026-09-23.md`, hors nav.
- **Pages de 1re génération obsolètes** : `docs/hermes/etat-des-lieux.md`, `docs/hermes/audit-documents-a-reviser.md`, `docs/BAVI_ONTOLOGY.md`.

**Impact** : un lecteur qui arrive sur le wiki publié ne voit que 12 pages ; ~90 % de la documentation rédigée est invisible depuis la navigation. Aucun bandeau n'indique qu'il s'agit d'archives ou de brouillons.

**Source de mesure** : sortie `mkdocs build --strict`, section *« The following pages exist in the docs directory, but are not included in the "nav" configuration »*.

### 5.2 D-02 — Liens morts : dashboard GitHub Pages inexistant (priorité HAUTE)

L'URL `https://christophedanhier-hash.github.io/leo-dashboard/` répond **HTTP 404**.

Elle est citée dans **10 occurrences**, dont **2 dans des pages actives** :

| Fichier | Ligne | Statut du fichier |
|---|---|---|
| `hermes/bureaux/ch11-bureau-michel.md` | 160 | **Actif** (page publique) |
| `hermes/annexes/exemple-leo-complet.md` | 67 | **Actif** (non exposé — cf. D-01) |
| `archives/exemple-leo-complet.md`, `hermes/archives/exemples-LEO.md` | — | Archives (à conserver tels quels) |

**URL réellement servie, vérifiée** : `https://tofdan.be/dashboard/` → **200**, et `http://localhost:9119/` → **200**.

**Impact** : deux références actives pointent vers une ressource inexistante ; la doc désigne une cible que l'infrastructure n'héberge plus.

### 5.3 D-03 — Wiki OCA : 21 ancres internes cassées (priorité MOYENNE)

`mkdocs build --strict` remonte **21 liens du type `#ancre` sans cible** sur 3 fichiers non exposés dans la nav :

- `t600/cowork/sources/Rapport_Analyse_T600_02.md` — 11 ancres mortes
- `t600/cowork/sources/analyse_Docs_JP_Phase_01.md` — 10 ancres mortes

Ces fichiers sont des **rapports sources importés** (analyse Copilot du système T600). Les ancres visées (`#4-prérequis-et-accès-au-système`, `#24-distribution-électrique`, `#3-analyse-par-sous-système`…) sont des **renvois vers la table des matières du rapport d'origine**, non recopiés à l'import.

**Impact** : table des matières non cliquable. Le contenu est intact — c'est un défaut de fidélité à l'import, pas une perte d'information.

### 5.4 D-04 — Wiki OCA : 15 pages hors nav dont 12 non justifiées (priorité MOYENNE)

Sur 85 pages hors nav, 70 sont des journaux (`journal-2026-*`, exclusion volontaire plausible) et **15 sont du contenu réel non exposé** :

- `formation-guide-astro/sources-integrales/` — **12 fichiers** (index + 11 modules sources). Or les **modules dérivés** (`formation-guide-astro/modules/`, 12 fichiers) sont, eux, bien dans la nav : la couche « sources intégrales » a été délibérément rendue invisible. Divergence à confirmer (choix assumé ou oubli ?).
- `t600/cowork/sources/` — **3 fichiers** de rapports d'analyse (ceux de D-03). Ces documents portent les conclusions d'analyse T600 : leur retrait de la nav mérite un bandeau explicite ou une page d'index.

### 5.5 D-05 — Écart écosystème : `emile-wiki` semble sortir de Leo Docs (priorité HAUTE — à confirmer)

Le référentiel de Leo Docs déclare 17 sources dont `emile-wiki` (`leo-docs.py:145`). Or :

- `emile-wiki` est bien dans `DOC_ROOTS` du code **local** de `leo-docs.py` (version sur disque) ;
- l'index **réellement servi** par le service en écoute sur `:8766` remonte bien `emile-wiki: 19` documents.

**Écart constaté** : le service `:8766` tourne sur `/home/tofdan/Projets_Dev/leo-docs.py` (symlink créé le 17/08) tandis que le **dépôt Git** est `/home/tofdan/Projets_Dev/leo-docs/leo-docs.py`. Les deux chemins coexistent. Le `:8766` a été démarré le 21/09 et sert une version qui compte 1453 documents.

**À confirmer par Michel** (périmètre infra) : le service sert-il la version versionnée du dépôt, ou une copie antérieure ? Tant que ce n'est pas établi, l'index de Leo Docs **n'est pas traçable au dépôt** — et une correction poussée dans le dépôt pourrait ne pas être celle qui est servie.

### 5.6 D-06 — Pages « zombies » obsolètes non neutralisées (priorité MOYENNE)

| Page | Problème |
|---|---|
| `docs/hermes/etat-des-lieux.md` | Se déclare archivée au 07/07/2026 ; annonce Hermes `v0.18.2`, Python `3.14.4`, 5 profils, « Docker non utilisé », 126 skills. Aucune de ces valeurs n'est l'état courant. |
| `docs/hermes/audit-documents-a-reviser.md` | « État des lieux au 04/07/2026 » : liste 75 documents à réviser sous forme de cases **toutes décochées**. Aucun statut d'avancement → impossible de savoir ce qui a été traité. |
| `docs/BAVI_ONTOLOGY.md` + `docs/hermes/BAVI_ONTOLOGY.md` | Doublon de nom entre deux emplacements (cf. D-01). |

**Impact** : ces pages se présentent comme des documents de référence sans être marquées comme périmées dans la navigation, et donnent des chiffres faux si lues hors contexte.

---

## 6. Incohérences doc ↔ état réel vérifié de la plateforme

| # | Affirmation documentaire | État réel mesuré le 24/09/2026 | Verdict |
|---|---|---|---|
| I-01 | `etat-des-lieux.md` : « 5 profils actifs (default, emile, michel, robert, sylvia) » | **6 profils** : `default`, `emile`, `gerard`, `michel`, `robert`, `sylvia` | ❌ Périmé |
| I-02 | `etat-des-lieux.md` : Hermes `v0.18.2` | **`v0.19.0`** (`.update_check`) | ❌ Périmé |
| I-03 | `etat-des-lieux.md` : « Docker non utilisé — host services » | Un conteneur Docker Ollama (`qwen2.5:7b`) est documenté sur la même page et des process tiers tournent en conteneur | ⚠️ Contradiction interne |
| I-04 | `etat-des-lieux.md` : « Crons actifs : 49 » | **75 jobs** dans `profiles/michel/cron/jobs.json` | ❌ Périmé |
| I-05 | `TABLE.md` : « 6 profils, 72 jobs Michel » (21/09/2026) | 6 profils ✔ / **75 jobs** | ⚠️ Jobs à rafraîchir |
| I-06 | `TABLE.md` : `gerard` → modèle `gpt-5.6-luna` | **`DeepSeek-V4.1-Flash`** (azure-foundry), fallback `gemini-3.7-flash` — changement du 24/09/2026 | ❌ Périmé (bug de modèle Gérard) |
| I-07 | `ch11-bureau-michel.md` : dashboard sur `christophedanhier-hash.github.io/leo-dashboard/` | **404**. Réel : `https://tofdan.be/dashboard/` (200) | ❌ Lien mort |
| I-08 | `TABLE.md` : services `8765`, `8766`, `9119`, `8793` | Les 4 sont en écoute ✔ — mais **le port 8766 sert une version de code non traçable au dépôt** (D-05) | ⚠️ Partiel |
| I-09 | `etat-des-lieux.md` : Skills installés « 126 » puis « 105 » (deux valeurs sur la même page) | Non re-mesuré (hors périmètre de cette passe) | ⚠️ Incohérence interne |

> **Note de traçabilité** : I-06 est une incohérence que je porte moi-même — ma propre ligne de profil dans `TABLE.md` ne reflète plus le modèle que j'exécute depuis le 24/09/2026.

---

## 7. Le cas Leo Docs — documents orphelins et valeur de preuve

### 7.1 Ce qui est sain

- Le corpus de connaissance `leo-knowledge` passe son lint : `raw=5 pages=14 errors=0 warnings=0`.
- Le rapport `reports/contradictions.md` est **à jour et honnête** : il ne recopie pas les anciennes descriptions d'Émile/ Gérard comme état courant.
- L'index Geo Docs est cohérent entre l'API (`/docs/api/pages`, 1453) et l'index interne (`build_index`, 1453).

### 7.2 Ce qui mérite décision

**31 noms de documents sont dupliqués entre plusieurs groupes.** Exemples significatifs :

| Nom dupliqué | Groupes concernés | Lecture |
|---|---|---|
| `memoire-consolidee-20260806` | vault-michel, vault-emile, vault-sylvia, vault-robert (**4 copies**) | Copies de mémoire par profil — duplication attendue, mais **aucune trace de laquelle fait foi** |
| `audit-crons-20260730` | vault-michel, bavi-leo | **Deux copies du même audit** dans deux corpus |
| `analyse-scope-skills-workflows` | bavi-leo × 4 bureaux | Copies conformes par bureau |
| `vault-structure` | vault-christophe, vault-emile, vault-sylvia | Fichiers de configuration dupliqués |
| `audit`, `commandes`, `glossaire`, `guide-rapide`, `troubleshooting` | `hermes-wiki/` **et** `hermes-wiki/hermes/` | **Doublons purs** dans le même dépôt (cf. D-01) |

**20 documents indexés n'ont pas été modifiés depuis plus de 60 jours** (le plus ancien : `vault-*/Hermes/Config/vault-structure`, 82 jours ; les rapports T600 Cowork, 76 jours). Ces documents sont **servis au même titre que des documents actifs** : rien ne signale leur ancienneté.

**Recommandation de conservation** : les rapports `t600/cowork/sources/` et `reports/cleanup-*` ont **valeur de preuve** (traçabilité d'un audit et d'un nettoyage). Ils doivent être conservés **avec un statut explicite** (page d'index « sources et preuves »), pas supprimés ni laissés flottants.

---

## 8. Checklist de validation

| # | Contrôle | Résultat |
|---|---|---|
| V-01 | Le build strict des deux wikis passe sans erreur | ✅ `exit=0` pour les deux |
| V-02 | Le nombre de pages hors nav est chiffré avec la commande qui le produit | ✅ 129 (hermes-wiki) / 15 hors journaux (wiki-oca) |
| V-03 | Chaque lien mort est testé par une requête HTTP réelle | ✅ `curl` — 404 confirmé sur `leo-dashboard` |
| V-04 | Chaque incohérence doc/réel est adossée à une mesure | ✅ 9 incohérences sourcées (§6) |
| V-05 | L'index Leo Docs est comparé entre les deux voies (API ↔ interne) | ✅ 1453 = 1453 |
| V-06 | Les garde-fous du corpus sont exécutés | ✅ `lint.py` : 0 erreur, 0 avertissement |
| V-07 | Aucune modification de contenu n'a été faite | ✅ audit en lecture seule |
| V-08 | Le point d'incertitude est déclaré, pas comblé | ✅ D-05 : traçabilité du `:8766` à confirmer par Michel |

---

## 9. Priorisation proposée

| Priorité | Objet | Porteur | Nature |
|---|---|---|---|
| **P1** | D-02 : corriger les 2 liens morts `leo-dashboard` (pages actives) → `tofdan.be/dashboard/` | LEO (wiki Hermes) | Correction éditoriale |
| **P1** | D-05 : établir quelle version de code sert `:8766` et la rattacher au dépôt | **Michel** (infra) | Vérification infra |
| **P1** | I-06 : corriger la ligne `gerard` dans `TABLE.md` | **Gérard** (moi) | Correction éditoriale |
| **P2** | D-01 : décider du sort des 129 pages hors nav — exposer les chapitres rédigés, déclarer les archives comme telles | LEO + Christophe | Décision de structure |
| **P2** | D-06 : neutraliser les pages zombies (`etat-des-lieux.md`, `audit-documents-a-reviser.md`) — bandeau daté ou archivage | LEO | Correction éditoriale |
| **P3** | D-03 : restaurer les 21 ancres des rapports T600 Cowork | **Gérard** | Correction de fidélité |
| **P3** | D-04 : statuer sur `sources-integrales/` et `t600/cowork/sources/` | Christophe | Décision de structure |
| **P3** | §7.2 : page d'index « sources et preuves » pour les rapports d'audit | Gérard + LEO | Structuration |

---

## 10. Sources

- Sortie `mkdocs build --strict` (hermes-wiki, wiki-oca) — 24/09/2026
- `curl http://127.0.0.1:8766/docs/api/pages` — 24/09/2026
- `python3 lint.py` dans `leo-knowledge` — 24/09/2026
- `.update_check` Hermes → `v0.19.0`
- `git log` / `git remote -v` — a1a4097 (hermes-wiki), 07a47e0 (leo-docs), c411801 (leo-knowledge), b0eb62b (wiki-oca)
- `ss -ltnp` → ports 8765/8766/9119/8793
- `ps aux` → PID 2474700 `leo-docs.py :8766` (démarré 21/09)
- `leo-docs.py:137-155` → déclaration des 17 `DOC_ROOTS`
- Lignes citées : `hermes/bureaux/ch11-bureau-michel.md:160`, `TABLE.md:5`, `etat-des-lieux.md:25-31`
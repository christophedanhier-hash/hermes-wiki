# Sources Ethnographiques — T600

Les documents sources du projet T600 ont été collectés, analysés et structurés par le rôle **Ethnographe** du Bureau Gérard, à partir d'entretiens avec **Jean-Paul Dumoulin** et **Christian Wanlin**, ainsi que des documents bruts partagés sur Google Drive.

> **Source :** Google Drive — `01_SOURCES_BRUTES` (ID: 14D-4vFZiLvfiuCGOmhdMLFUItW6Nl95V)

---

## Fiches sources

### Fiche 1 — Domotisation Télescope T600 (PDF)

| Champ | Valeur |
|-------|--------|
| **Titre** | Domotisation du Télescope T600 |
| **Auteurs** | Christian Wanlin & Jean-Paul Dumoulin |
| **Date** | 25 mai 2026 |
| **Type** | PDF (13 pages, image-based) |

Document fondateur décrivant l'architecture complète du système :
- Pilotage via automate **IPX800**
- Transmission radio **NRF24L01** pour les cimiers
- Cartes **Pléiades** (Alcyone-5, Electra-5, Maia-4)
- Intégration logicielle : ASCOM, NINA, AnyDesk, Foscam

> **Lacune :** Aucun schéma de câblage détaillé. Document entièrement composé d'images — texte obtenu par OCR.

### Fiche 2 — Améliorations (Google Doc)

| Champ | Valeur |
|-------|--------|
| **Titre** | Améliorations |
| **Auteur** | Jean-Paul Dumoulin |
| **Type** | Google Doc (export .docx) |

Document concis listant les **lacunes critiques** identifiées par JP :

- ❌ Absence de capteurs fin de course AD/DEC → risque de collision destructrice
- ❌ Autoguideur non documenté → imagerie longue pose compromise
- ❌ Absence de parafoudre type 2 → risque pour l'électronique

> **Correction importante :** PC NUC-T600 est au 1er étage (alimente l'IPX800), PC NUC-T600-TELE est alimenté par l'IPX800.

### Fiche 3 — Opérations_T600.pptx

| Champ | Valeur |
|-------|--------|
| **Titre** | Opérations et Télémétrie Experte du Télescope T600 |
| **Auteurs** | Jean-Paul Dumoulin & Christian Wanlin |
| **Date** | 2026 — Édition Harmonisée |
| **Type** | PowerPoint (11 slides) |

Présentation experte apportant :
- **Matrice de criticité** : Nominal / Alerte / Séquentiel / Criticité Maximale
- **Séquence d'initialisation** complète avec vérifications
- **Diagnostic télémétrique 4 axes** (Énergie, Data, Commutation, Environnement)
- **Procédure d'extinction** en 4 niveaux
- Cartographie réseau complète

### Fiche 4 — T600-Mise-en-route-20260525.pptx

| Champ | Valeur |
|-------|--------|
| **Titre** | T600 — Mise en route au 26/05/2026 |
| **Auteurs** | Jean-Paul Dumoulin & Christian Wanlin |
| **Date** | 26 mai 2026 |
| **Type** | PowerPoint (17 slides) |

Procédure complète de démarrage et d'extinction, slide par slide :
- Architecture à deux PC (NUC + NUC-TELE)
- Double accès local/distant
- Tous les identifiants et mots de passe documentés
- Séquence d'extinction en 3 étapes

> **Lacune :** Pas de détail sur les 4 boutons à cliquer dans l'interface IPX800.

### Fiche 5 — Domotisation-T600-20260525.pptx

| Champ | Valeur |
|-------|--------|
| **Titre** | Domotisation T600 : 25 mai 2026 |
| **Auteurs** | Christian Wanlin & Jean-Paul Dumoulin |
| **Date** | 25 mai 2026 |
| **Type** | PowerPoint (39 slides) |

Vue d'ensemble architecturale complète de la domotisation :
- Matériel central → Cimiers → Télescope → Rotation Dôme → Logiciel
- Sécurités : arrêts d'urgence par diodes, détecteur de pluie
- Supervision : AnyDesk + caméra Foscam

> **Lacune :** Majorité des slides sans texte (contenu visuel uniquement).

### Fiche 6 — Rapport de Croisement Experts

| Champ | Valeur |
|-------|--------|
| **Titre** | Rapport de Croisement — Télescope T600 |
| **Rôle** | Orchestrateur-Gérard, Phase 4 |
| **Date** | 12 juin 2026 |

Synthèse croisant les analyses **Astro-Optique**, **Hardware** et **Firmware** :

**Convergences (18 points)**
- Architecture IPX800, chaîne cimiers, cartes Pléiades validées par tous
- Boucle fermée Maia-4 avec encodeur quadrature
- 5 points forts confirmés : domotique fonctionnelle, séquence dém/extinction, réseau IP complet

**Divergences (6 points)**
- Type de moteur AD/DEC : pas-à-pas vs doute FW
- Nombre de moteurs cimiers : 2 ou 4 ?
- Dome Radius NINA : offset optique vs rayon
- Dimensions GEM aberrantes (50 mm N/S suspect)

**Actions prioritaires P1 (5 actions critiques)**

| # | Action | Effort |
|---|--------|:------:|
| P1.1 | Relevé optique obligatoire | 1 jour |
| P1.2 | Installer capteurs fin de course AD/DEC | 2-3 jours |
| P1.3 | Installer parafoudre Type 2 | ½ jour |
| P1.4 | Extraire les firmwares | 1-2 jours |
| P1.5 | Créer procédure de mise en station | 2 jours |

---

## Documents connexes

### Note de Service — Jean-Paul Dumoulin

Date : 12 juin 2026  
Expéditeur : Christophe Danhier (pilote documentation T600)

Accusé de réception des corrections v1.2 de Jean-Paul Dumoulin :
- **9 corrections intégrées** : sous-réseau `192.168.0.x`, ordre d'extinction réordonné, rebranchement batterie au Niveau 1
- **8 nouveautés Hermes** : analyse astro-optique, firmware, hardware, recommandations P1/P2/P3
- **Formation v1.1 enrichie** : objectifs SMART, sémantique Output/Input, annexe formateur

### Synthèse des changements v1.0 → v1.1

Date : 12 juin 2026

Fusion des forces Hermes (analyse système) + Cowork v1.2 (corrections JP Dumoulin) :
- Adresses IP corrigées dans 11 sections
- Ordre d'extinction modifié : Info avant Relais
- 6 ajouts matériels (pilotage manuel, sonde NUC, brochage ST-4...)
- Formation enrichie (SMART, Output/Input, diagnostic 4 axes)

### Mise à jour des Skills — Bureau Gérard

Date : 12 juin 2026

Mise à jour des compétences des agents Hermes suite à l'analyse :
- **Hardware :** brochage ST-4, diagnostic 4 axes
- **Firmware :** patterns ISR fins de course, Pulse Guide autoguidage
- **Formateur :** structure obligatoire 10 sections
- **Rédacteur :** cross-reference corrections Cowork
- **Orchestrateur :** scope verification Phase 0, nouvelle Phase 3b

---

## Méthodologie

La collecte ethnographique a suivi le processus suivant :

1. **Extraction** des documents bruts depuis Google Drive
2. **Analyse** et structuration en fiches avec métadonnées
3. **Croisement** des analyses par experts (AO, HW, FW)
4. **Validation** par Jean-Paul Dumoulin (corrections v1.2)
5. **Synthèse** en documentation technique et formation

> **Principe :** Chaque information est tracée avec sa source, sa fiabilité et son statut (confirmé / à confirmer / lacune).

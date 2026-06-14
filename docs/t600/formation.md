# Formation Opérateur — Télescope T600

Version 1.1 — 12 juin 2026  
Durée estimée : 1 journée (théorie + pratique)  
Prérequis : notions de base en astronomie, utilisation d'un PC

> **Objectif principal :** À l'issue de la formation, l'opérateur sera capable de mettre en route, utiliser et éteindre le T600 en autonomie, en respectant les consignes de sécurité.

---

## Objectifs pédagogiques (SMART)

| Critère | Objectif |
|---------|----------|
| **Spécifique** | Exécuter la séquence complète de mise en route et d'extinction, de la vérification météo au rebranchement de la batterie |
| **Mesurable** | Réaliser les 8 étapes clés sans erreur d'ordre |
| **Atteignable** | Oui — après démonstration et mise en situation encadrée |
| **Réaliste** | Adapté aux opérateurs OCA sans prérequis technique avancé |
| **Temporel** | Validé en fin de session de 3h par une mise en situation complète notée |

---

## Module 1 — Présentation du T600

Le **T600** est un télescope de **600 mm d'ouverture** installé à l'**OCA**, captant environ **7 300 fois plus de lumière** que l'œil humain.

### Caractéristiques principales

- **Ouverture :** 600 mm
- **Monture :** Équatoriale allemande (GEM)
- **Dôme :** 4 500 mm de diamètre, motorisé
- **Domotisation :** Pilotage complet via automate IPX800
- **Supervision :** Caméra Foscam + AnyDesk (télétravail possible)

### Sécurité — Règles d'or

> **RÈGLE #1 :** JAMAIS de rotation du dôme avec le câble de charge des cimiers branché.
>
> **RÈGLE #2 :** Toujours vérifier que les cimiers sont 100 % ouverts avant de faire tourner le dôme.
>
> **RÈGLE #3 :** En cas d'orage, exécuter l'extinction complète immédiatement.
>
> **RÈGLE #4 :** Ne jamais forcer un mouvement mécanique — arrêter et diagnostiquer.

---

## Module 2 — Architecture et composants

### Composants clés

| Composant | Rôle |
|-----------|------|
| **IPX800** | Automate commandant tous les relais (adresses .237 et .238) |
| **PC T600-NUC** | PC du 1er étage, alimente l'IPX800 |
| **PC T600-NUC-TELE** | PC pilotant le télescope (NINA, LesveDomeNet) |
| **Caméra Foscam** | Supervision visuelle du dôme (latence < 1s) |
| **Cimiers** | Volets du dôme, commande radio via NRF24L01 |
| **Encodeur Grayhill** | Capteur de position du dôme |
| **Batterie cimiers** | Alimentation partie tournante (toujours en charge) |

### Sémantique IPX800 — Output / Input

- **Output :** ordre envoyé par l'IPX800 (« mets sous tension »)
- **Input :** mesure constatée (« la tension est présente en aval »)

| Situation | Interprétation | Action |
|-----------|----------------|--------|
| ✅ Output=ON et Input=ON | Équipement alimenté | Continuer |
| ❌ Output=ON mais Input=OFF | Problème (fusible, câble) | Diagnostiquer |
| ❌ Output=OFF mais Input=ON | Fuite ou relais collé | Intervention technique |

> **Astuce :** L'écart Output/Input est votre **premier indicateur de panne**.

---

## Module 3 — Démarrage pas-à-pas

### Étapes de démarrage

**1. Préparation physique**
- Débrancher le câble de charge des cimiers
- Enlever la bâche du télescope
- Mettre tension coffret cimier si nécessaire

**2. Connexion au PC T600-NUC**
- Local : mot de passe `forets`
- AnyDesk : 513 471 809 / `T6002024$#@`

**3. Alimentation IPX800**
- `192.168.0.237` → ON sur D0 → Actualiser

**4. Activation sorties IPX800**
- `192.168.0.238` → Login Admin / `Oc@2018`
- Activer les sorties → Vérifier Output/Input

**5. Connexion au PC T600-NUC-TELE**
- AnyDesk : 1 041 426 244 / `T600NUC2024$#@`

**6. Caméra Foscam**
- Programme Foscam T6002021
- Login `foscamt600` / `T6002021`

**7. Diagnostic télémétrique (4 axes)**

| Axe | Vérification | Attendu |
|-----|-------------|:-------:|
| ⚡ Énergie mobile | Tension batterie cimiers | NOMINAL |
| 📊 Intégrité data | Communication NRF24L01 | NOMINAL |
| 🔄 Commutation | Relais Keyes, fins de course | NOMINAL |
| 🌧️ Environnement | Détecteur de pluie, température | NOMINAL |

**8. Ouverture des cimiers**
- Commande S6 → ~90 secondes
- Surveiller courant ACS712 + caméra

**9. Rotation du dôme** (conditions strictes)
- Cimiers 100 % ouverts, câble débranché
- Lancer LesveDomeNet

### Extinction en 4 niveaux

| Niveau | Action |
|:------:|--------|
| **1 — Mécanique** | Fermer cimiers (S4), rebrancher batterie |
| **2 — Informatique** | Arrêter T600-NUC-TELE (intégrité fichiers) |
| **3 — Relais** | Désactiver toutes les sorties IPX800 .238 |
| **4 — Énergie** | Couper IPX800 .237 |

> **Ordre validé v1.2 :** l'arrêt informatique précède la coupure des relais pour protéger l'intégrité des fichiers d'acquisition.

---

## Module 4 — Opérations courantes

### Pointage du télescope

> ⚠️ Aucune procédure documentée pour l'alignement stellaire et la mise en station à ce jour.

Étapes indicatives :
1. Mise en station (polar alignment) via SharpCap
2. Alignement stellaire dans NINA (plate solving, ≥ 6 étoiles)
3. Centrage de l'objet cible

### Acquisition d'images (NINA)

1. Lancer NINA sur T600-NUC-TELE
2. Configurer la séquence (filtre, temps de pose, nombre)
3. Lancer l'acquisition
4. Surveiller via Foscam et les logs

---

## Module 5 — Diagnostic et dépannage

| Problème | Cause probable | Solution |
|----------|---------------|----------|
| IPX800 ne répond pas | PC NUC éteint | Vérifier T600-NUC, switch WiFi |
| Cimiers bloqués | Batterie déchargée | Vérifier tension, test relais |
| Caméra absente | Programme non démarré | Vérifier login foscamt600 |
| Rotation irrégulière | Encodeur Grayhill sale | Nettoyer roue encodeur |

### Quand appeler le support

- Bruit mécanique anormal → **arrêter immédiatement**
- Odeur de brûlé → **couper l'alimentation générale**
- Fumée → **évacuer, appeler les pompiers**
- Problème récurrent non résolu → appeler avec description détaillée

---

## Module 6 — Maintenance 1er niveau

| Périodicité | Actions |
|-------------|---------|
| **Avant chaque session** | Diagnostic télémétrique, vérification visuelle, test communication |
| **Hebdomadaire** | Contrôle batterie cimiers, soufflette optique |
| **Mensuel** | Inspection ventilation Alcyone-5, test arrêts d'urgence |
| **Trimestriel** | Nettoyage encodeur Grayhill, contrôle variateur 24.0 Hz |
| **Annuel** | Relevé électrique complet, inspection câbles, maintenance moteurs |

### Actions interdites

- ❌ Toucher les surfaces optiques
- ❌ Forcer un mouvement mécanique
- ❌ Modifier un paramètre inconnu
- ❌ Débrancher/rebrancher sans couper
- ❌ Utiliser sans supervision la première fois

---

## Annexe — Lexique

| Terme | Définition |
|-------|------------|
| **Ouverture** | Diamètre du miroir principal |
| **Focale** | Distance de formation de l'image |
| **Monture équatoriale** | Suit la rotation terrestre |
| **AD / DEC** | Ascension Droite / Déclinaison |
| **Cimiers** | Volets du dôme |
| **NINA** | Logiciel d'acquisition et pilotage |
| **Autoguidage** | Correction automatique du suivi |
| **Plate Solving** | Identification des étoiles par photo |

### Aide-mémoire des accès

| Service | Identifiant | Mot de passe |
|---------|-------------|:------------:|
| IPX800 | Admin | Oc@2018 |
| AnyDesk T600-NUC-TELE | 1 041 426 244 | T600NUC2024$#@ |
| AnyDesk T600-NUC | 513 471 809 | T6002024$#@ |
| Foscam locale | foscamt600 | T6002021 |
| WiFi dôme | wireless2.4G_A84620 | Admin2021$ |
| Local 1er étage | — | forets |

> **À conserver en lieu sûr — ne pas diffuser largement.**

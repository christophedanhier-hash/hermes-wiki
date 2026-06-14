# Documentation Technique du T600

Version 1.1 — 12 juin 2026  
Rédacteur : Rédacteur Technique (Bureau Gérard)

> **Statut :** Document initial — nombreuses sections marquées [LACUNE] nécessitant un complément terrain.

---

## Présentation du système

Le **T600** est un télescope de **600 mm** d'ouverture monté en **configuration équatoriale allemande (GEM)**, intégré dans un dôme motorisé de **4500 mm** de diamètre avec coupole rotative et volets automatisés (cimiers).

Le système combine :
- Une **domotisation complète** via automate IPX800
- Une **électronique de pilotage** par cartes Pléiades (Alcyone-5, Electra-5, Maia-4)
- Un **réseau WiFi/Ethernet** avec supervision à distance (AnyDesk, caméra Foscam)
- Des **microcontrôleurs Arduino** pour les communications radio (NRF24L01) des cimiers
- Un **watchdog environnemental** (Wemos D1 Mini + DS18B20)

### État du système

| Aspect | Évaluation |
|--------|:----------:|
| Infrastructure électrique/réseau | ✅ Bien documentée |
| Noyau astronomique | ❌ Quasi-absent des sources |
| Procédures démarrage/extinction | ✅ Bien documentées |
| Sécurité | ⚠️ Lacunes critiques (fin de course, parafoudre) |

> **Lacune critique :** Les spécifications optiques (focale, type optique, collimation) et les procédures astronomiques (mise en station, alignement, autoguidage) ne sont **pas documentées**.

---

## Architecture réseau

```text
RÉSEAU GLOBAL T600 — SSID: wireless2.4G_A84620
├── 192.168.0.236 → Commande cimiers (wifi)
├── 192.168.0.237 → IPX800 Alimentation (ON/OFF)
├── 192.168.0.238 → IPX800 Relais E/S (Admin / Oc@2018)
├── 192.168.4.201 → Énergie & Environnement (Wemos D1 Mini + DS18B20)
├── T600-NUC-TELE  → PC pilotage télescope (AnyDesk: 1 041 426 244)
└── T600-NUC       → PC 1er étage (AnyDesk: 513 471 809)
```

## Architecture d'alimentation

```text
[Réseau EDF] → Variateur (24.0 Hz) → Moteur réducteur rotation dôme
[Pilier 20V] → IPX800 S2
    ├── Alimentation Télescope 12V
    └── Alcyone-5 [12V-24V → régule 12V(drivers) + 9V(Arduino Uno)]
            └── Electra-5 [régule 5V + 3.3V]
                    └── Maia-4 [TB67H303HC, max 24V, 2.7A]
[Batterie cimiers] → toujours en charge → Arduino Mega + NRF24L01 + Relais
[Watchdog] Wemos D1 Mini (ESP8266) + DS18B20
```

## Chaîne cimiers (volets du dôme)

**Partie fixe :** IPX800 → Relais Keyes → Arduino Uno → NRF24L01 TX

**Partie tournante (sur batterie) :** Arduino Mega + NRF24L01 RX
- Relais moteurs → Moteurs cimiers (×2 à confirmer)
- Capteur ACS712 (mesure courant moteur)
- Capteurs fin de course (GH, GB, DY, DB)
- Détecteur de pluie

> Pilotage manuel possible via interrupteurs physiques à côté du boîtier.

## Chaîne rotation dôme

PC T600-NUC-TELE → USB → Velleman PVM110N (timer: 60ms) → Variateur (24.0 Hz) → Moteur réducteur
Retour position : Encodeur Gray Code (Grayhill 654321, 16 trous, roue 241mm) + Switch Home

## Chaîne télescope / monture

PC T600-NUC-TELE → ASCOM/NINA → Alcyone-5 → Electra-5 → Maia-4 (TB67H303HC) → Moteurs pas-à-pas AD/DEC
- Boucle fermée via encodeur quadrature
- Port ST-4 présent pour autoguidage

## BOM — Composants référencés

| Réf. | Désignation | Fabricant | Qté |
|:----:|-------------|-----------|:---:|
| H-001 | Automate IPX800 | GCE Electronics V4/V5 | 1 |
| H-002 | Wemos D1 Mini | ESP8266 | 1 |
| H-003 | Arduino Uno R3 | Arduino.cc | 1 |
| H-004 | Arduino Mega R3 | Arduino.cc | 1 |
| H-005 | Module NRF24L01+ | Nordic Semiconductor | 2 |
| H-006 | Sonde DS18B20 | Maxim Integrated | 1 |
| H-007 | Encodeur Gray Code | Grayhill 654321 | 1 |
| H-008 | Interface USB → Analogique | Velleman PVM110N | 1 |
| H-009 | Driver moteur pas-à-pas | Toshiba TB67H303HC | 1 |
| H-010 | Carte Alcyone-5 Shield | Pléiades | 1 |
| H-011 | Carte Electra-5 | Pléiades | 1 |
| H-012 | Carte Maia-4 | Pléiades | 1 |
| H-013 | Capteur courant | ACS712 | 1 |
| H-014 | Relais power switch | Keyes SRly | 1 |
| H-015 | Caméra IP | Foscam FI9831P-T600 | 1 |

## Brochage ST-4 (port autoguidage)

| Broche | Couleur | Signal | Effet |
|:------:|:-------:|:------:|-------|
| 1 | Blanc | NC | Non connecté |
| 2 | Noir | GND | Masse |
| 3 | Rouge | RA+ | Correction A.D. vers l'est |
| 4 | Vert | DE+ | Correction DECL. vers le nord |
| 5 | Jaune | DE− | Correction DECL. vers le sud |
| 6 | Bleu | RA− | Correction A.D. vers l'ouest |

## I/O Mapping — IPX800

| Sortie | Fonction | Statut |
|:------:|----------|:------:|
| S1 | Rotation Coupole | ✅ |
| S2 | Pilier 20V & Télescope 12V | ✅ |
| S3 | PC NUC T600 | ✅ |
| S4 | Fermeture Cimiers | ✅ |
| S5 | Fermeture Cimiers URGENCE | ✅ |
| S6 | Ouverture Cimiers | ✅ |
| S7 | Non spécifié | ❌ [LACUNE] |
| S8 | Non spécifié | ❌ [LACUNE] |

## Spécifications mécaniques connues

| Paramètre | Valeur | Statut |
|-----------|--------|:------:|
| Diamètre coupole | 4500 mm | ✅ |
| Temps Shutter (cimiers) | 90 s | ✅ |
| Variateur fréquence | 24.0 Hz | ✅ |
| Timer interval Velleman | 60 ms | ✅ |
| Position Home | 310 | ⚠️ Unité inconnue |
| Dome Radius (NINA) | 750 mm | ⚠️ Probable offset optique |

## Lacunes critiques confirmées

| # | Lacune | Gravité |
|---|--------|:-------:|
| L-01 | Type optique et focale inconnus | 🔴 Critique |
| L-02 | Aucune procédure de mise en station | 🔴 Critique |
| L-03 | Autoguideur absent / non documenté | 🔴 Critique |
| L-04 | Capteurs fin de course AD/DEC absents | 🔴 Critique |
| L-05 | Parafoudre Type 2 absent | 🔴 Critique |
| L-06 | Firmwares sources indisponibles (.ino, .cpp) | 🔴 Critique |
| L-07 | Spécifications moteurs inconnues | 🟠 Grave |
| L-08 | Backlash RA/DEC non documenté | 🟠 Grave |

## Actions prioritaires

**🔴 P1 — Actions critiques (bloquantes)**

| # | Action | Effort |
|---|--------|:------:|
| P1.1 | Relevé optique : focale, type optique, backfocus | 1 jour |
| P1.2 | Installer capteurs fin de course AD/DEC | 2-3 jours |
| P1.3 | Installer parafoudre Type 2 | ½ jour |
| P1.4 | Extraire les firmwares (Arduino, Wemos) | 1-2 jours |
| P1.5 | Créer procédure de mise en station | 2 jours |

**🟠 P2 — Actions importantes**

- Créer procédure d'alignement stellaire (NINA, plate solving)
- Acquérir et installer un autoguideur
- Créer procédure de collimation
- Identifier tous les moteurs (marque, modèle, tension)
- Relevé électrique et physique sur site

> **Note :** Toute information optique doit être marquée [À CONFIRMER] tant que P1.1 n'est pas exécuté. Ne pas inventer de valeurs.

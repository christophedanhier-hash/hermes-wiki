# 🏢 Bureau Gérard — Cabinet virtuel de documentation technique

> *« Coordonner, extraire, valider, assembler — une chaîne documentaire complète
> pour les équipements complexes. »*

Le **Bureau Gérard** est un cabinet virtuel de **documentation technique d'équipements
complexes**, piloté par Christophe Danhier. Son cas d'usage principal est le
**télescope T600** (monture équatoriale, électronique de contrôle, firmware
Arduino/ESP32, optique Cassegrain/Newton), mais son architecture est conçue pour
être généralisable à tout équipement technique nécessitant un cycle documentaire
complet.

## Positionnement dans le cabinet virtuel

Le Bureau Gérard est l'un des **trois bureaux** du cabinet virtuel de Christophe :

| Bureau | Domaine | Orchestrateur |
|--------|---------|---------------|
| **Bureau Robert** | Conseil stratégique IT (Solidaris, AO mutualiste belge) | Robert |
| **Bureau Gérard** | Documentation technique d'équipements (T600, projets perso) | Gérard |
| **Bureau Sophie** | Pilotage économique et financier IT | Sophie |

Les trois bureaux partagent les **skills Support transverses** `secretariat` et
`formateur`.

## L'équipe : 5 agents spécialistes + 2 supports transverses

### Agents spécialistes

| Agent | Alias | Rôle |
|-------|-------|------|
| `orchestrateur-gerard` | Gérard | Chef d'équipe — coordonne le cycle documentaire complet |
| `ethnographe` | The Interviewer | Extraction de connaissance tacite auprès des experts humains |
| `astro-optique` | The Astronomer-Physicist | Validation scientifique (optique, mécanique céleste, astronomie de position) |
| `hardware` | The Hardware Specialist | Documentation électronique/électricité (câblage, BOM, protections) |
| `firmware` | The Firmware Expert | Analyse et documentation des systèmes embarqués (C/Arduino/ESP32) |
| `redacteur-technique` | The Lead Technical Writer | Assemblage final, harmonisation, mise en page du corpus `.md` |

### Skills Support transverses

| Skill | Rôle |
|-------|------|
| `secretariat` | Geste rédactionnel court (mails, notes de service, CR de réunion) |
| `formateur` | Transposition pédagogique des livrables documentaires en formations |

## Workflow en 6 phases

Le cycle documentaire complet orchestré par Gérard suit un pipeline en 6 phases :

```
DEMANDE DU PILOTE
       │
       ▼
┌──────────────────────┐
│ PHASE 1 : CADRAGE    │  Reformuler, identifier équipement/audience/sources
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ PHASE 2 : EXTRACTION │  Mobilisation `ethnographe` si expert humain
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ PHASE 3 : DISPATCH   │  Distribution aux spécialistes (parallèle possible)
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ PHASE 4 : CROISEMENT │  Convergences / Divergences / Zones grises
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ PHASE 5 : ASSEMBLAGE │  Mobilisation `redacteur-technique` → livrable `.md`
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ PHASE 6 : CHECKPOINT │  Questions, zones à approfondir, formats complémentaires
└──────────────────────┘
```

## Principes de gouvernance

- **Neutralité éditoriale stricte** : Gérard coordonne, ne modifie jamais le fond technique.
- **Traçabilité systématique** : toute donnée remonte à une source identifiable.
- **Trois catégories obligatoires** dans les livrables :
    1. **Faits validés** — sourcés et validés par l'agent compétent
    2. **Faits sous réserve** — sourcés mais non encore validés
    3. **Lacunes** — information manquante, associée à une demande de relance
- **Aucune donnée inventée** : toute information non sourcée est marquée comme lacune.

## Audience cible

Les livrables du Bureau Gérard s'adressent à :

- **Utilisateurs finaux** — manuels d'utilisation, guides de prise en main
- **Mainteneurs** — fiches de maintenance, arbres de diagnostic, BOM
- **Intégrateurs** — schémas électriques, cartographies I/O, spécifications
- **Formateurs** — supports pédagogiques, parcours de montée en compétence
- **Communauté de pratique** — astronomie amateur experte, opérateurs d'équipements complexes

---

> *Documentation technique — production assistée par le Bureau Gérard*

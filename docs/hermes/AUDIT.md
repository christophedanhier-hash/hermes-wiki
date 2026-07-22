## 📋 Audit rédactionnel — 22/07/2026

**Modèle :** Règles locales + audit structurel
**Fichiers audités :** 57 (hermes-wiki) + 126 (BAVI_LEO) = 183
**Anomalies :** 35
**Corrigées :** 22 (15 hermes-wiki + BAVI_LEO index + bavi-pour-les-nuls + 4 guides)

### Nouvelles corrections

| Fichier | Correction |
|---------|-----------|
| `configuration/profiles.md` | Tableau 5 profils → 8 profils avec colonne Bot Telegram |
| `configurer/ch05-gateway-profils.md` | Tableau 5 profils → 8 profils |
| `configurer/ch07-multi-bots.md` | Titre « 3 bots » → « 5 bots » |
| `architecture-communication.md` | Header 5→8 profils, section « 5 entités » → « 5 bots Telegram » |
| `etat-des-lieux.md` | Profils actifs 5→8 avec liste complète |
| `utilisation/documentation-map.md` | 5 profils → 8 profils |
| `utilisation/dashboards.md` | state.db 5→8 profils |
| `utilisation/skills-catalogue.md` | 5 profils → 8 profils |
| `dashboards/ch22-dashboards-intro.md` | state.db 5→8 profils |
| `installation/linux.md` | Diagramme gateway 5→8 profils |
| `bureaux/ch10-architecture-bureaux.md` | bureau-michel → michel + annotation |
| `configurer/ch08-skills.md` | bureau-michel → michel |
| `skills/ch21-ecrire-ses-skills.md` | bureau-michel → michel |

### Anomalies persistantes

| Fichier | Problème |
|---------|----------|
| `interface-web.md` | Mentionne 4 bots → devrait être 5 |
| `utilisation/documentation-map.md` | Mentionne 2 bots dans une ligne → devrait être 5 |

### Statistiques par statut

| Statut | Nb |
|--------|----|
| wrong (corrigé) | 15 |
| outdated (corrigé) | 7 |

## Historique

- **20/07/2026** — regex pre-scan : 71 anomalies, 18 fichiers patchés
- **17/07/2026** — Audit DeepSeek (2 passages) : profiles.md, providers.md, architecture-communication.md, crons.md
- **22/07/2026** — Audit structurel complet : 183 fichiers, 35 anomalies, 22 corrigées

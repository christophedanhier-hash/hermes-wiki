## 📋 Audit rédactionnel — 20/07/2026

**Modèle :** regex pre-scan (clé API redacted)
**Fichiers audités :** 55 (hermes-wiki)
**Anomalies :** 71
**Corrigées :** 18 fichiers patchés

| Catégorie | Nb | Statut | Détail |
|-----------|----|--------|--------|
| `/opt/data/` → `~/Projets_Dev/` | 54 corrigés | ✅ corrigé | 18 fichiers patchés |
| n8n encore mentionné comme actif | 3 fichiers | ⚠️ outdated | Conservé comme référence historique |
| Liste profils sans bureau-robert | 1 | ✅ corrigé | backup-recovery.md |
| deepseek-chat → deepseek-v4-flash | 0 | ✅ ok | Plus aucune occurrence |

**Fichiers modifiés :** ch26-crons-intro, ch12-bureau-sylvia, changelog, ch07-multi-bots, ch09-memoire, ch22-dashboards-intro, etat-des-lieux, gestion-releases, n8n, pre-migration-v017, ch16-skills-systeme, ch19-skills-creatifs, ch20-skills-recherche, ch21-ecrire-ses-skills, backup-recovery, bots-telegram, crons, dashboards

## 🤖 Audit DeepSeek — 17/07/2026 à 18:00

| Page | Section | Statut | Correction |
|------|---------|--------|------------|
| profiles.md | §4 profils | 🔴 wrong | 4→5 profils : ajout bureau-robert (DeepSeek Pro, Conseil Stratégique) |
| profiles.md | Tableau | ❌ missing | Ajout ligne bureau-robert (Conseil Stratégique IA) |
| providers.md | §Ollama modèles | ⚠️ outdated | Modèles non-installés commentés, note GPU RTX 3050 8GB |

## 🤖 Audit DeepSeek — 17/07/2026 à 15:05

| Page | Section | Statut | Correction |
|------|---------|--------|------------|
| architecture-communication.md | §2 Services | ⚠️ obsolète | n8n retiré (déprécié 13/07), 4 corrections |
| architecture-communication.md | §2 Mémoire | ⚠️ partiel | Sync corrigée : default↔leo-copilot uniquement |
| architecture-communication.md | §2 Moteurs | ⚠️ partiel | Ajout DeepSeek V4 Pro dans la liste |
| crons.md | Watchdog | ⚠️ obsolète | Fréquence 15min→2min (`*/2 * * * *`) |
| providers.md | — | ✅ conforme | Aucune correction |
| profiles.md | — | ✅ conforme | Aucune correction |

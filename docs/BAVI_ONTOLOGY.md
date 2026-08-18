# 🏗️ BAVI — Ontologie Structurée

> **Version** : 1.0 — 24 juillet 2026  
> **Auteur** : Michel (LEO — Bureau Infrastructure)  
> **Périmètre** : Écosystème BAVI complet  
> **Usage** : Charger ce fichier comme contexte pour tout bureau BAVI

---

## 1. VISION GLOBALE

BAVI (Bureau d'Analyse et de Vie Intégrée) est un écosystème d'agents IA autonomes fonctionnant sur Hermes Agent, hébergé sur le serveur LEO (Linux Ubuntu). Chaque agent est un "bureau" spécialisé avec son propre profil Hermes, sa mémoire, ses skills et ses crons.

**Architecture conceptuelle :**
```
BAVI OS
├── Léo (default)     → Interface de dialogue, délégation
├── Michel            → Infrastructure, code, crons, dashboard
├── Émile             → Pédagogie, mémoire de fin d'études
├── Robert            → Conseil stratégique IT
├── Sylvia            → Agence de voyage, roadbooks
└── Sophie (via Michel) → Budget, pilotage économique
```

**Principe fondateur** : Chaque bureau est autonome mais l'écosystème est cohérent. Les crons de Michel gèrent l'infrastructure transversale. Les autres bureaux ont leurs propres crons dans leurs profils respectifs.

---

## 2. INFRASTRUCTURE PHYSIQUE

| Composant | Détail |
|-----------|--------|
| **Serveur** | LEO — Linux Ubuntu 7.0.0-28-generic |
| **IP locale** | 100.92.102.28 |
| **Utilisateur** | `tofdan` |
| **Home** | `/home/tofdan` |
| **Hermes** | `~/.hermes/` (config, profils, crons, skills, state) |
| **Projets** | `~/Projets_Dev/` (wikis, BAVI_LEO, dashboards) |
| **Timezone** | Europe/Brussels (UTC+2) |

### Services Docker

| Service | Port | Rôle |
|---------|------|------|
| Home Assistant | 8123 | Domotique, caméras, énergie |
| Ollama | 11434 | Modèles locaux (qwen2.5:7b) |

### Dashboards

| Dashboard | Port | Accès |
|-----------|------|-------|
| LEO Control Panel | 8765 | `http://100.92.102.28:8765` — token: `leo-panel-2026` |
| Hermes Dashboard | 9119 | `http://100.92.102.28:9119` — creds: `leo` / `L30_d4nh13r_2026!` |

---

## 3. PROFILS HERMES

### 3.1 Tableau des profils

| Profil | Bot Telegram | Modèle | Provider | Rôle |
|--------|-------------|--------|----------|------|
| `default` | Léo | deepseek-v4-flash | deepseek | Interface de dialogue, délégation |
| `michel` | Michel | deepseek-v4-pro | deepseek | Infrastructure, code, crons |
| `emile` | Émile | deepseek-v4-flash | deepseek | Assistant pédagogique |
| `robert` | Robert | deepseek-v4-flash | deepseek | Conseil stratégique IT |
| `sylvia` | Bavi | deepseek-v4-flash | deepseek | Agence de voyage |

### 3.2 Providers configurés

| Provider | Type | Base URL | Usage |
|----------|------|----------|-------|
| `deepseek` | Principal | api.deepseek.com | Tous les profils |
| `openrouter` | Secondaire (configuré, non utilisé) | openrouter.ai/api/v1 | Modèles free (dépréciés) |
| `google` | Custom | generativelanguage.googleapis.com | Gemini (fallback potentiel) |
| `ollama` | Custom | localhost:11434/v1 | Modèles locaux |

### 3.3 Règles de routage

- **michel** = `deepseek-v4-pro` exclusivement — pas de fallback
- **default/emile/robert/sylvia** = `deepseek-v4-flash`
- OpenRouter configuré mais crons migrés vers DeepSeek (24/07/2026)
- Budget cible : ~$30/mois DeepSeek

---

## 4. CRONS (46 jobs gérés par Michel)

### 4.1 Catégories

| Catégorie | Nombre | Exemples |
|-----------|--------|----------|
| Collecteurs | 5 | Unified Collector, Énergie, Machine KPI, Viessmann (paused) |
| Watchdogs | 6 | Gateway FD, Dashboards, Cron, BAVI, GitHub Actions, Health Check |
| Synchronisation | 6 | Drive-sync, Drive→Issue, Doc Watch, Docs-update, Contacts, Sheets |
| Wikis & Docs | 5 | Rebuild BAVI, Rebuild Voyages, Auto-commit, Doc-crons-sync, Journaux |
| Qualité & Audit | 4 | Audit Infra, Audit Qualité Crons, Audit Rédactionnel, Doctor Michel |
| Budget & Backup | 3 | Budget Alert, Backup GDrive, Recovery Export |
| Email | 2 | Gmail Classifier, Check Gmail |
| Communication | 1 | Point Contact (4×/jour) |
| Divers | 3 | Veille IA (paused), Déploiement tofdan.be, Synthèse Hebdo |
| Nouveaux (24/07) | 2 | Cron Metrics Collector, Doctor Michel |

### 4.2 Crons LLM-driven (no_agent=false)

| Cron | Modèle | Fréquence | Rôle |
|------|--------|-----------|------|
| Unified Collector v2 | deepseek-v4-flash | */15 min | Collecte 10 sources KPI |
| Journaux Quotidiens | deepseek-v4-flash | 23h | 5 wikis + 5 vaults |
| Audit Rédactionnel | deepseek-v4-flash | 6h | 2 wikis, qualité markdown |

### 4.3 Dépendances critiques

- **drive-sync** → alimente **drive-issue** → visible dans dashboard
- **doc-watch-auto** → détecte changements → **docs-update** → **auto-commit**
- **rebuild-wiki / rebuild-voyages** → régénèrent les sites MkDocs
- **cron-metrics-collector** → alimente **cron-quality-audit-v2** → dashboard
- **energy-collect** → **energy-aggregate** → dashboard KPI

---

## 5. WIKIS & DOCUMENTATION

### 5.1 Wikis MkDocs

| Wiki | Dépôt GitHub | URL locale | URL publique |
|------|-------------|------------|--------------|
| BAVI_LEO | Tofdan/BAVI_LEO | `~/Projets_Dev/BAVI_LEO/docs/` | bavi.tofdan.be |
| hermes-wiki | Tofdan/hermes-wiki | `~/Projets_Dev/hermes-wiki/docs/` | hermes.tofdan.be |
| emile-wiki | Tofdan/emile-wiki | `~/Projets_Dev/emile-wiki/docs/` | emile.tofdan.be |
| voyages-wiki | Tofdan/voyages-wiki | `~/Projets_Dev/voyages-wiki/docs/` | voyages.tofdan.be |
| wiki-oca | Tofdan/wiki-oca | `~/Projets_Dev/wiki-oca/docs/` | oca.tofdan.be |

### 5.2 Règles wiki

- **Commit wiki** → **rebuild automatique** (cron toutes les 15min)
- **Docs modifiés** → **doc-watch** détecte → **docs-update** → **auto-commit**
- **Audit rédactionnel** scanne tous les .md actifs de hermes-wiki + BAVI_LEO
- Fichiers exclus de l'audit : `archives/`, `aller-plus-loin/`, `annexes/`, `AUDIT.md`, `TABLE.md`

---

## 6. GOOGLE WORKSPACE

### 6.1 Tokens OAuth

| Token | Compte Gmail | Usage |
|-------|-------------|-------|
| `leo_google_token.json` | `leodanhieria@gmail.com` | Envoi mails, backup, veille |
| `leo_sheets_token.json` | `christophe.danhier@gmail.com` | Classifieur inbox, check-gmail |
| `leo_drive_token.json` | Drive (pas Gmail) | Upload backup GDrive |

### 6.2 Règles tokens

- Refresh automatique toutes les 50 minutes (`refresh_google_tokens.py`)
- Vérifier le compte réel avec `gmail.users().getProfile()`, pas le nom du fichier
- Le champ OAuth est `token`, pas `access_token`
- Piège connu : `google_token_christophe.json` pointait vers `leodanhieria`

---

## 7. BUDGET & COÛTS

| Poste | Coût mensuel |
|-------|-------------|
| DeepSeek API | ~$30 |
| Total | ~$30/mois |

- Suivi via **Budget Alert** (2×/jour, 8h et 20h)
- Dashboard affiche le solde temps réel
- DeepSeek Pro = ~$2.50/M tokens ; Flash = ~$0.27/M tokens

---

## 8. SÉCURITÉ & RÈGLES

### 8.1 Tokens et credentials

- `$GAUTH` pour GitHub (jamais en clair)
- `$DEEPSEEK_API_KEY` dans `.env`
- `$OPENROUTER_API_KEY` dans `.env` (configuré, non utilisé)
- `leo-panel-2026` pour l'API dashboard
- Backup AVANT toute modification de config

### 8.2 Règles de déploiement

1. **STABILITÉ > features** — ne jamais casser ce qui marche
2. **Backup avant modification** — `jobs.json`, configs, scripts
3. **ZÉRO notification Telegram de routine** — dashboard = seul canal
4. **Preuve = site LIVE** — vérifier sur le site déployé, pas raw GitHub
5. **Var TOKEN → GAUTH** — utiliser `$GAUTH` pour GitHub

### 8.3 Pièges connus

- **Python 3.14** : `sqlite3` ne ferme plus les connexions dans `with conn:` → fuite FDs → crash gateway (corrigé le 24/07/2026 via `executions.py`)
- **Gateway restart impossible depuis l'intérieur** → utiliser `hermes gateway restart` depuis un shell extérieur
- **Fallback silencieux Pro→Flash** → supprimé pour tous les profils (24/07/2026)
- **Dashboard `last_status=ok` mais entries en `error`** → toujours vérifier les DEUX sources
- **allowed_chats vide** → gateway muette → `hermes config set telegram.allowed_chats <id>`
- **Cron LLM qui échoue** → convertir en `no_agent=true` + script bash

---

## 9. CYCLE DE VIE DES DONNÉES

```
[Sources]               [Collecte]            [Stockage]           [Dashboard]
────────────────────────────────────────────────────────────────────────────
HomeWizard P1 ────→ collect-energy.py ──→ energy_metrics.json ──→ Panel 8765
HA (caméras) ────→ camera-motion.py ────→ Telegram (alerte)
Viessmann ───────→ (paused) ────────────→ viessmann_metrics.json
Machine ─────────→ machine-kpi.py ──────→ metrics DB ──────────→ Panel 8765
Gmail ───────────→ check-gmail.py ──────→ Telegram (important)
Drive ───────────→ drive-sync.sh ───────→ GitHub (issue)
Crons ───────────→ cron-metrics-collector → cron_metrics.db ───→ Audit V2
```

---

## 10. ANALYSE — Forces & Faiblesses

### ✅ Forces

- **Multi-profils spécialisés** — 5 bureaux avec rôles distincts
- **Monitoring redondant** — Doctor Michel (30min) + Audit V2 (24h) + Watchdogs
- **Auto-correction** — Audit V2 détecte rate-limit, suggère changements de modèle
- **Métriques historiques** — 2500+ entrées, 11 jours, tendances 7j
- **Dashboards unifiés** — panel 8765 + Hermes 9119
- **Sauvegardes** — GDrive quotidien + recovery state horaire

### ❌ Faiblesses

- **Pas de collaboration inter-bureaux** — chaque bureau est un silo
- **Pas de hiérarchie** — pas de CEO qui supervise les managers
- **Pas de boucle d'auto-amélioration complète** — l'Audit V2 suggère mais n'applique pas automatiquement
- **Ontologie absente** — pas de source unique de vérité structurée (→ ce document)
- **Pas d'interface agentique visuelle** — le dashboard est passif

---

## 11. PLAN D'IMPLÉMENTATION — Améliorations BAVI

### Phase 1 — Fondations (court terme, faible risque)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1.1 | **Ontologie structurée** ← CE DOCUMENT | Élevé | ✅ Fait |
| 1.2 | Injecter l'ontologie dans les skills des bureaux | Moyen | 30 min |
| 1.3 | Cron Metrics Collector → DB (déjà fait) | Moyen | ✅ Fait |
| 1.4 | Audit Qualité V2 avec tendances 7j (déjà fait) | Élevé | ✅ Fait |

### Phase 2 — Boucle d'auto-amélioration (moyen terme)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 2.1 | Auto-fix : appliquer automatiquement les suggestions triviales | Élevé | 1h |
| 2.2 | Métriques de coût par cron (tokens consommés) | Moyen | 2h |
| 2.3 | Alertes proactives (avant la panne) | Élevé | 3h |

### Phase 3 — Collaboration & Hiérarchie (long terme)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 3.1 | Bureau CEO — supervise tous les bureaux | Très élevé | 4h |
| 3.2 | @mentions inter-bureaux — un bureau peut en appeler un autre | Très élevé | 6h |
| 3.3 | Pipeline multi-agents — workflow séquentiel entre bureaux | Très élevé | 8h |

### Phase 4 — Interface agentique (vision)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 4.1 | Dashboard live — voir les agents travailler en temps réel | Élevé | 10h |
| 4.2 | Chat intégré par bureau dans le dashboard | Moyen | 6h |
| 4.3 | Pôles visuels — un channel par bureau avec outputs | Moyen | 8h |

---

## 12. RÉFÉRENCES CROISÉES

| Ressource | Chemin |
|-----------|--------|
| Config Michel | `~/.hermes/profiles/michel/config.yaml` |
| Crons jobs.json | `~/.hermes/profiles/michel/cron/jobs.json` |
| Skills | `~/.hermes/profiles/michel/skills/` |
| Mémoire | `~/.hermes/profiles/michel/memories/` |
| Dashboard | `~/Projets_Dev/BAVI_LEO/server.py` |
| Metrics DB | `~/.hermes/metrics/cron_metrics.db` |
| Audit Qualité | `~/.hermes/metrics/cron-quality-audit.json` |
| Doctor Michel | `~/.hermes/profiles/michel/scripts/doctor-michel.py` |
| Backups | `~/.hermes/profiles/michel/backups/` |
| CREDENTIALS | `~/.hermes/CREDENTIALS.md` |
| SOUL Michel | `~/.hermes/profiles/michel/SOUL.md` |

---

*Document généré automatiquement par Michel (Bureau Infrastructure LEO) le 24 juillet 2026.*
*Contexte extrait de : mémoire Hermes, configs, jobs.json, skills, sessions historiques.*
*Prochaine mise à jour : après chaque changement d'infrastructure.*

> 🤖 Dernier audit : 30/07/2026 à 06:00 (UTC+2)

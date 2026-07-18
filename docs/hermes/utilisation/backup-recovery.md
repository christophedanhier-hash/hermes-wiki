# 💾 Backup & Recovery — État actuel (10/07/2026)

> **Mise à jour post-migration du 10/07/2026** — tous les chemins ont migré de `/opt/data/` vers `~/.hermes/`. Le backup inclut maintenant 29 chemins + hermes-christophe.

## 🔴 Restauration d'urgence — 10/07/2026 12:09

Le conteneur Docker LEO a été perdu. Restauration complète depuis le fichier `leo-full-backup-2026-07-10.tar.gz` (dans `~/Téléchargements/`).

### Déroulé

1. **Extraction** du backup dans `/tmp/leo-backup/`
2. **Restauration** des mémoires (`memories/`), skills, profils, config, .env, crons, scripts
3. **Correction** du symlink `SOUL.md` cassé → pointait sur `/opt/data/` qui n'existe plus
4. **Redémarrage** des 5 gateways (default, leo-copilot, bavi-leo, emile, bureau-robert)
5. **Ajustement** des chemins `OBSIDIAN_VAULT_PATH` dans les 4 `.env` (→ `~/.hermes/vault-*`)
6. **Backup de sauvegarde** immédiat : `leo-full-backup-2026-07-10_12-18.tar.gz` (93 Mo)

### Problèmes résolus

| Problème | Cause | Fix |
|----------|-------|-----|
| SOUL.md introuvable | Symlink → `/opt/data/profiles/default/SOUL.md` (inexistant) | Recréé vers `~/.hermes/profiles/default/SOUL.md` |
| Crons bloqués | Sans SOUL.md, le cron ne chargeait pas le profil | Symlink réparé + gateway redémarrée |
| Vaults inaccessibles | `OBSIDIAN_VAULT_PATH` → `/opt/data/vault-*` | Mis à jour vers `~/.hermes/vault-*` |
| Profiles absents | Backup extrait sans les dossiers `profiles/` | Copiés depuis `/tmp/leo-backup/profiles/` |

### État final (12:25)

| Service | Statut | Modèle |
|---------|--------|--------|
| **Léo** (default, toi ici) | ✅ Gateway actif | DeepSeek Flash |
| **Léo Copilote** (infra) | ✅ Gateway actif + 38 crons | DeepSeek Pro |
| **BAVI LEO Voyages** (Sylvia) | ✅ Gateway actif | DeepSeek Flash |
| **Émile** (pédagogique) | ✅ Gateway actif | DeepSeek Flash |
| **n8n**  | ❌ Retiré (13/07/2026) | — |
| **Ollama** | ✅ Docker (port 11434) | qwen2.5:7b |
| **Wikis publics** (5) | ✅ GitHub Pages — 10/07 10:00 | — |

### Leçons

- **Le symlink SOUL.md est le point de défaillance #1** — sans lui, le profil ne charge pas son identité et les crons échouent
- **memories/ est critique** — perte = perte d'identité de l'agent
- **Les paths doivent être absolus** — les `OBSIDIAN_VAULT_PATH` en `/opt/data/` plantent hors conteneur
- **Faire un backup immédiat après restauration** — protège l'état restauré

## Vue d'ensemble

| Destination | Format | Taille | Rétention | Fréquence |
|-------------|--------|--------|-----------|-----------|
| 🖥️ Local (`~/.hermes/backups/`) | `leo-full-backup-YYYY-MM-DD.tar.gz` | ~150 MB | 7 jours | Quotidien 06:00 |
| ☁️ Google Drive `Hermes_Christophe/Backups/` | `leo-full-backup-YYYY-MM-DD.tar.gz` | ~150 MB | Manuel (GDrive) | Quotidien 06:00 |

Le backup est **automatique et sans LLM** (mode `no_agent` = 0 token consommé).

## Ce qui est backupé

| Élément | Détail |
|---------|--------|
| ⚙️ Config Hermes | `config.yaml` (gateways, providers, crons) |
| 🔑 Tous les tokens OAuth | google_token, leo_google_token, leo_drive_token, leo_email_token, leo_sheets_token, gdrive-service-account |
| 🔐 Credentials vault | `credentials_vault.json` (tous les .env, secrets) |
| 📚 Skills Hermes | ~1022 fichiers, 22 skills actifs |
| 👤 **Tous les profils** | `profiles/default`, `profiles/leo-copilot`, `profiles/bavi-leo`, `profiles/emile` — configs, skills, memory, cron |
| 🏛️ Vaults Obsidian | `vault-leo`, `vault-default`, `vault-emile`, `vault-bavi` |
| 📜 Scripts personnalisés | ~106 scripts dans `scripts/` |
| 🧠 Session DB | `state.db` (~2.6 MB) — historique complet des conversations |
| 📋 Kanban | `kanban.db` — tâches et projets |
| 📊 Crons & jobs | `cron/` (jobs.json + historique des runs) |
| 🧠 Mémoires persistantes | `memories/` (USER.md, MEMORY.md) **— CRITIQUE** |
| 💫 SOUL.md | Fichier d'identité LEO |
| 📈 Métriques | `metrics/` (données dashboard KPI) |
| 🔧 hermes-christophe | `~/Projets_Dev/hermes-christophe/` — scripts BAVI + LEO (61 fichiers) |

## Cron associé

```json
{
  "Nom":       "LEO Backup quotidien → GDrive",
  "ID":        "55465c2cedde",
  "Horaire":   "0 6 * * *" (tous les jours à 06:00),
  "Script":    "leo-full-backup.py",
  "Mode":      "no_agent" (0 token LLM),
  "Deliver":   "local"
}
```

Le script :
1. Crée une archive tar.gz de **29 chemins** critiques + hermes-christophe
2. Sauvegarde localement dans `~/.hermes/backups/`
3. Upload sur Google Drive via OAuth (token `leo_google_token.json`)
4. Nettoie les backups locaux > 7 jours

## Recovery Kit — Couche 2 ✅

**Emplacement :** `/home/tofdan/.hermes/recovery-kit/`  
**Statut :** ✅ Créé le 10/07/2026

| Fichier | Rôle |
|---------|------|
| `README.md` | Documentation du kit |
| `rebuild.sh` | Script de reconstruction automatisé |
| `docker-commands.md` | Commandes exactes de recréation des conteneurs |
| `secrets.b64` | `.env` + tokens + configs (base64) |
| `secrets-manifest.txt` | Liste des fichiers dans l'archive |
| `checksums.sha256` | Intégrité du kit |

Le kit est **statique** : aucune modification du conteneur, pas de `--privileged`.

## Nettoyage et maintenance automatiques

Un cron de maintenance tourne tous les jours à **03:00** :

```json
{
  "Nom":       "LEO Maintenance quotidienne",
  "ID":        "af37c79fc7c5",
  "Horaire":   "0 3 * * *" (tous les jours à 03:00),
  "Script":    "leo-daily-maintenance.py",
  "Mode":      "no_agent" (0 token LLM)
}
```

Vérifications automatiques :
- ✅ Purge des outputs cron > 30 jours
- ✅ Détection de fichiers orphelins `_*.py` à la racine
- ✅ Vérification des symlinks cassés
- ✅ Détection de débris (`.bak`, `.dead`, fichiers coquille)
- ✅ Alerte espace disque

## Usage manuel

```bash
# Backup immédiat
~/.hermes/venv/bin/python3 ~/.hermes/profiles/leo-copilot/scripts/leo-full-backup.py

# Vérifier via cron
hermes cron list | grep backup
hermes cron run backup
```

## Procédure de restauration complète (PRA)

En cas de perte totale du serveur LEO, la restauration prend **~45 minutes**.

### Étape 1 — Installer Hermes (10 min)

```bash
apt update && apt upgrade -y
apt install -y python3 python3-pip python3-venv git curl wget

cd /opt
git clone https://github.com/nousresearch/hermes-agent.git
cd hermes-agent
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Étape 2 — Restaurer la config (5 min)

Télécharger le dernier backup depuis **Google Drive → Hermes_Christophe → Backups/** puis :

```bash
tar xzf leo-full-backup-YYYY-MM-DD.tar.gz -C /home/tofdan/.hermes/
chown -R tofdan:tofdan /home/tofdan/.hermes/
```

### Étape 3 — Restaurer les accès (5 min)

Le backup contient déjà tous les tokens. Vérifier :

```bash
ls ~/.hermes/*.json ~/.hermes/.env
```

Configurer GitHub :

```bash
gh auth login --with-token < ~/.hermes/leo_token.json
```

### Étape 4 — Vérifier les composants critiques

```bash
ls ~/.hermes/profiles/       # Doit montrer: default leo-copilot bavi-leo emile
ls ~/.hermes/vault-*/        # Doit montrer: vault-leo vault-default vault-emile vault-bavi
ls ~/.hermes/memories/       # Doit montrer: MEMORY.md USER.md ← CRITIQUE
ls ~/.hermes/state.db        # Sessions DB
```

### Étape 5 — Cloner les repos GitHub (15 min)

```bash
cd ~/Projets_Dev
for repo in BAVI_LEO hermes-wiki emile-wiki wiki-oca voyages-wiki hermes-christophe; do
    git clone "https://github.com/christophedanhier-hash/$repo.git"
done
```

### Étape 6 — Vérification (5 min)

```bash
# Dashboards en ligne ?
for url in hermes-wiki BAVI_LEO wiki-oca voyages-wiki emile-wiki; do
  curl -s -o /dev/null -w "$url: %{http_code}\n" \
    "https://christophedanhier-hash.github.io/$url/"
done
```

## État GDrive (10/07/2026)

| Backup | Taille | Date |
|--------|--------|------|
| leo-full-backup-2026-07-10.tar.gz | 181.8 MB | 10/07 04:01 |
| leo-full-backup-2026-07-09.tar.gz | 161.4 MB | 09/07 04:02 |
| leo-full-backup-2026-07-08.tar.gz | 148.7 MB | 08/07 04:01 |
| leo-full-backup-2026-07-07.tar.gz | 131.8 MB | 07/07 04:01 |
| leo-full-backup-2026-07-06.tar.gz | 120.4 MB | 06/07 04:01 |

## Points d'attention

- **Permissions** — après restauration, vérifier `chown -R tofdan:tofdan ~/.hermes/`
- **Rotation automatique** — ne pas désactiver (max 7 jours de rétention locale)
- **Test mensuel** — vérifier que les backups apparaissent dans Backups/ sur GDrive
- **Le token GDrive (`leo_google_token.json`) est inclus dans le backup** — il permet de restaurer et uploader les backups suivants
- **memories/ est critique** — sans USER.md et MEMORY.md, l'agent perd son identité (cause #1 du crash 30/06)
- **Recovery-kit** — régénérer `secrets.b64` après chaque modification du `.env`
- **Ne JAMAIS commit le recovery-kit** — il contient les secrets en clair

## Emplacement des fichiers

| Fichier | Chemin |
|---------|--------|
| Script de backup principal | `~/.hermes/profiles/leo-copilot/scripts/leo-full-backup.py` |
| Script de maintenance | `~/.hermes/profiles/leo-copilot/scripts/leo-daily-maintenance.py` |
| Backups locaux | `~/.hermes/backups/` |
| Backups GDrive | `Hermes_Christophe/Backups/` (ID: `1ljeXPcYa-F4CkD9L_q0DrLgxYLMiAOGR`) |
| Recovery Kit | `~/.hermes/recovery-kit/` |
| Skill DRP | `leo-backup-dr` (skill Hermes — infrastructure) |

*Document mis à jour le 10/07/2026 à 00:00 — LEO 🦁*

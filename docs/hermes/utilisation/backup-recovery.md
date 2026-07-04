# 💾 Backup & Recovery — État actuel (04/07/2026)

> **Mise à jour post-crash du 30/06/2026** — le backup a été révisé et simplifié. Plus de scripts obsolètes, plus de 17 crons, une seule archive complète, un seul cron.

## Vue d'ensemble

| Destination | Format | Taille | Rétention | Fréquence |
|-------------|--------|--------|-----------|-----------|
| 🖥️ Local (`/opt/data/backups/`) | `leo-full-backup-YYYY-MM-DD.tar.gz` | ~100 MB | 7 jours | Quotidien 06:00 |
| ☁️ Google Drive `Hermes_Christophe/Backups/` | `leo-full-backup-YYYY-MM-DD.tar.gz` | ~100 MB | 7 jours | Quotidien 06:00 |

Le backup est **automatique et sans LLM** (mode `no_agent` = 0 token consommé).

## Ce qui est backupé

| Élément | Détail |
|---------|--------|
| ⚙️ Config Hermes | `config.yaml` (gateways, providers, crons) |
| 🔑 Tous les tokens OAuth | google_token, leo_google_token, leo_drive_token, leo_email_token, leo_sheets_token, gdrive-service-account |
| 🔐 Credentials vault | `credentials_vault.json` (tous les .env, secrets) |
| 📚 Skills Hermes | ~990 fichiers, 22 skills actifs |
| 👤 **Tous les profils** | `profiles/default`, `profiles/leo-copilot`, `profiles/bavi-leo`, `profiles/emile` — configs, skills, memory, cron |
| 🏛️ Vaults Obsidian | `vault-leo`, `vault-default`, `vault-emile`, `vault-bavi` |
| 📜 Scripts personnalisés | ~123 scripts dans `scripts/` |
| 🧠 Session DB | `state.db` (~48 MB) — historique complet des conversations |
| 📋 Kanban | `kanban.db` |
| 📊 Crons & jobs | `cron/` (jobs.json + historique des runs) |
| 🧠 Mémoires persistantes | `memories/` (USER.md, MEMORY.md) |
| 💫 SOUL.md | Fichier d'identité LEO |

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
1. Crée une archive tar.gz de **27 chemins** critiques
2. Sauvegarde localement dans `/opt/data/backups/`
3. Upload sur Google Drive via OAuth (token `leo_drive_token.json`)
4. Nettoie les backups locaux > 7 jours

## Usage manuel

```bash
# Backup immédiat
/opt/hermes/.venv/bin/python3 /opt/data/scripts/leo-full-backup.py

# Vérifier via cron
hermes cron list | grep backup
hermes cron run backup
```

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

Télécharger le dernier backup depuis **Google Drive → Hermes_Christophe → Backups/** :

```bash
# Copier depuis Google Drive (téléchargement manuel ou via API)
# Puis extraire dans /opt/data/
tar xzf leo-full-backup-2026-07-04.tar.gz -C /opt/data/

# Permissions
chown -R hermes:hermes /opt/data/profiles /opt/data/state.db /opt/data/.env
```

### Étape 3 — Restaurer les accès (5 min)

Le backup contient déjà tous les tokens. Vérifier :

```bash
ls /opt/data/*.json /opt/data/.env
# Les tokens OAuth et credentials sont inclus dans l'archive
```

Configurer GitHub :

```bash
gh auth login --with-token < /opt/data/leo_token.json
# Ou recréer le token depuis l'interface GitHub
```

### Étape 4 — Restaurer skills et profils (5 min)

Les profils et skills sont dans l'archive extraite à l'étape 2. Vérifier :

```bash
ls /opt/data/profiles/
ls /opt/data/skills/ | wc -l
```

### Étape 5 — Cloner les repos GitHub (15 min)

```bash
cd /opt/data

# Wikis actifs
gh repo clone christophedanhier-hash/hermes-wiki
gh repo clone christophedanhier-hash/hermes-guide
gh repo clone christophedanhier-hash/BAVI_LEO
gh repo clone christophedanhier-hash/BAVI_PLUS
gh repo clone christophedanhier-hash/wiki-oca
gh repo clone christophedanhier-hash/voyages-wiki
gh repo clone christophedanhier-hash/emile-wiki

# Drive mirror
gh repo clone christophedanhier-hash/hermes-christophe
```

### Étape 6 — Recréer les crons (5 min)

Restaurer depuis le backup — les crons sont dans l'archive à l'étape 2. Vérifier :

```bash
cat /opt/data/cron/jobs.json | python3 -c "import json,sys; j=json.load(sys.stdin); [print(f'{jb[\"name\"]:40s} {jb[\"schedule\"][\"expr\"]:15s}') for jb in j['jobs']]"
```

**Crons actifs au 04/07/2026 :**

| Nom | Horaire | Script | Mode |
|-----|---------|--------|------|
| LEO Backup quotidien → GDrive | 0 6 * * * | `leo-full-backup.py` | no_agent |
| LEO Maintenance quotidienne | 0 3 * * * | `leo-daily-maintenance.py` | no_agent |
| LEO Health Check bots | */15 * * * * | `leo-health-check.py` | no_agent |
| vault-daily-journal | 0 23 * * * | (prompt + skill obsidian) | LLM |
| vault-default-daily-journal | 0 23 * * * | (prompt + skill obsidian) | LLM |

### Étape 7 — Vérification (5 min)

```bash
# Gateways actifs ?
hermes gateway list

# Dashboards en ligne ?
for url in hermes-wiki BAVI_LEO wiki-oca voyages-wiki emile-wiki hermes-guide; do
  curl -s -o /dev/null -w "$url: %{http_code}\n" \
    "https://christophedanhier-hash.github.io/$url/"
done
```

## Points d'attention

- **Permissions** — après restauration, vérifier `chown -R hermes:hermes /opt/data/`
- **Rotation automatique** — ne pas désactiver (max 7 jours de rétention)
- **Test mensuel** — vérifier que les backups apparaissent dans Backups/ sur GDrive
- **Le token GDrive (`leo_drive_token.json`) est inclus dans le backup** — il permet de restaurer et uploader les backups suivants
- **Anciens fichiers sur GDrive** — des fichiers individuels pré-crash (`.env`, `config.yaml`, etc.) traînent encore dans Backups/ mais n'interfèrent pas avec les nouvelles archives

## Emplacement des fichiers

| Fichier | Chemin |
|---------|--------|
| Script de backup principal | `/opt/data/scripts/leo-full-backup.py` |
| Script de maintenance | `/opt/data/scripts/leo-daily-maintenance.py` |
| Backups locaux | `/opt/data/backups/` |
| Backups GDrive | `Hermes_Christophe/Backups/` |
| Skill hygiène | `workspace-hygiene` (skill Hermes — infrastructure) |
| PRA complet | https://github.com/christophedanhier-hash/BAVI_LEO/blob/main/docs/wiki/agent-pro/bureau-michel/pra-leo-recovery-20260629.md |
*Document mis à jour le 04/07/2026 — 00:00:00 — Modèles DeepSeek unifiés 🦁*

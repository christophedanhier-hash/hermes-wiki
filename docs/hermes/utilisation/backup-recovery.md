# 💾 Backup & Recovery

## Vue d'ensemble

Un backup automatisé de LEO est effectué **tous les jours à 06:00** vers **Google Drive**.

| Destination | Format | Taille | Rétention |
|-------------|--------|--------|-----------|
| Google Drive `Hermes_Christophe/Backups/` | `leo-backup-YYYY-MM-DD.tar.gz` | ~20 MB | 7 jours |

## Ce qui est backupé

| Élément | Détail |
|---------|--------|
| ⚙️ Config Hermes | `config.yaml` (gateways, providers, crons) |
| 🔑 Tokens OAuth | google_token.json, leo_google_token.json |
| 🐙 Token GitHub | leo_token.json |
| 📚 Skills | ~150 skills Hermes (~8 MB) |
| 👤 Profile Bot | bavi-leo (profil voyages, ~56 MB) |
| 📜 Scripts personnalisés | Tous les scripts dans scripts/ |
| 📊 Métriques Dashboards | Bases de données metrics/ |

## Cron associé

```
Nom :      daily-backup
Horaire :  06:00 quotidien
Script :   run-backup.sh → leo-backup.py
Mode :     no_agent (0 token LLM)
```

Le cron utilise `no_agent=True` : le script s'exécute directement, sans LLM.

## Usage manuel

```bash
# Backup immédiat
/opt/hermes/.venv/bin/python3 /opt/data/scripts/leo-backup.py

# Lister les backups sur Drive
/opt/hermes/.venv/bin/python3 /opt/data/scripts/leo-backup.py --list

# Forcer le nettoyage (rotation)
/opt/hermes/.venv/bin/python3 /opt/data/scripts/leo-backup.py --prune
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

Télécharger le dernier backup depuis **Google Drive → Hermes_Christophe → Backups/** et extraire :

```bash
tar xzf leo-backup-2026-06-18.tar.gz -C /opt/data/
```

### Étape 3 — Restaurer les accès (5 min)

```bash
# Copier les tokens OAuth
cp /opt/data/leo/google_token.json /opt/data/google_token.json
cp /opt/data/leo/leo_google_token.json /opt/data/leo_google_token.json

# Restaurer le token GitHub
cat /opt/data/leo/leo_token.json
# Copier la valeur : gh auth login --with-token
```

### Étape 4 — Restaurer skills et profils (5 min)

```bash
cp -r /opt/data/leo/skills/ /opt/data/skills/
cp -r /opt/data/leo/profiles/ /opt/data/profiles/
cp -r /opt/data/leo/scripts/ /opt/data/scripts/
cp -r /opt/data/leo/metrics/ /opt/data/metrics/
```

### Étape 5 — Cloner les 13 repos GitHub (15 min)

```bash
cd /opt/data

# Wikis
gh repo clone christophedanhier-hash/hermes-wiki
gh repo clone christophedanhier-hash/BAVI_LEO
gh repo clone christophedanhier-hash/wiki-oca
gh repo clone christophedanhier-hash/voyages-wiki

# Dashboards
gh repo clone christophedanhier-hash/dashboard-leo
gh repo clone christophedanhier-hash/leo-metrics
gh repo clone christophedanhier-hash/crons-dashboard
gh repo clone christophedanhier-hash/github-dashboard
gh repo clone christophedanhier-hash/bavi-leo-dashboard

# Drive mirror
gh repo clone christophedanhier-hash/hermes-christophe

# Autres
gh repo clone christophedanhier-hash/hermes-guide
gh repo clone christophedanhier-hash/dashboard-kpi
gh repo clone christophedanhier-hash/machine-metrics
```

### Étape 6 — Recréer les crons (5 min)

Liste des 17 crons à restaurer. La config Hermes dans `~/.hermes/` est restaurée à l'étape 2.

Vérifier avec : `hermes cron list`

### Étape 7 — Vérification (5 min)

```bash
# Gateways actifs ?
hermes gateway list

# Dashboards en ligne ?
for url in hermes-wiki BAVI_LEO wiki-oca voyages-wiki; do
  curl -s -o /dev/null -w "$url: %{http_code}\n" \
    "https://christophedanhier-hash.github.io/$url/"
done

# Sync scripts — exécuter manuellement
/opt/data/scripts/wiki-sync.py          # Guide → wiki LEO
/opt/data/scripts/t600-drive-sync.py    # T600 → wiki OCA
```

## Points d'attention

- **Permissions root** — certains fichiers skills sont en `root:root`, le script les ignore proprement
- **Rotation automatique** — ne pas désactiver (max 7 backups conservés)
- **Test mensuel** — exécuter `--list` pour vérifier la présence des backups

## Emplacement des fichiers

| Fichier | Chemin |
|---------|--------|
| Script de backup | `/opt/data/scripts/leo-backup.py` |
| Wrapper cron | `/opt/data/scripts/run-backup.sh` |
| Skill DR | `leo-backup-dr` (skill Hermes) |

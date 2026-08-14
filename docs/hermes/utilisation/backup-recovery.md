# 💾 Backup & Recovery — Plan de Reprise d'Activité LEO

> **Dernière mise à jour : 02/08/2026** — Audit complet, 32 901 fichiers sauvegardés, recovery-kit régénéré (clés OpenRouter (non actif en prod) + Gemini incluses).

## Synthèse

| Indicateur | Valeur |
|-----------|--------|
| Dernier backup | 2026-08-02 06:02 |
| Taille archive | 606 MB |
| Fichiers sauvegardés | 32 901 |
| RTO estimé | ~45 minutes |
| Destination | Google Drive (5 To) + HDD local (1 To) |
| Fréquence | Quotidienne (06:00 CEST) |

## Ce qui est sauvegardé

### Profils Hermes

| Profil | Fichiers | Contenu |
|--------|:-------:|---------|
| default (LEO) | 36 | Bot principal, config, tokens |
| michel | 15 336 | Scripts, skills, sessions, logs |
| sylvia | 3 101 | Agence voyage, roadbooks |
| emile | 723 | Assistant pédagogique |
| robert | 10 760 | Conseil stratégique |

### Vaults Obsidian

| Vault | Fichiers | Dailies |
|-------|:-------:|:-------:|
| vault-michel | 29 | 21 |
| vault-default | 36 | 28 |
| vault-emile | 36 | 28 |
| vault-sylvia | 37 | 28 |
| vault-robert | 17 | 13 |

### Autres

| Catégorie | Fichiers | Statut |
|-----------|:-------:|:------:|
| Tokens Google OAuth | 6 JSON | ✅ |
| Config (.env, config.yaml) | 2 | ✅ |
| Bases (state.db, kanban.db) | 2 | ✅ |
| Skills | 1 225 | ✅ |
| Scripts (via profiles/michel/) | 123+ | ✅ |
| Crons (jobs + outputs) | 356 | ✅ |
| Memories | 4 | ✅ |
| Metrics (incl. benchmark.db) | 46 | ✅ |
| hermes-christophe | 1 130 | ✅ |

### Non sauvegardé (reconstruit depuis GitHub)

| Élément | Méthode | Temps |
|---------|---------|:-----:|
| BAVI_LEO | git clone | 2 min |
| hermes-wiki | git clone | 1 min |
| emile-wiki | git clone | 1 min |
| wiki-oca | git clone | 1 min |
| voyages-wiki | git clone | 1 min |
| Docker (HA, Ollama) | docker-compose | 10 min |

## Recovery Kit

Emplacement : `/home/tofdan/.hermes/recovery-kit/`

| Fichier | Rôle | Dernière màj |
|---------|------|:------------:|
| `secrets.b64` | Archive des secrets (tokens, .env, configs) | **02/08/2026** |
| `rebuild.sh` | Script de reconstruction automatisé | 10/07/2026 |
| `checksums.sha256` | Vérification d'intégrité | **02/08/2026** |
| `docker-commands.md` | Commandes Docker | 10/07/2026 |
| `secrets-manifest.txt` | Liste des fichiers dans secrets.b64 | 10/07/2026 |
| `README.md` | Documentation | 10/07/2026 |

**Contenu de secrets.b64** : .env (DeepSeek, Gemini, OpenRouter, Telegram, GitHub), config.yaml, credentials_vault.json, gateway_state.json, 5 tokens OAuth Google, 5 profils/.env.

## Cron associé

    Nom :     💾 LEO Backup quotidien → GDrive (script)
    Horaire : 0 6 * * * (06:00)
    Script :  leo-full-backup.py
    Mode :    no_agent (0 token LLM)

Le script :
1. Crée une archive tar.gz des chemins critiques + hermes-christophe
2. Sauvegarde localement dans `~/.hermes/backups/`
3. Upload sur Google Drive via OAuth (token `leo_google_token.json`)
4. Mirror HDD → `/mnt/data/backups/hermes/`
5. Rotation automatique 7 jours sur les 3 destinations

## Maintenance automatique

Cron quotidien 03:00 (`leo-daily-maintenance.py`, no_agent) :

    Nom :     🔧 LEO Maintenance quotidienne
    Horaire : 0 3 * * * (03:00)

Vérifications : purge outputs cron > 30 jours, détection fichiers orphelins, symlinks cassés, débris (.bak, .dead), dossiers vides, alerte espace disque.

## Procédure de restauration complète (PRA)

En cas de perte totale du serveur, restauration en **~45 minutes**.

### Étape 1 — Installer l'environnement (10 min)

    apt update && apt upgrade -y
    apt install -y python3 python3-pip python3-venv git curl wget
    cd /opt
    git clone https://github.com/nousresearch/hermes-agent.git
    cd hermes-agent
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -e .

### Étape 2 — Restaurer les données (5 min)

Télécharger le dernier backup depuis Google Drive → Hermes_Christophe → Backups/ puis :

    tar xzf leo-full-backup-YYYY-MM-DD.tar.gz -C /home/tofdan/.hermes/
    chown -R tofdan:tofdan /home/tofdan/.hermes/

### Étape 3 — Restaurer les secrets (2 min)

    cd /home/tofdan/.hermes/recovery-kit
    base64 -d secrets.b64 | tar xz -C /home/tofdan/.hermes/
    chmod 600 /home/tofdan/.hermes/.env
    chmod 600 /home/tofdan/.hermes/credentials_vault.json
    sha256sum -c checksums.sha256

### Étape 4 — Configurer GitHub (2 min)

    cat /home/tofdan/.hermes/leo_token.json
    gh auth login --with-token < /home/tofdan/.hermes/leo_token.json

### Étape 5 — Cloner les repos (15 min)

    cd ~/Projets_Dev
    for repo in BAVI_LEO hermes-wiki emile-wiki wiki-oca voyages-wiki; do
        git clone "https://github.com/christophedanhier-hash/$repo.git"
    done

### Étape 6 — Vérifier l'intégrité (5 min)

    ls /home/tofdan/.hermes/profiles/
    ls /home/tofdan/.hermes/vault-*/
    ls /home/tofdan/.hermes/memories/

### Étape 7 — Restaurer Docker (5 min)

    docker-compose -f ~/docker-compose.yml up -d

### Étape 8 — Vérification finale (1 min)

    hermes gateway list
    curl -s -o /dev/null -w "BAVI: %{http_code}" http://100.92.102.28:8765/

## Vérifications périodiques

| Fréquence | Action |
|-----------|--------|
| Quotidienne | Vérifier backup local (cron 06:00) |
| Hebdomadaire | Vérifier présence sur GDrive |
| Mensuelle | Tester restauration complète |
| Après nouveau profil/vault | Vérifier PATHS dans le script |

## Maintenance du recovery-kit

Après tout ajout de clé API ou modification du `.env` :

    cd /home/tofdan/.hermes
    tar czf - .env config.yaml credentials_vault.json gateway_state.json \
      leo_google_token.json leo_sheets_token.json leo_drive_token.json \
      gdrive-service-account.json google_client_secret.json \
      profiles/default/.env profiles/michel/.env profiles/sylvia/.env \
      profiles/emile/.env profiles/robert/.env |
      base64 > recovery-kit/secrets.b64
    cd recovery-kit
    sha256sum secrets.b64 rebuild.sh README.md docker-commands.md secrets-manifest.txt > checksums.sha256

## Historique

| Date | Action |
|------|--------|
| 30/06/2026 | Crash — perte totale des sessions et mémoire |
| 05/07/2026 | Mise en place backup GDrive quotidien |
| 10/07/2026 | Création recovery-kit, restauration post-migration |
| 16/07/2026 | Correction bug croissance exponentielle (backups/ dans PATHS) |
| 22/07/2026 | Ajout profils sylvia, emile, robert |
| 02/08/2026 | Audit complet + régénération secrets.b64 (OpenRouter, Gemini, benchmark.db) |

## Emplacement des fichiers

| Fichier | Chemin |
|---------|--------|
| Script de backup | `~/.hermes/profiles/michel/scripts/leo-full-backup.py` |
| Script de maintenance | `~/.hermes/profiles/michel/scripts/leo-daily-maintenance.py` |
| Backups locaux | `~/.hermes/backups/` |
| Backups GDrive | `Hermes_Christophe/Backups/` (ID: `1ljeXPcYa-F4CkD9L_q0DrLgxYLMiAOGR`) |
| Recovery Kit | `~/.hermes/recovery-kit/` |
| Document BAVI complet | [bureau-leo/pra-backup-disaster-recovery](http://100.92.102.28:8765/wiki/agent-pro/bureau-leo/pra-backup-disaster-recovery/) |

*Document mis à jour le 02/08/2026 — Michel (Chef Infrastructure LEO)*
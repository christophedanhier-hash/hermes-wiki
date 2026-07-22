# Multi-bots : pourquoi 3 bots valent mieux qu'un

LEO ne tourne pas avec un seul bot Telegram, mais avec **cinq bots spécialisés**. Chaque bot a son propre profil Hermes, son propre modèle, son propre rôle — et ils communiquent entre eux.

## Pourquoi plusieurs bots ?

Un seul bot peut tout faire. Alors pourquoi en créer plusieurs ?

### 1. Séparation des responsabilités

``` 
Un seul bot                                                 5 bots spécialisés
┌─────────────────────┐           ┌──────────┐ ┌──────────┐ ┌──────────┐
│ 🦁 LEO              │           │ 🦁 LEO   │ │ 🔧       │ │ 🧭       │
│                     │           │ Central  │ │ Copilote │ │ Sylvia   │
│ • Analyses          │           │          │ │          │ │          │
│ • Emails            │    →      │ Hub      │ │ Infra    │ │ Voyages  │
│ • Infra             │           │ général  │ │ Système  │ │ Roadbooks│
│ • Voyages           │           └──────────┘ └──────────┘ └──────────┘
│ • Mémoire           │
└─────────────────────┘
```

Avec un seul bot, tout est mélangé. Avec plusieurs bots :
- **default** : le hub central, votre premier interlocuteur — analyses, emails, classification, documentation
- **leo-copilot** : l'ingénieur infrastructure — crons, dashboards, scripts Python, budget, système (root sudo) — gère tous les crons (41 jobs, 39 actifs)
- **bureau-robert** : le consultant stratégique — analyses IT, recommandations
- **bavi-leo** (Sylvia) : la voyageuse — roadbooks camping-car, itinéraires, cartes OSM
- **emile** : l'assistant pédagogique — mémoire, création de contenu

### 2. Modèles adaptés à chaque usage

| Bot | Modèle principal | Coût | Usage typique |
|:----|:-----------------|:----:|:--------------|
| default | DeepSeek V4 Flash | Payant (faible) | Quotidien, polyvalent |
| leo-copilot | DeepSeek V4 Pro | Payant (faible) | Analyses complexes, infra |
| bavi-leo | DeepSeek V4 Flash | Payant (faible) | Roadbooks, voyages |
| bureau-robert | DeepSeek V4 Pro | Payant (faible) | Conseil stratégique IA |
| emile | DeepSeek V4 Flash | Payant (faible) | Pédagogie, mémoire |
| (fallback) | Gemini 3.5 Flash + Ollama qwen2.5:7b | Gratuit | Si DeepSeek indisponible |

### 3. Isolation des tokens et permissions

Chaque bot a son propre token Telegram. Si un token est compromis ou rate-limity, les autres bots continuent de fonctionner.

```
default.env
├── TELEGRAM_BOT_TOKEN=...  ← default
├── TELEGRAM_ALLOWED_USERS=...

leo-copilot.env
├── TELEGRAM_BOT_TOKEN=...  ← leo-copilot
├── TELEGRAM_ALLOWED_USERS=...

bavi-leo.env
├── TELEGRAM_BOT_TOKEN=...  ← bavi-leo (Sylvia)
├── TELEGRAM_ALLOWED_USERS=...

bureau-robert.env
├── TELEGRAM_BOT_TOKEN=...  ← bureau-robert
├── TELEGRAM_ALLOWED_USERS=...

emile.env
├── TELEGRAM_BOT_TOKEN=...  ← emile
├── TELEGRAM_ALLOWED_USERS=...
```

## Architecture des profils

### Créer un profil

```bash
hermes profile create leo-copilot
```

Cette commande crée un dossier `~/.hermes/profiles/leo-copilot/` avec un `config.yaml` vierge et prépare l'alias `leo-copilot` (vous pourrez utiliser `leo-copilot chat` directement).

### Structure d'un profil

```bash
~/.hermes/profiles/leo-copilot/
├── config.yaml        # Modèle, provider, outils, permissions
├── .env               # Token Telegram, clés API (gardé secret)
├── SOUL.md            # Personnalité, règles, contexte permanent
├── memories/          # Mémoire persistante (MEMORY.md + USER.md)
├── skills/            # Skills synchronisés depuis le profil source
├── cron/              # Tâches planifiées propres à ce profil
└── sessions/          # Historique des conversations
```

### Le fichier SOUL.md

C'est le cœur de la personnalité du bot. Il définit qui il est, ce qu'il fait et comment il se comporte.

```markdown
# Léo Copilote — Infrastructure

Tu es Léo Copilote, l'ingénieur infrastructure de l'écosystème LEO.

Tu gères :
- 41 crons automatisés (39 actifs, 2 en pause)
- 1 dashboard unifié
- scripts Python (ex-n8n, workflows migrés le 13/07/2026)
- Les gateways Hermes
- Le budget DeepSeek

Tu as accès root complet (sudo) sur la machine.
```

### Fichier config.yaml

Exemple de configuration pour un profil spécialisé infra :

```yaml
model:
  default: deepseek-v4-pro        # Modèle puissant pour l'infra
  provider: deepseek
fallback_providers: '[{"provider": "gemini", "model": "gemini-3.5-flash"}]'
display:
  language: fr
timezone: Europe/Brussels
```

## Communication entre profils

Les profils peuvent partager des informations de plusieurs façons :

### 1. Mémoire partagée (symlinks)

\`\`\`bash
# Les deux profils pointent vers les mêmes fichiers
ln -s ~/.hermes/memories/MEMORY.md ~/.hermes/profiles/leo-copilot/memories/MEMORY.md
ln -s ~/.hermes/memories/USER.md ~/.hermes/profiles/leo-copilot/memories/USER.md
\`\`\`

Quand un bot met à jour sa mémoire, l'autre voit les changements automatiquement.

### 2. SOUL.md — L'alignement TUI ↔ Telegram

**Problème critique :** Hermes charge le SOUL.md depuis \`$HERMES_HOME/SOUL.md\` (mécanisme interne dans \`agent/prompt_builder.py\`). Tous les profils qui partagent le même \`$HERMES_HOME\` chargent **exactement le même fichier** — quel que soit le profil actif.

```python
# Dans agent/prompt_builder.py
def load_soul_md(...):
    soul_path = get_hermes_home() / "SOUL.md"  # ← MÊME chemin pour tous les profils
```

Si le fichier racine n'est pas synchronisé avec le profil, **TUI et Telegram chargent des personnalités différentes**.

**Solution : un symlink unique**

```bash
# 1 fichier source de vérité
rm -f ~/Projets_Dev/SOUL.md
ln -s ~/.hermes/profiles/<profil>/SOUL.md ~/Projets_Dev/SOUL.md
```

Pour les profils qui partagent la même identité (ex: default + leo-copilot sont tous deux LEO) : **un seul SOUL.md unifié** avec un tableau des rôles, et les deux profils symlinkent vers le même fichier :

```bash
# Les 3 chemins pointent vers le même inode
ln -sf ~/.hermes/profiles/default/SOUL.md ~/Projets_Dev/SOUL.md
ln -sf ~/.hermes/profiles/default/SOUL.md ~/.hermes/profiles/leo-copilot/SOUL.md
```

Structure du SOUL.md unifié :
```markdown
## Rôles des profils

| Profil | Moteur | Rôle |
|--------|--------|------|
| **\`default\`** | DeepSeek Flash | Dialogue — échange, ne touche pas à l'infrastructure |
| **\`leo-copilot\`** | DeepSeek Pro | Infra — crons, dashboard, scripts, déploiements |

- Si tu es \`default\` → interface de dialogue
- Si tu es \`leo-copilot\` → chef d'infrastructure
```

**Vérification :**
```bash
stat -L -c "%n → inode %i" ~/Projets_Dev/SOUL.md ~/.hermes/profiles/*/SOUL.md
# Tous doivent montrer le MÊME inode
```

**⚠️ Quand NE PAS unifier :** les profils avec des personnalités différentes (Sylvia voyage ≠ Émile pédagogie) gardent leur propre SOUL.md indépendant. Seuls les profils qui sont la **même personne avec un modèle différent** partagent un SOUL.md unifié.

### 3. Skills synchronisés

Le profil principal (source de vérité) synchronise ses skills vers les autres profils toutes les 30 minutes :

```bash
# Sync automatique intégrée à Hermes (curator)
# Le profil default = source → pousse vers leo-copilot, bavi-leo, emile
```

### 3. Délégation de tâches

LEO (hub central) peut déléguer des tâches complexes à Léo Copilote :

```yaml
# Dans le config.yaml de Léo Copilote
delegation:
  model: deepseek-v4-pro
  max_concurrent_children: 3
  max_spawn_depth: 1
  orchestrator_enabled: true
```

## Exemple réel : l'écosystème LEO

| Profil | Bot Telegram | Modèle | Rôle | 
|:-------|:-------------|:-------|:-----|
| `default` | LEO 🦁 | DeepSeek V4 Flash | Hub central — analyses, emails, docs |
| `leo-copilot` | Léo Copilote 🦁 | DeepSeek V4 Pro | Infrastructure — crons, système, budget |
| `bavi-leo` | Sylvia 🚐 | DeepSeek V4 Flash | Roadbooks camping-car, voyages |
| `emile` | Émile 🎓 | DeepSeek V4 Flash | Assistant pédagogique mémoire |
| `bureau-robert` | Robert 🏛️ | DeepSeek V4 Pro | Conseil stratégique IA |

*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

> 🤖 Dernier audit : 22/07/2026 à 07:26 (UTC+2)


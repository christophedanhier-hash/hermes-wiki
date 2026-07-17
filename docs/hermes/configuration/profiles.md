# Profils, gateways et skills

## Profils

Un **profil** est une instance isolée d'Hermes avec sa propre configuration, ses propres clés API, sa mémoire et ses sessions. Chaque profil devient aussi une commande séparée.

```bash
# Créer un profil → crée aussi l'alias "mon-profil"
hermes profile create mon-profil

# Utiliser le profil
mon-profil chat           # alias complet
hermes -p mon-profil chat # flag explicite
```

Structure d'un profil dans `~/.hermes/profiles/<nom>/` :

```
~/.hermes/profiles/mon-profil/
├── config.yaml     # Modèle, provider, outils
├── .env            # Clés API, tokens
├── SOUL.md         # Personnalité
├── memories/       # Mémoire persistante
├── skills/         # Skills dédiés
├── sessions/       # Sessions du profil
├── cron/           # Tâches planifiées
└── logs/           # Logs
```

### Règle LEO : architecture multi-profils

> *"5 profils spécialisés, 1 mémoire unifiée."*

LEO utilise **5 profils Hermes**, chacun avec son propre bot Telegram et sa spécialisation :

| Profil | Rôle | Modèle | Mémoire |
|--------|------|--------|---------|
| `default` | Dialogue quotidien | DeepSeek Flash | Partagée avec leo-copilot |
| `leo-copilot` | Infrastructure & crons | DeepSeek Pro | Partagée avec default |
| `bavi-leo` | Voyages (Sylvia) | DeepSeek Flash | Séparée |
| `emile` | Création contenu | DeepSeek Flash | Séparée |
| `bureau-robert` | Conseil Stratégique IA | DeepSeek Pro | Séparée |

- **Mémoire unifiée** entre `default` et `leo-copilot` (deux profils, un cerveau)
- **Crons** : 39 dans `leo-copilot` exclusivement. Règle « ZÉRO hors leo-copilot » respectée (emile=0, bavi-leo=0, default=0).
- **Zéro duplication** de config — chaque profil a son `.env` et `config.yaml`

| Propriété | Configuration | Description |
|-----------|--------------|-------------|
| **Modèle** | `model.default` | LLM principal (ex: `deepseek-v4-flash`) |
| **Provider** | `model.provider` | Fournisseur (ex: `deepseek`, `openrouter`) |
| **Gateway** | `gateways.telegram.bot_token` | Token du bot Telegram |
| **Outils** | `hermes tools` | Toolsets activés par plateforme |
| **Skills** | `hermes skills install <id>` | Procédures chargées automatiquement |

### Commandes profils

```bash
# Lister les profils
hermes profile list

# Créer un profil (vide)
hermes profile create mon-profil

# Créer avec clonage de la config actuelle
hermes profile create mon-profil --clone

# Créer en clonant depuis un autre profil
hermes profile create mon-profil --clone-from default

# Utiliser un profil par défaut
hermes profile use mon-profil

# Voir les détails
hermes profile show mon-profil

# Supprimer
hermes profile delete mon-profil

# Renommer
hermes profile rename ancien nouveau

# Exporter / Importer (tar.gz)
hermes profile export mon-profil
hermes profile import archive.tar.gz

# Lancer avec un profil spécifique
hermes -p mon-profil chat
hermes -p mon-profil chat -q "Bonjour"
```

## Gateways

Un **gateway** est le canal par lequel vous communiquez avec votre assistant.

### Gateway Telegram (recommandé)

Permet de parler à votre assistant depuis votre téléphone.

1. Créez un bot Telegram via [@BotFather](https://t.me/botfather)
2. Notez le token du bot
3. Configurez dans config.yaml :

```yaml
gateways:
  telegram:
    bot_token: "******"
    allowed_users:
      - "votre_username"
      - 123456789  # Votre user ID Telegram
```

4. Lancez le gateway :

```bash
hermes gateway start
```

### Gateway Discord

```yaml
gateways:
  discord:
    bot_token: "******"
```

### Gateway local (terminal)

```bash
# Mode terminal interactif (aucune configuration)
hermes
# ou : hermes chat
```

## Skills

Les **skills** sont des procédures que l'assistant charge pour savoir comment effectuer des tâches spécifiques. C'est la mémoire procédurale de votre assistant.

### Structure d'un skill

Un skill est un fichier `SKILL.md` dans le dossier `skills/` :

```markdown
---
name: mon-skill
description: "Faire X quand Y se produit"
---

# Mon Skill

## Quand l'utiliser
Quand [condition], faire [action].

## Procédure
1. Étape 1
2. Étape 2
3. Vérifier le résultat

## Pièges
- Attention à [piège connu]
```

### Skills essentiels (exemple LEO)

| Skill | Description |
|-------|-------------|
| `living-documentation` | Tenir la documentation à jour |
| `budget-tracking` | Suivi des coûts LLM |
| `leo-architecture` | Architecture et règles de fonctionnement |
| `routage-llm` | Quel LLM utiliser pour quelle tâche |
| `system-management` | Gestion des machines distantes |

### Bonnes pratiques

- **Un skill = une responsabilité** (pas de fourre-tout)
- **Versionnez** les skills (ils évoluent avec votre assistant)
- **Stockez les corrections dans les skills**, pas en mémoire passagère
- **Patchez** un skill obsolète plutôt que d'en créer un nouveau

## Pour aller plus loin

- [Documentation Hermes : Skills](https://hermes-agent.nousresearch.com/docs)
- Voir `02-configuration/providers.md` pour la configuration LLM
- Voir `exemples/LEO.md` pour l'architecture complète
*Document mis à jour le 17/07/2026 — Léo 🦁*

---
> 🤖 Dernier audit : 17/07/2026 à 22:30 (UTC+2) — 5 profils confirmés, 39 crons leo-copilot exclusif, emile/bavi-leo=0 confirmé
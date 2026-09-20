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

> **Page canonique de référence :** [`hermes/architecture.md`](../architecture.md). Mesures vérifiées le **20/09/2026**.

LEO repose sur une architecture multi-profils isolée (mémoire, sessions, configuration et `.env` propres à chaque profil). **Six profils opérationnels** ont été mesurés le 20/09/2026 :

| Profil | Rôle | Provider principal | Modèle configuré | Fallback déclaré | Interface / Gateway |
|---|---|---|---|---|---|
| `default` | LEO, dialogue et pilotage général | Azure Foundry | `gpt-5.6-luna` | Google Gemini | Gateway Hermes (DM Telegram) |
| `michel` | Infrastructure, crons et déploiements | Azure Foundry | `gpt-5.6-luna` | `custom:google/gemini-3.7-flash` | Bot Telegram dédié |
| `robert` | Conseil stratégique | Azure Foundry | `gpt-5.6-luna` | Google Gemini | Bot Telegram dédié |
| `sylvia` | Voyages et roadbooks | OpenRouter | `meta/muse-spark-1.3-contributor` | Selon configuration | Bot Telegram dédié |
| `emile` | Assistant professionnel Émilie (My Émile IA Workbench) | Azure Foundry | `gpt-5.6-luna` | Google Gemini | Bot Telegram dédié |
| `gerard` | Astronomie, astrophotographie, site tofdan et documentation | Azure Foundry | `gpt-5.6-luna` | Google Gemini | Profil opérationnel |

> **Notes clés sur les profils :**
>
> - **LEO est un agent Hermes** (profil `default`), pas un bot Telegram autonome ; son accès s'effectue via le gateway Hermes sans handle Telegram inventé.
> - **`leo` est l'alias Hive du profil `default`**, et non un septième profil distinct.
> - **Gérard** est un profil opérationnel dédié à l'astronomie, à l'astrophotographie, au site tofdan et à la documentation générale, avec son étude comme guide astronomie (le projet T600/OCA étant un volet parmi d'autres ; aucun bot Telegram inventé si non prouvé).
> - **Crons Michel :** 72 jobs planifiés au 20/09/2026 dans `~/.hermes/profiles/michel/cron/jobs.json` (71 activés, 70 `no_agent`, 2 pilotés par un LLM).
> - **Incident d'infrastructure suivi séparément :** l'unité systemd Michel est observée en boucle d'auto-restart car un PID est déjà actif. Cet incident relève de l'infrastructure et n'est pas masqué dans la documentation.
> - **Note historique (datée) :** Le profil `bureau-robert` a été renommé en `robert` lors de la consolidation de juillet 2026. Le profil `emile` a initialement soutenu la formation et le mémoire de fin d'études avant d'évoluer vers le workbench professionnel My Émile IA (développé via Avenyra). Le profil `gerard` a été documenté initialement sur le projet T600/OCA avant la prise en compte complète de ses activités d'astronomie et du site tofdan. La configuration de juillet 2026 utilisait initialement DeepSeek avant la bascule vers Azure Foundry.

| Propriété | Configuration | Description |
|-----------|--------------|-------------|
| **Modèle** | `model.default` | Modèle LLM configuré (ex: `gpt-5.6-luna`) |
| **Provider** | `model.provider` | Fournisseur principal (ex: `azure`, `openrouter`) |
| **Fallback** | `fallback_providers` | Fournisseur de secours déclaré (ex: Google Gemini) |
| **Gateway** | `gateways.telegram.bot_token` | Token du bot Telegram (pour les profils avec gateway) |
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
- Voir [`providers.md`](providers.md) pour la configuration des providers LLM
- Voir [`dashboards.md`](../utilisation/dashboards.md) pour les interfaces et le monitoring
- Voir [`architecture.md`](../architecture.md) pour l'état canonique de référence

---

> 🤖 Dernière mesure vérifiée : **20/09/2026** — LEO et Michel. Source de vérité : `~/.hermes/profiles/*/config.yaml` et `architecture.md`.

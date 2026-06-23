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

### 🏛️ L'Architecture Multi-Profils LEO — Un seul "Cerveau" répliqué

Contrairement à l'adage d'origine *"un seul profil"*, l'écosystème LEO a évolué pour s'appuyer sur **trois profils isolés et actifs simultanément**, chacun étant optimisé pour un domaine précis de réflexion et doté de son propre Gateway Telegram :

| Profil | Bot Telegram associé | Moteur Principal (LLM) | Mission & Rôle |
| :--- | :--- | :---: | :--- |
| **`default`** (H) | `@hermes_leo_bot` | **DeepSeek Flash** | **Dialogue Principal & Général** — Rapide, disponible 24/7 et très économique. |
| **`leo-copilot`** | `@hermes_leo_copilot_bot` | **Gemini 3.5 Flash** | **Infrastructure & Réflexion Technique** — N8n, serveurs, Code-Server, diagnostics, scripts et dashboards. Plus puissant en réflexion. |
| **`bavi-leo`** | `@bavi_leo_voyages_bot` | **DeepSeek Flash** | **Bureaux & Activités Spécialisés** — Conseil (Robert), Finance (Sophie), Technique (Gérard), Voyages (Sylvie/bot voyages dédié). |

### 🔄 La Réplication de Mémoire (Une seule entité LEO)

Pour garantir que ces trois profils agissent comme un seul assistant unifié (LEO) pour Christophe, un mécanisme de synchronisation automatique de la mémoire est actif :

*   **Le Script** : `/opt/data/scripts/sync-memory.py`
*   **Fréquence** : Toutes les **30 minutes** (géré par le cron `sync-memory` sur le profil `default`).
*   **Fonctionnement** : Le script compare les dates de modification du fichier `MEMORY.md` de chaque profil (`~/.hermes/profiles/<nom>/memories/MEMORY.md`). La version la plus récente est immédiatement copiée et propagée vers les deux autres profils.
*   **Bénéfice** : Tout ce que LEO Copilote apprend lors d'une session de debug technique est instantanément accessible à LEO Hermes lors d'un chat général sur ton téléphone, créant un assistant doté d'un cerveau unifié.

---

### Commandes profils utiles

```bash
# Lister les profils actifs et leur statut de passerelle (gateway)
/opt/hermes/bin/hermes profile list

# Voir les détails de configuration d'un profil précis
/opt/hermes/bin/hermes profile show leo-copilot

# Lancer un chat local interactif sur un profil spécifique
/opt/hermes/bin/hermes -p leo-copilot chat
```

## Gateways (Passerelles de communication)

Un **gateway** est le canal par lequel vous communiquez avec votre assistant (Telegram, Discord, Slack, etc.).

Dans l'écosystème LEO, **chaque profil dispose d'un gateway Telegram dédié** et configuré avec son propre token de bot dans `config.yaml` :

```yaml
# Exemple dans config.yaml du profil leo-copilot
gateways:
  telegram:
    bot_token: "******"
    allowed_users:
      - "Tofdan"
```

Les trois gateways tournent de manière autonome sur le serveur via le superviseur **s6-supervisor** pour assurer un fonctionnement ininterrompu 24h/24.

---

## Skills

Les **skills** sont des procédures que l'assistant charge automatiquement pour savoir comment effectuer des tâches spécifiques. C'est la mémoire procédurale de votre assistant.

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

### Skills essentiels de l'écosystème LEO

| Skill | Description |
| :--- | :--- |
| `bavi-leo-governance` | Méthodologie d'audit multi-bureaux, standard 7 phases, interopérabilité, facturation. |
| `leo-architecture` | Topologie des profils, hiérarchie des LLM, règles anti-régression et réflexe commit. |
| `budget-tracking` | Suivi économique et relevés financiers des comptes d'API. |
| `system-management` | Gestion centralisée des serveurs physiques via Tailscale et SSH. |
| `dashboard-kpi` | Spécifications des dashboards HTML générés automatiquement. |

## Pour aller plus loin

*   [Documentation officielle Hermes : Skills](https://hermes-agent.nousresearch.com/docs)
*   Voir `02-configuration/providers.md` pour la topologie des LLM
*   Voir `03-utilisation/architecture-leo.md` pour le fonctionnement complet des crons et dashboards

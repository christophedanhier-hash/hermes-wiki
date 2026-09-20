# Configuration des providers LLM

> **Page canonique de référence :** [`hermes/architecture.md`](../architecture.md). Mesures vérifiées le **20/09/2026**.

Hermes Agent permet d'orchestrer plusieurs fournisseurs de modèles de langage (LLM). Sur l'écosystème LEO, la configuration s'appuie sur une séparation par profil avec fournisseur principal et fallback de secours déclaré.

## Principe d'orchestration sur LEO

Depuis l'audit du 20/09/2026, la répartition opérationnelle est la suivante :

- **Azure Foundry (`gpt-5.6-luna`)** : provider principal pour la majorité des profils opérationnels (`default`, `michel`, `robert`, `emile`, `gerard`).
- **OpenRouter (`meta/muse-spark-1.3-contributor`)** : provider principal pour le profil `sylvia` (voyages et roadbooks).
- **Google Gemini** : fallback déclaré (notamment `custom:google/gemini-3.7-flash` sur le profil Michel).
- **Automatisations no_agent** : 70 des 72 jobs planifiés dans `profiles/michel/cron/jobs.json` s'exécutent sans appel LLM (coût nul).
- **Ollama local (`qwen2.5:7b`)** : environnement local disponible sur la machine, mais non utilisé comme fallback actif en production.

| Profil | Rôle | Provider principal | Modèle configuré | Fallback déclaré |
|---|---|---|---|---|
| `default` (LEO) | Dialogue quotidien et pilotage | Azure Foundry | `gpt-5.6-luna` | Google Gemini |
| `michel` | Infrastructure et crons | Azure Foundry | `gpt-5.6-luna` | `custom:google/gemini-3.7-flash` |
| `robert` | Conseil stratégique | Azure Foundry | `gpt-5.6-luna` | Google Gemini |
| `emile` | Pédagogie et formation | Azure Foundry | `gpt-5.6-luna` | Google Gemini |
| `gerard` | Dossiers T600/OCA | Azure Foundry | `gpt-5.6-luna` | Google Gemini |
| `sylvia` | Voyages camping-car | OpenRouter | `meta/muse-spark-1.3-contributor` | Selon configuration |

---

## 1. Azure Foundry (Provider principal)

Azure Foundry héberge le modèle de référence `gpt-5.6-luna` pour cinq profils opérationnels.

### Configuration dans `config.yaml`

```yaml
model:
  default: gpt-5.6-luna
  provider: azure
```

### Variables d'environnement (`.env`)

Les clés et endpoints sont stockés exclusivement dans le fichier `.env` du profil (`~/.hermes/profiles/<nom>/.env`) et ne doivent jamais être commités :

```bash
AZURE_OPENAI_API_KEY=sk-...
AZURE_OPENAI_ENDPOINT=https://<votre-ressource>.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

---

## 2. Google Gemini (Fallback déclaré)

Google Gemini assure le rôle de secours automatique en cas d'indisponibilité du provider principal. Pour le profil `michel`, le fallback est explicitement configuré sur `custom:google/gemini-3.7-flash`.

### Configuration du fallback

```yaml
fallback_providers:
  - provider: google
    model: custom:google/gemini-3.7-flash
```

Dans le fichier `.env` du profil :

```bash
GEMINI_API_KEY=AIza...
```

---

## 3. OpenRouter (Profil Sylvia)

Le profil dédié aux voyages (`sylvia`) s'appuie sur OpenRouter pour accéder au modèle `meta/muse-spark-1.3-contributor`.

### Configuration

```yaml
model:
  default: meta/muse-spark-1.3-contributor
  provider: openrouter
```

Dans le `.env` de Sylvia :

```bash
OPENROUTER_API_KEY=sk-or-v1-...
```

---

## 4. Ollama (Environnement local)

Ollama permet d'exécuter des modèles locaux directement sur la machine (par exemple `qwen2.5:7b` sur GPU RTX 3050 8GB).

> **Important :** Sur l'installation LEO au 20/09/2026, Ollama est un runtime local d'appoint et **n'est pas le fallback de secours actif en production**.

### Configuration type (expérimentale ou locale)

```yaml
model:
  default: qwen2.5:7b
  provider: ollama
  base_url: "http://localhost:11434/v1"
```

Vérification du service local :

```bash
curl http://localhost:11434/api/tags
```

---

## 5. Synthèse du routage et maîtrise des coûts

Sur LEO, la politique de routage garantit à la fois performance et sobriété :

| Usage | Profil | Provider / Modèle | Modalité |
|---|---|---|---|
| Pilotage général | `default` | Azure Foundry / `gpt-5.6-luna` | Pay-as-you-go |
| Administration & code | `michel` | Azure Foundry / `gpt-5.6-luna` | Pay-as-you-go |
| Conseil stratégique | `robert` | Azure Foundry / `gpt-5.6-luna` | Pay-as-you-go |
| Pédagogie & mémoire | `emile` | Azure Foundry / `gpt-5.6-luna` | Pay-as-you-go |
| Dossiers T600/OCA | `gerard` | Azure Foundry / `gpt-5.6-luna` | Pay-as-you-go |
| Roadbooks voyages | `sylvia` | OpenRouter / `meta/muse-spark-1.3-contributor` | Pay-as-you-go |
| Secours si panne primaire | Profils Azure | Google Gemini (`gemini-3.7-flash`) | Quota / API |
| 70 crons d'automatisation | `michel` | Aucun LLM (`no_agent`) | **0$** |

---

## Contexte historique (daté)

> 📜 **Historique (juillet 2026) :** Lors de la phase initiale de reconstruction post-crash en juillet 2026, DeepSeek (`deepseek-v4-flash` et `deepseek-v4-pro`) était configuré comme provider principal direct avant d'être remplacé par Azure Foundry (`gpt-5.6-luna`). De même, les versions initiales mentionnaient `gemini-3.5-flash` avant la bascule vers la série Gemini 3.7. Ces mentions dans les archives et journaux datés reflètent l'état de leur époque.

---

## Pour aller plus loin

- Consulter [`architecture.md`](../architecture.md) pour l'état canonique de l'infrastructure
- Consulter [`profiles.md`](profiles.md) pour l'isolation des profils et des mémoires
- Consulter [`dashboards.md`](../utilisation/dashboards.md) pour le suivi des métriques et des services
- [Documentation officielle Hermes : Providers](https://hermes-agent.nousresearch.com/docs)

---

> 🤖 Dernière mesure vérifiée : **20/09/2026** — LEO et Michel. Source de vérité : `~/.hermes/profiles/*/config.yaml` et `architecture.md`.

# Configuration des providers LLM

> **Page canonique de référence :** [`hermes/architecture.md`](../architecture.md). Mesures vérifiées le **20/09/2026**.

Hermes Agent permet d'orchestrer plusieurs fournisseurs de modèles de langage (LLM). Sur l'écosystème LEO, la configuration s'appuie sur une séparation par profil avec fournisseur principal et fallback de secours déclaré.

## Principe d'orchestration sur LEO

Depuis le relevé du 24/10/2026, la répartition opérationnelle est la suivante :

- **Azure Foundry (`azure-foundry-claude`)** : provider principal pour cinq profils opérationnels (`michel`, `sylvia`, `robert`, `emile`, `gerard`).
- **deepseek-direct** : provider principal pour le profil `default` (LEO). OpenRouter n'est le fournisseur principal d'AUCUN profil (catalogue non utilisé).
- **Google Gemini (Gemini 3.8 Flash)** et **deepseek-flash** : replis de secours déclarés.
- **Automatisations no_agent** : 115 crons déclarés, dont 105 actifs (michel 96 · LEO 7 · sylvia 1 · robert 1) — relevé du 24/10/2026, s'exécutant en quasi-totalité sans appel LLM (coût nul).
- **Ollama local (`qwen2.5:7b`)** : environnement local disponible sur la machine, mais non utilisé comme fallback actif en production.

| Profil | Rôle | Provider principal | Modèle configuré | Fallback déclaré |
|---|---|---|---|---|
| `default` (LEO) | Dialogue quotidien et pilotage | deepseek-direct | `deepseek-flash` | Gemini 3.8 Flash |
| `michel` | Infrastructure et crons | azure-foundry-claude | Claude / Azure Foundry | deepseek-flash, Gemini 3.8 Flash |
| `robert` | Conseil stratégique | azure-foundry-claude | Claude / Azure Foundry | deepseek-flash, Gemini 3.8 Flash |
| `emile` | Assistant professionnel Émilie (Workbench) | azure-foundry-claude | Claude / Azure Foundry | deepseek-flash, Gemini 3.8 Flash |
| `gerard` | Astronomie, astrophotographie & documentation | azure-foundry-claude | Claude / Azure Foundry | deepseek-flash, Gemini 3.8 Flash |
| `sylvia` | Voyages camping-car | azure-foundry-claude | Claude / Azure Foundry | deepseek-flash, Gemini 3.8 Flash |

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

## 3. OpenRouter (Catalogue non utilisé)

OpenRouter n'est le fournisseur principal d'**AUCUN** profil (le profil `sylvia` utilise `azure-foundry-claude`). OpenRouter n'existe que comme entrée de catalogue, non utilisée — relevé du 24/10/2026. Le point laissé ouvert depuis le 22/09 est **tranché**.

### Référence catalogue (non utilisée)

```yaml
# Entrée de catalogue, non utilisée en production
model:
  default: meta/muse-spark-1.3-contributor
  provider: openrouter
```

Dans le `.env` (non actif) :

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
| Pilotage général | `default` | deepseek-direct / `deepseek-flash` | Pay-as-you-go |
| Administration & code | `michel` | azure-foundry-claude | Pay-as-you-go |
| Conseil stratégique | `robert` | azure-foundry-claude | Pay-as-you-go |
| Assistant pro Émilie (Workbench) | `emile` | azure-foundry-claude | Pay-as-you-go |
| Astronomie, astrophotographie & docs | `gerard` | azure-foundry-claude | Pay-as-you-go |
| Roadbooks voyages | `sylvia` | azure-foundry-claude | Pay-as-you-go |
| Secours si panne primaire | Profils Azure & default | deepseek-flash, Google Gemini (`gemini-3.8-flash`) | Quota / API |
| Crons d'automatisation | `michel` (96 actifs) | 115 crons déclarés, dont 105 actifs (michel 96 · LEO 7 · sylvia 1 · robert 1) — relevé du 24/10/2026, quasi-totalité en `no_agent` | **0$** |

---

## Contexte historique (daté)

> 📜 **Historique (juillet 2026) :** Lors de la phase initiale de reconstruction post-crash en juillet 2026, DeepSeek (`deepseek-v4-flash` et `deepseek-v4-pro`) était configuré comme provider principal direct avant d'être remplacé par Azure Foundry (`gpt-5.6-luna`). De même, les versions initiales mentionnaient `gemini-3.5-flash` avant la bascule vers la série Gemini 3.7. Le profil `emile` a initialement été déployé pour la formation et le mémoire universitaire d'Émilie avant d'évoluer vers le workbench métier My Émile IA. Le profil `gerard` a d'abord été documenté sur les seuls dossiers T600/OCA avant l'intégration globale de l'astronomie, l'astrophotographie et du site tofdan. Ces mentions dans les archives et journaux datés reflètent l'état de leur époque.

---

## Pour aller plus loin

- Consulter [`architecture.md`](../architecture.md) pour l'état canonique de l'infrastructure
- Consulter [`profiles.md`](profiles.md) pour l'isolation des profils et des mémoires
- Consulter [`dashboards.md`](../utilisation/dashboards.md) pour le suivi des métriques et des services
- [Documentation officielle Hermes : Providers](https://hermes-agent.nousresearch.com/docs)

---

> 🤖 Dernière mesure vérifiée : **24/10/2026** — LEO et Michel. Source de vérité : `~/.hermes/profiles/*/config.yaml` et `architecture.md`.

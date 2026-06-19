# Configuration des providers LLM

Hermes Agent peut utiliser plusieurs fournisseurs de modèles de langage (LLM). Voici comment configurer les plus courants.

## Principe

```mermaid
flowchart LR
    Profil[\"Un seul profil\"] --> Principal[\"Provider principal<br/>Conversations,<br/>tâches complexes\"]
    Profil --> Local[\"Provider local<br/>Tâches simples,<br/>gratuit, privé\"]
    Profil --> Fallback[\"Provider fallback<br/>Sécurité si le<br/>principal plante\"]

    style Profil fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style Principal fill:#e8f5f9,stroke:#0288d1,stroke-width:2px
    style Local fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style Fallback fill:#fff3e0,stroke:#e65100,stroke-width:2px
    linkStyle default stroke-width:2px,fill:none
```

## DeepSeek (recommandé pour le provider principal)

DeepSeek offre un excellent rapport qualité/prix avec son API.

### 1. Créer un compte

1. Allez sur [platform.deepseek.com](https://platform.deepseek.com)
2. Créez un compte
3. Rechargez du crédit (quelques dollars suffisent pour commencer)
4. Générez une clé API dans la section API Keys

### 2. Configurer

```bash
# Dans votre config.yaml
hermes config set model.default deepseek-chat
hermes config set model.provider deepseek
hermes config set DEEPSEEK_API_KEY "sk-votre-cle-ique"
```

Ou éditez `config.yaml` manuellement :

```yaml
model:
  default: deepseek-chat
  provider: deepseek
providers:
  deepseek:
    api_key: "sk-votre-cle-ique"
```

### 3. Vérifier

```bash
hermes run -m "Quel est mon solde DeepSeek ?"
```

## Ollama (provider local, gratuit)

Ollama exécute des LLM sur votre machine. Gratuit, privé, sans consommation de tokens.

### 1. Installer Ollama

```bash
# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows → Téléchargez depuis ollama.com/download
```

### 2. Télécharger un modèle

```bash
# Modèle recommandé pour l'assistant
ollama pull qwen2.5:7b

# Autres modèles
ollama pull llama3.1:8b    # Meta Llama 3.1
ollama pull mistral:7b     # Mistral
```

### 3. Configurer Hermes

```yaml
# Dans config.yaml
providers:
  custom:
    ollama:
      base_url: "http://localhost:11434/v1"
      api_key: "ollama"  # Valeur arbitraire, non utilisée
```

### 4. Vérifier

```bash
curl http://localhost:11434/api/tags
```

## Google Gemini (fallback)

Gemini peut servir de provider de secours si le principal est indisponible.

### 1. Obtenir une clé

1. Allez sur [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Créez une clé API (gratuite avec quota limité)

### 2. Configurer

```yaml
# Dans config.yaml — comme fallback
fallback_providers:
  - provider: google
    model: gemini-2.0-flash-001
```

Stockez la clé dans `.env` :

```bash
echo "GEMINI_API_KEY=AIza..." >> .env
```

## Grâce à un assistant déjà configuré

Si vous configurez votre assistant comme **LEO**, l'arbitrage entre providers est automatique :

| Tâche | Provider utilisé | Coût |
|-------|-----------------|------|
| Conversation normale | DeepSeek 🤖 | Payant (faible) |
| Traitement batch, analyse simple | Ollama 🏠 | Gratuit |
| Secours si plantage | Gemini ⚡ | Gratuit (quota) |
| Scripts planifiés | Aucun LLM (no_agent) | 0 |

## Configuration avancée

### Variables d'environnement (recommandé pour les clés)

Créez un fichier `.env` à côté de `config.yaml` :

```bash
DEEPSEEK_API_KEY="sk-..."
GEMINI_API_KEY="AIza..."
OPENAI_API_KEY="sk-..."  # Si vous utilisez OpenAI
```

### Plusieurs providers dans un seul profil

```yaml
model:
  default: deepseek-chat
  provider: deepseek
providers:
  custom:
    ollama:
      base_url: "http://localhost:11434/v1"
      api_key: "ollama"
fallback_providers:
  - provider: google
    model: gemini-2.0-flash-001
```

Ce n'est pas grave si votre fichier `config.yaml` est plus ou moins complexe. L'important est qu'il fonctionne pour **vous**.

## Pour aller plus loin

- Voir la [documentation des providers Hermes](https://hermes-agent.nousresearch.com/docs)
- Voir `02-configuration/profiles.md` pour les profils et gateways

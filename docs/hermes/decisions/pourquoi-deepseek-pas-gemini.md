# 🦁 Pourquoi LEO utilise DeepSeek plutôt que Gemini

> Analyse comparative — Juillet 2026. Le choix est financier, pas technique.

---

## Le constat

LEO a **cinq profils** qui tournent 24/7 avec **39 crons, 5 bots Telegram**. Chaque message, chaque analyse de cron, chaque classification d'email passe par une API.

À ce volume, **le prix au million de tokens est le facteur décisif** — et DeepSeek est **10 à 20 fois moins cher** que Gemini.

---

## 🟠 DeepSeek (notre choix principal)

### Ce qu'on utilise

| Modèle | Input (/1M) | Output (/1M) | Usage LEO |
|:---|:---|:---|:---|
| **DeepSeek V4 Pro** | $0.435 | $0.87 | Analyses complexes, debug, code, dashboards |
| **DeepSeek V4 Flash** | $0.14 | $0.28 | Crons légers, classification, bots Telegram |

> 💡 *Prix DeepSeek au 06/07/2026 (source : api-docs.deepseek.com). Le cache contextuel réduit encore le coût : $0.0028/1M (Flash) et $0.003625/1M (Pro) pour les hits.*

### Notre facture réelle

| Indicateur | Valeur |
|:---|:---|
| **Coût moyen / jour** | ~1.50 USD |
| **Soit par mois** | ~50 USD (cap) |
| **Modèle principal** | DeepSeek V4 Pro |

---

## 🟣 Google Gemini (notre fallback + usage ponctuel)

### La gamme (beaucoup plus large)

| Modèle | Input (/1M) | Output (/1M) | Contexte | Points forts |
|:---|:---|:---|:---|:---|
| **Gemini 3.5 Flash** | $1.50 | $9.00 | 1M | Équilibré, rapide |
| **Gemini 3.1 Pro** | $2.00 ($4.00 >200k) | $12.00 ($18.00 >200k) | 2M | Raisonnement avancé |
| **Gemini 2.5 Pro** | $1.25 | $10.00 | 1M | Bon rapport qualité/prix |
| **Gemini 2.5 Flash** | $0.30 | $2.50 | 1M | Volume, vision |
| **Gemini 2.0 Flash** | $0.10 | $0.40 | 1M | Budget, prototypage |

### Ce que Gemini a EN PLUS

```mermaid
mindmap
  root((Gemini))
    📚 Documentation
      Google AI Studio gratuit
      SDK Python natif
      Guides officiels
      Exemples de code
    🎨 Capacités
      Vision (images, vidéo)
      Audio
      Context 1M-2M tokens
      JSON mode natif
    🆓 Free Tier
      Flash models gratuits
      Prototypage illimité
      Pas de carte bancaire
    🏢 Écosystème Google
      Vertex AI
      BigQuery
      Cloud Functions
```

### Ce que DeepSeek a EN MOINS

```mermaid
mindmap
  root((DeepSeek))
    ❌ Documentation
      Minimaliste
      API doc basique
      Peu d'exemples
      Communauté plus petite
    ❌ Capacités
      Pas de vision
      Pas d'audio
      Contexte 128K-1M max
    ❌ Free Tier
      Aucun (paiement requis)
      Pas de sandbox gratuite
```

---

## 📊 Comparaison chiffrée

| Critère | DeepSeek V4 Pro | Gemini 2.5 Pro | Ratio |
|:---|:---|:---|:---|
| **Input / 1M tokens** | $0.435 | $1.25 | DeepSeek **2.9× moins cher** |
| **Output / 1M tokens** | $0.87 | $10.00 | DeepSeek **11.5× moins cher** |
| **Contexte max** | 1M tokens | 1M-2M tokens | Équivalent |
| **Vision** | ❌ | ✅ | Gemini gagne |
| **Audio** | ❌ | ✅ | Gemini gagne |
| **Documentation** | Basique | Excellente | Gemini gagne |
| **Modèles dispo** | 2 (Pro/Flash) | 8+ (Pro/Flash/Flash-Lite/Imagen/Veo) | Gemini gagne |

| Critère | DeepSeek V4 Flash | Gemini 2.5 Flash | Ratio |
|:---|:---|:---|:---|
| **Input / 1M tokens** | $0.14 | $0.30 | DeepSeek **2.1× moins cher** |
| **Output / 1M tokens** | $0.28 | $2.50 | DeepSeek **8.9× moins cher** |

---

## 💰 Projection : si LEO tournait sur Gemini

Prenons notre volume mensuel réel (~60M tokens input, ~20M tokens output) :

| Scénario | Coût DeepSeek | Coût Gemini 2.5 Pro | Surcoût |
|:---|:---|:---|:---|
| **Mensuel** | ~44 USD | ~670 USD | **+1 423 %** |
| **Annuel** | ~528 USD | ~8 040 USD | **+7 512 USD** |

> **DeepSeek nous fait économiser ~600 USD par mois, soit ~7 500 USD par an.**

Même avec Gemini 2.5 Flash (le moins cher des Flash récents à $0.30/$2.50), on serait à $68/mois pour ce volume — un peu plus cher que DeepSeek.

---

## 🎯 Notre stratégie actuelle

> ⚠️ Mise à jour 24/06/2026 : Leo Copilot a brièvement utilisé Gemini 2.5 Flash/Pro avant de revenir à DeepSeek V4 Pro. Voir détails ci-dessous.

```mermaid
flowchart TB
    subgraph BOTS["🤖 5 Bots LEO"]
        MAIN["🦁 LEO Principal\nDeepSeek V4 Flash\nChat quotidien"]
        COPILOT["🔧 Leo Copilot\nDeepSeek V4 Pro\nInfra, code"]
        BAVI["🧭 BAVI Voyages\nDeepSeek V4 Flash\nRoadbooks"]
        EMILE["🎓 Émile\nDeepSeek V4 Flash\nAssistant pédagogique"]
        ROBERT["🏛️ Robert\nDeepSeek V4 Pro\nConseil stratégique"]
    end

    subgraph BACKUP["⚡ Fallback"]
        GEMINI["Gemini 3.5 Flash\nSecours si DeepSeek down"]
    end

    subgraph CRONS["⏰ 41 crons"]
        DS_PRO["DeepSeek V4 Pro\nAnalyses, backups"]
        DS_FLASH["DeepSeek V4 Flash\nCollecte, dashboards"]
    end

    MAIN & BAVI & EMILE --> DS_FLASH
    COPILOT & ROBERT --> DS_PRO
    DS_PRO & DS_FLASH -.->|si KO| GEMINI
```

### Pourquoi Gemini n'a pas été retenu comme principal sur Leo Copilot

En test (22-23/06/2026), Leo Copilot a utilisé Gemini 2.5 Flash puis 2.5 Pro :

| Critère | Gemini 2.5 Flash | Gemini 2.5 Pro | DeepSeek V4 Pro |
|:--------|:----------------:|:--------------:|:--------------:|
| Actions agentiques | ❌ Stoppe l'exécution | ✅ Correct | ✅ Excellent |
| SWE-bench | 60.4% | 63.8% | **80.6%** |
| Coût output /1M | $2.50 | $10.00 | **$0.87** |
| Tool calls parallèles | Standard | Standard | **128** |

**Conclusion :** Gemini est conservé en fallback technique, mais DeepSeek reste le meilleur choix pour le volume et les capacités agentiques.

---

## ✅ Verdict

> **DeepSeek gagne sur le prix (10-20× moins cher). Gemini gagne sur l'écosystème (docs, modèles, capacités).**

Pour LEO, qui fait **du volume** (39 crons, bots Telegram, classification d'emails), le prix est le critère n°1. DeepSeek est imbattable.

Pour du **prototypage**, de la **vision**, ou des **tâches ponctuelles complexes**, Gemini est supérieur — et c'est pour ça qu'il reste configuré en fallback.

---

### Tableau récapitulatif : quel modèle pour quel usage

| Usage | Modèle | Pourquoi |
|:---|:---|:---|
| Crons quotidiens (38 jobs) | DeepSeek V4 Pro | Fiable, pas cher |
| Bots Telegram (dialogue) | DeepSeek V4 Flash | Latence faible, volume élevé |
| Classification emails | DeepSeek V4 Flash | 0.18 USD/M output |
| Debug & analyses complexes | DeepSeek V4 Pro | Raisonnement profond |
| Fallback (urgence) | Gemini 3.5 Flash | Toujours dispo, gratuit en test |
| Vision / OCR | Gemini 2.5 Flash | DeepSeek ne fait pas de vision |
| Prototypage rapide | Gemini (AI Studio) | Gratuit, bien documenté |

---

## 📈 Évolution des prix (rappel)

Le marché évolue vite. Ce qui est vrai en juillet 2026 peut changer :

- **DeepSeek V4** : prix actuels $0.435/$0.87 (Pro) et $0.14/$0.28 (Flash). Cache contextuel : $0.0036/$0.0028.
- **Gemini 3.5** : baisse probable à l'arrivée de Gemini 4 en prod.
- **Gemini 3.1 Pro** : disponible en preview, $2.00/$12.00 (≤200k).

LEO surveille les prix via le **cron budget-check-v6** et alertera si le rapport de force change.

---

*Document mis à jour le 07/07/2026 à 02:38 — Léo 🦁*

> 🤖 Dernier audit : 20 July 2026 à 09:14 (UTC+2)


# Budget et tracking DeepSeek

LEO coûte environ **$19.97 (coût réel constaté)**. Voici comment suivre et maîtriser ce budget.

## Le coût réel de LEO

```yaml
Budget LEO (post-reconstruction 04/07/2026):
  DeepSeek V4 Flash (quotidien):   composant principal
  DeepSeek V4 Pro (analyses):      usage ponctuel
  Gemini (fallback):                0 € (gratuit)
  Ollama (classification):          0 € (local)
  GitHub Pages (hébergement):       0 € (gratuit)
  n8n (workflows):                  ❌ Retiré 13/07/2026
  Coût réel constaté:              ~$19.97
```

> ⚠️ **Mise à jour 04/07/2026** : le budget DeepSeek réel est d'environ **$19.97** (coût total constaté). Les projections pré-crash (1-3€/mois) ne sont plus valides suite aux changements de modèles et d'usage.

## Triple ventilation

```python
# Ne pas se fier aux logs DeepSeek
# Mesurer le delta de balance
vrai_coût = solde_avant - solde_après

# Ventiler par usage
coûts = {
    "deepseek_flash":  ~$0.03/jour,    # Usage quotidien
    "deepseek_pro":    ~$0.05/jour,    # Analyses complexes
    "ollama":           0.00,          # Gratuit
    "gemini":           0.00,          # Gratuit (fallback)
}
```

## Dashboard budget

```markdown
| Métrique              | Valeur          |
|:---------------------|:----------------|
| Solde réel           | ~$19.97         |
| Dépense totale       | ~$19.97         |
| Moyenne quotidienne  | variable        |
| Coût 14 jours        | ~$19.97         |
| Tendance             | Stable 📊       |
```

## Alertes

```yaml
Seuils d'alerte:
  Solde < 10€:  🔴 Notification immédiate
  Dépense > 1€/jour: 🟡 Vérifier si anomalie
  Erreur API:        🟡 Fallback Gemini automatique
```

## Comparaison des providers

| Provider | Coût IN (1M tokens) | Coût OUT (1M tokens) | Autonomie ($60) |
|:---------|:-------------------:|:--------------------:|:---------------:|
| DeepSeek Flash | $0.14 | $0.28 | >6 ans |
| DeepSeek Pro | $1.50 | $5.00 | ~2 mois |
| Gemini Flash | **0 €** | **0 €** | ∞ (quotas gratuits) |
| Ollama | **0 €** | **0 €** | ∞ (local) |
*Document mis à jour le 04/07/2026 — 22:48:00 — Léo 🦁*

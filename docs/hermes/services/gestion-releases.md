# 📦 Gestion des Releases Hermes — Stratégie LEO

> Mise à jour sans impact. Continuité garantie.

---

## 🔄 Pipeline complet

```
Détection (cron hebdo) → Évaluation (Ollama) → Backup → Déploiement → Vérification → Suivi
```

---

## 1. Détection — Cron hebdomadaire

Tous les lundis 9h, compare `hermes --version` avec l'API GitHub :

```
hermes --version → v0.16.0
GitHub API → v0.17.0 (différent ?) → 🚨 Alerte Telegram
```

## 2. Évaluation — Ollama qwen (0 €)

Analyse du changelog GitHub pour extraire :
- **Breaking changes** ⚠️
- **Nouvelles features** ✨
- **Bugs fixés** 🐛
- **Impact sur nos profils** (leo-copilot, default, bavi-leo)

## 3. Backup — Obligatoire avant déploiement

```bash
# Export profil complet
hermes -p leo-copilot profile export > /opt/data/backups/hermes-leo-copilot-$(date +%Y%m%d).tar.gz

# Git snapshot
cd /opt/data/hermes-wiki && git push
cd /opt/data/leo-tracker && git push
```

## 4. Déploiement — Fenêtre de maintenance

- **Quand** : nuit (2h-4h) ou demande explicite
- **Action** : `uv pip install --upgrade hermes-agent`
- **Redémarrage** : gateways default + leo-copilot + bavi-leo + emile + bureau-robert

## 5. Vérification — Checklist post-déploiement

| Point | Check |
|:---|:---|
| 5 gateways UP | `hermes gateway status` |
| Crons OK | Dashboard global |
| Dashboards OK | Vérification HTTP |
| n8n workflows | ❌ Retiré (13/07/2026) |

## 6. Rollback — Si échec

```bash
uv pip install hermes-agent==VERSION_PRÉCÉDENTE
# Restaurer backup si nécessaire
```

## 7. Suivi — Documentation

- Version déployée → `hermes-wiki/docs/hermes/releases.md`
- Changelog résumé → Ollama → archivé
- Prochain check → cron J+7

---

*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

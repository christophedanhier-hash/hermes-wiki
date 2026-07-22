# Watchdogs et alertes

Les watchdogs sont des scripts qui surveillent en continu l'état des services et alertent en cas de problème. C'est le système immunitaire de LEO.

## Principe

Un watchdog = un script qui tourne régulièrement et vérifie qu'un service répond.

```bash
# Watchdog typique
#!/bin/bash
# Vérifie que n8n répond (exemple historique — n8n retiré 13/07/2026)
# Remplacé par des healthchecks Hermes directs
if ! curl -s http://localhost:5678/healthz > /dev/null; then
    echo "❌ n8n ne répond pas"
    # Tentative de redémarrage (historique)
    docker restart n8n
    # Notification
    hermes memory add "n8n relancé le $(date)" --target memory
fi
```

> ⚠️ **Note 17/07/2026** : n8n a été retiré le 13/07/2026. Cet exemple est conservé pour montrer le pattern de watchdog. Les watchdogs actuels surveillent Hermes, Ollama, Docker et les dashboards.
```

## Les watchdogs de LEO

```yaml
Utiliser une liste à puces propre ou un tableau Markdown valide.

Toutes les 6 heures:
  - 🔭 Drive Watch             → détecte les changements dans Google Drive

Tous les jours:
  - 🤖 Hermes Update Check     → nouvelle version disponible ?
  - 💰 Budget Check            → solde suffisant ?
```

## Auto-heal : le watchdog principal

> 🚫 **Auto-Heal supprimé le 04/07/2026** — remplacé par le déploiement horaire unifié via `collect-v2.py` et leo-copilot.

```yaml
À clarifier selon l'architecture réelle du dashboard.
  ✅ Ollama:       qwen2.5:7b responsive ?
  ✅ Docker:       2/2 conteneurs UP (n8n retiré 13/07) ?
  ✅ Disque:       < 80% utilisé ?
  ✅ Token LEO:    Google API OK ?
  Supprimer ou préciser le contexte

En cas d'échec:
  1. Tentative de correction automatique
  2. Si réussi → log + continue
  3. Si échec → issue GitHub (label auto-heal)
```

## Dashboard Watch

Le Dashboard Watch vérifie que le dashboard unifié est en ligne et à jour :

```bash
for dashboard in leo-kpi machines crons github bavi-leo global; do
    code=$(curl -s -o /dev/null -w "%{http_code}" \
        "http://localhost:8765/panel (ou autre URL locale valide)")
    if [ "$code" != "200" ]; then
        echo "❌ ${dashboard}: HTTP ${code}"
        # Redéploiement automatique
        python3 ~/.hermes/profiles/leo-copilot/scripts/deploy-dashboard.py
    else
        echo "✅ ${dashboard}: HTTP 200"
    fi
done
```

## Notifications

```yaml
Canaux de notification:
  - Telegram DM      → alertes critiques (disque, budget, panne)
  - GitHub Issues    → problèmes non critiques (auto-heal, watchdogs)
  - Dashboard        → tous les statuts en temps réel
  
Règles:
  - Une alerte = une issue GitHub
  - Label "auto-heal" si corrigé automatiquement
  - Pas de spam : pas de notification pour les succès
```
*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

> 🤖 Dernier audit : 22 July 2026 à 09:00 (UTC+2)


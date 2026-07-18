# 🏛️ Architecture LEO — Dashboards & Crons

> Document vivant — mis à jour le **17/07/2026** (audit rédactionnel).

> ⚠️ **Changements 13-17/07/2026** : n8n retiré (13/07). 5 dashboards GitHub Pages actifs. La collecte utilise `collect-v2.py` (8 sources, n8n retiré). Déploiement toutes les heures (`10 * * * *`) via leo-copilot.

---

## 1. Vue d'ensemble

```mermaid
flowchart TB
    subgraph Sources["📡 Sources de données (8)"]
        DS["DeepSeek API<br/>budget"]
        GH_API["GitHub API<br/>github"]
        OS["OS serveur LEO<br/>infra"]
        SESS["Sessions DB<br/>sessions"]
        BAVI_M["BAVI metrics<br/>bavi"]
        CRONS_M["Crons Hermes<br/>crons"]
        SVCS["Services<br/>services"]
        VAULTS["Obsidian Vaults<br/>vaults"]
    end

    subgraph Collecte["⏱️ Collecte unifiée (H:10)"]
        COLLECT["collect-v2.py<br/>8 sources → JSON<br/>déploiement toutes les heures"]
    end

    subgraph Dashboard["📊 leo-dashboard (1 seul)"]
        DASH["leo-dashboard<br/>Chart.js · GitHub Pages<br/>https://christophedanhier-hash.github.io/leo-dashboard/"]
    end

    subgraph scripts["🐍 Scripts Python (ex-n8n)"]
        DRIVE_ISSUE["Drive → Issue<br/>Surveillance Drive"]
        GARDIEN["Gardien du Drive<br/>Protection documents"]
        SAVE_CONTACTS["Save Contacts<br/>Sauvegarde contacts"]
    end

    subgraph Vaults["📒 Vaults Obsidian (4)"]
        LEO_VAULT["leo"]
        DEFAULT_VAULT["default"]
        EMILE_VAULT["emile"]
        BAVI_VAULT["bavi"]
    end

    Sources --> COLLECT
    COLLECT --> DASH
    DASH -->|monitoring| scripts
    Vaults -->|monitoring dashboard| DASH
```

---

## 2. Dashboard unique

Depuis la reconstruction post-crash du 30/06/2026, **un seul dashboard** existe :

| Dashboard | URL | Contenu | Généré par | Fréquence |
|-----------|-----|---------|-----------|-----------|
| **🌍 leo-dashboard** | [leo-dashboard](https://christophedanhier-hash.github.io/leo-dashboard/) | Sessions, budget, machines, crons, GitHub, BAVI, services, vaults | `collect-v2.py` | H:10 (déploiement leo-copilot) |

**Collecteur unifié** : `collect-v2.py` agrège 9 sources de données :
1. Sessions — nombre de sessions et messages
2. Budget — solde DeepSeek (~$19.97)
3. Crons — statut des tâches planifiées
4. Infra — CPU/RAM/disque du serveur LEO
5. n8n — workflows et exécutions
6. GitHub — activité des repos
7. BAVI — métriques bureaux
8. Services — statut des services (Ollama, Docker, etc.)
9. Vaults — monitoring des 4 vaults Obsidian

---

## 3. Déploiement

Le déploiement du dashboard est assuré par un cron unique :

```
10 * * * *  →  collect-v2.py (via leo-copilot, no_agent)
```

Changement clé du 04/07/2026 :
- **Avant** : 7 crons séparés (un par dashboard) + Auto-Fix Daemon
- **Après** : 1 cron unique `collect-v2.py` (déploiement toutes les heures)

---

## 4. Les Workflows n8n (3) — ❌ RETIRÉS

> ⚠️ **n8n a été retiré le 13/07/2026.** Les 3 workflows ont été migrés vers des crons Hermes no_agent. Cette section est conservée pour référence historique.

n8n tournait sur `localhost:5678` (même machine que Hermes).

| Workflow | Rôle | Description | Statut |
|----------|------|-------------|--------|
| **Drive → Issue** | Surveillance Drive | Créait une issue GitHub quand un fichier Drive était modifié | → Cron `drive-to-issue` |
| **Gardien du Drive** | Protection documents | Surveillait l'intégrité des documents Google Docs | → Cron `gardien-drive` |
| **Save Contacts** | Sauvegarde contacts | Sauvegardait les contacts Google vers un fichier JSON | → Cron `save-contacts` |

---

## 5. Vaults Obsidian (4)

| Vault | Usage | Monitoring |
|-------|-------|------------|
| **leo** | Vault personnel LEO | ✅ Dashboard monitoring |
| **default** | Vault par défaut Hermes | ✅ Dashboard monitoring |
| **emile** | Vault pédagogie Émile | ✅ Dashboard monitoring |
| **bavi** | Vault bureaux BAVI | ✅ Dashboard monitoring |

Les 4 vaults sont surveillés via le dashboard unifié.

---

## 6. Budget

| Métrique | Valeur |
|----------|--------|
| Budget réel constaté | **~$19.97** |
| Seuil d'alerte | $30 |
| Seuil d'arrêt | $10 |

---

## 7. Statistiques clés

| Métrique | Valeur |
|----------|--------|
| Workflows n8n | **3** ✅ |
| Dashboards | **1** (unifié) |
| Sources de collecte | **9** |
| Vaults Obsidian | **4** |
| Budget DeepSeek | **~$19.97** |
| Déploiement | Toutes les heures via leo-copilot |

---

> **Document mis à jour le 04/07/2026** — reflet des changements post-crash.
*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

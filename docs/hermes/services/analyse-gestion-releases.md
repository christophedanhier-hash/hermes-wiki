# 🧠 Analyse : Gestion des Releases Hermes

> Comment garantir zéro casse lors des mises à jour d'un agent qui tourne 24/7 sur 3 profils, 30 crons, 5 workflows n8n.

---

## 1. Pourquoi c'est risqué

Hermes n'est pas un logiciel classique qu'on met à jour et on redémarre. C'est un **orchestrateur vivant** :

| Surface | Ce qui peut casser |
|:---|:---|
| **3 profils** (default, leo-copilot, bavi-leo) | Config YAML changée, variables renommées, nouvelles valeurs obligatoires |
| **30 crons** | Changement de signature des outils (`cronjob`, `terminal`…), breaking API |
| **5 workflows n8n** | Pas impactés directement (n8n est indépendant), mais si Hermes down → webhooks muets |
| **Skills custom** | ~20 skills créés/maintenus. Si le format SKILL.md change → plus chargés |
| **Mémoire** | Le format du `state.db` SQLite peut évoluer → corruption si rollback |
| **Gateways Telegram** | Si l'API gateway change → bots muets |

**Un `uv pip install --upgrade` naïf = risque de tout casser d'un coup.**

---

## 2. Les 8 étapes — Pourquoi chacune

### Étape 1 — DÉTECTION
**Pas juste `hermes --version`.**  
Un cron hebdomadaire interroge l'API GitHub Releases et compare avec la version installée. Pourquoi ?

- `hermes --version` dit "1 commit behind" — mais c'est le repo git local, pas la release stable
- Seule l'API GitHub donne la **release taguée** (v2026.6.19), pas le `main` instable
- Détection → alerte Telegram → **décision humaine**, pas mise à jour automatique

### Étape 2 — ÉVALUATION (Ollama qwen, 0 €)
Avant de toucher quoi que ce soit, Ollama lit le changelog GitHub et répond à :

1. Y a-t-il des **breaking changes** qui impactent nos profils ?
2. Les **skills** sont-ils compatibles ? (format SKILL.md, metadata)
3. La **config YAML** a-t-elle de nouveaux champs obligatoires ?
4. Les **outils** qu'on utilise (`cronjob`, `terminal`, `delegate_task`) ont-ils changé ?
5. Est-ce que ça vaut le coup ? (bugs fixés qui nous concernent ?)

**Exemple** : v0.17.0 a ajouté Photon iMessage — zéro impact pour nous. Mais a changé le curator — impact si on l'utilise.

### Étape 3 — BACKUP
```bash
hermes -p leo-copilot profile export → backup.tar.gz
```
Ce fichier contient **tout** : config.yaml, .env, skills, cron, state.db, memories.

**Pourquoi avant, pas après ?** Si la migration de DB casse (v0.16 → v0.17 change le schéma SQLite), le backup contient la version **pré-migration**. Un rollback simple ne suffira pas si la DB est corrompue — il faut restaurer.

### Étape 4 — STAGING (mises à jour majeures uniquement)
Pour v0.16 → v0.17 (~1475 commits), on **clone le profil leo-copilot en leo-staging** :

```bash
hermes profile create leo-staging --clone-from leo-copilot
```

On démarre la gateway staging, on fait un test rapide (un cron, un message Telegram), on vérifie que tout fonctionne. **Si staging casse → on ne touche pas la production.**

### Étape 5 — DÉPLOIEMENT
- **Fenêtre de nuit** (2h-4h) : les crons tournent moins, Christophe dort
- **Pause des crons** : `hermes cron pause` sur les critiques (budget, dashboard-watch)
- `uv pip install --upgrade hermes-agent` (dans le venv, pas de dépendances système)
- Redémarrage **un profil à la fois**, pas les 3 d'un coup

### Étape 6 — VÉRIFICATION
Checklist concrète, pas de "vérifier que tout va bien" :

| Test | Commande | Attendu |
|:---|:---|:---|
| Gateway UP | `curl localhost:18791/health` | 200 |
| Profil charge | `hermes -p leo-copilot chat -q "ping"` | Réponse |
| Cron run | `hermes cron run <id>` | Success |
| Dashboard | `curl dashboard-url` | 200 + contenu |
| n8n webhook | `curl webhook/leo-alert` | 200 |
| Skills load | `hermes skills list` | Liste complète |

### Étape 7 — ROLLBACK
Deux scénarios :

**Rollback simple** (si juste le binaire casse) :
```bash
uv pip install hermes-agent==0.16.0
```

**Rollback complet** (si la DB ou la config est corrompue) :
```bash
hermes profile import backup.tar.gz  # Écrase tout
```

### Étape 8 — SUIVI
- Version déployée → documentée dans `hermes-wiki`
- Changelog résumé → archivé pour référence
- Prochain check → cron J+7

---

## 3. Ce qu'on ne fait PAS

| ❌ À éviter | ✅ Pourquoi |
|:---|:---|
| Mise à jour automatique | Une release peut casser les crons → plus de budget tracking, plus de dashboards |
| Mise à jour en journée | Si ça casse, Christophe est impacté en direct |
| Skip du backup | Une DB corrompue par migration = perte de toutes les mémoires et sessions |
| Update des 3 profils en parallèle | Si un bug touche un profil, les 3 sont down |
| Faire confiance au changelog officiel | Il est écrit pour les humains. Ollama l'analyse pour **notre** usage spécifique |

---

## 4. Prochaine release : v0.17.0 (19 juin)

**Statut** : Disponible, pas encore évaluée.  
**Action requise** : Ollama analyse du changelog → rapport → décision.

---

*Analyse réalisée le 24/06/2026 — LEO 🦁*

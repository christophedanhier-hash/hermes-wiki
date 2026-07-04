# 🔐 Analyse pré-migration v0.16.0 → v0.17.0

> Audit complet de l'environnement LEO avant mise à jour. **Objectif : 150% de garantie.**

---

## 1. État actuel — 100% stable

| Composant | État | Détail |
|:---|:---|:---|
| **Version** | v0.16.0 (2026.6.5) | 1 commit behind upstream |
| **Gateway default** | 🟢 UP | PID 26649, uptime depuis 13 juin |
| **Gateway leo-copilot** | 🟢 UP | PID 489486, uptime depuis 23 juin |
| **Gateway bavi-leo** | 🟢 UP | PID 325210, uptime depuis 23 juin |
| **Crons leo-copilot** | 🟡 1/1 (erreur connue: Drive Watch — déjà corrigé) | |
| **Crons default** | 🟢 29/29 | |
| **Skills custom** | 🟢 1 skill agent (hermes-agent) | Aucun impact |
| **send_message tool** | ✅ Présent (78 KB) | Utilisé dans 2 skills bundle (non critiques) |
| **Tokens OAuth** | ✅ Google token valide | |
| **n8n** | 🟢 UP, 6 workflows | Indépendant de Hermes |
| **Dashboards** | 🟢 Tous OK | Indépendants |

---

## 2. Ce qui peut impacter notre setup

| Changement v0.17 | Impact LEO | Risque |
|:---|:---|:---|
| `send_message` toolset bug (#8616) | Déjà corrigé, le tool reste présent | **Aucun** |
| Telegram MarkdownV2 | Messages formatés → rendu amélioré | **Bénéfice** |
| Memory batch operations | Sync mémoire plus fiable | **Bénéfice** |
| `read_file` .docx/.xlsx | Utile pour Drive | **Bénéfice** |
| Background subagents | Nouveau, non utilisé | **Aucun** |
| iMessage/WhatsApp/Raft | Non utilisé | **Aucun** |
| Compaction trigger 85% | On utilise DeepSeek/Gemini, pas gpt-5.5 | **Aucun** |
| Refactoring cli.py/gateway | Si pas de patch custom → transparent | **Faible** |

---

## 3. Vérifications croisées

| Question | Réponse |
|:---|:---|
| `send_message` est-il dans nos skills custom ? | ❌ Non (seulement dans 2 skills bundle) |
| Nos crons utilisent-ils `delegate_task` avec timeout ? | ❌ Non |
| Avons-nous patché `cli.py` ou `gateway/run.py` ? | ❌ Non |
| Utilisons-nous le curator ? | ❌ Non |
| Les 3 gateways sont-elles joignables ? | ✅ Oui |

---

## 4. Plan de migration

```
1. BACKUP: tar czf /opt/data/backups/hermes-pre-v017-$(date +%Y%m%d).tar.gz \\
     /opt/data/profiles/ /opt/data/leo_google_token.json /opt/data/.env
     
2. PAUSE CRONS: hermes cron pause <critiques>

3. UPDATE: uv pip install --upgrade hermes-agent

4. RESTART GATEWAYS (un par un):
   default → vérifier → leo-copilot → vérifier → bavi-leo

5. VÉRIFIER: ping Telegram, 1 cron test, dashboard OK

6. ROLLBACK si échec:
   uv pip install hermes-agent==0.16.0
   tar xzf backup.tar.gz
```

---

## 5. Garanties

| Garantie | Moyen |
|:---|:---|
| **LEO revient** | Gateway redémarre, même config, même profil |
| **Crons reprennent** | Jobs.json intact, scheduler résilient |
| **Mémoire préservée** | state.db + MEMORY.md backupés |
| **Skills OK** | Format SKILL.md inchangé en v0.17 |
| **n8n intact** | Indépendant de Hermes |
| **Rollback < 2 min** | Backup + pip install version précédente |

---

*Document mis à jour le 04/07/2026 — 00:00:00 — Modèles DeepSeek unifiés 🦁*

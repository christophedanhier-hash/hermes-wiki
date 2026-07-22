# 📋 Journal d'Audit Rédactionnel — hermes-wiki

Dernier passage d'audit automatique : **22/07/2026**

## Résumé du passage

- **Total fichiers analysés** : 183 (63 hermes-wiki + 120 BAVI_LEO)
- **Méthode** : Statique (API DeepSeek indisponible — clé expirée sk-f90...5fc0)
- **Nouvelles anomalies détectées** : 0 (audit IA non réalisé)
- **Anomalies connues non résolues** : 17
- **Auto-fix appliqués** : 2 patches manuels sur bots-telegram.md
- **Statut global du wiki** : ⚠️ 17 anomalies non résolues

## Anomalies connues (issues précédentes non résolues)

| Page | Section | Gravité | Ce que dit la doc | Réalité | Action entreprise |
|------|---------|---------|-------------------|---------|-------------------|
| `docs/hermes/dashboards/ch22-dashboards-intro.md` | Pitfalls | 🟠 Manquant | Solution : ** | La phrase est tronquée, la solution n'est pas fournie. | Compléter la phrase avec la solution appropriée (par exemple, utiliser un canvas avec dimensions fixes ou désactiver le responsive). |
| `docs/hermes/services/n8n.md` | ⚡ Workflows Actifs (3) | 🟡 Obsolète | Présente 3 workflows comme actifs (Drive→Issue, Gardien du Drive, Save Contacts) avec leurs IDs et déclencheurs. | Tous les workflows n8n ont été supprimés le 13/07/2026 et migrés vers des crons Hermes no_agent. Ils ne sont plus actifs. | Remplacer la section par une mention historique ou supprimer les détails des workflows, car ils n'existent plus. |
| `docs/hermes/services/n8n.md` | 📊 Monitoring | 🟡 Obsolète | Le statut n8n est intégré au leo-dashboard (source n8n dans collect-v2.py) avec des métriques de santé, workflows, exécutions. | n8n étant retiré, ces métriques ne sont plus collectées. Le dashboard ne devrait plus référencer n8n comme source active. | Supprimer ou archiver la section Monitoring car n8n n'est plus surveillé. |
| `docs/hermes/services/n8n.md` | 🏗️ Architecture (diagramme Mermaid) | 🟡 Obsolète | Le diagramme montre n8n comme hub central de 3 workflows actifs (Drive→Issue, Gardien du Drive, Save Contacts). | n8n n'existe plus, les workflows sont des crons autonomes. Le diagramme suggère une architecture qui n'est plus en place. | Remplacer le diagramme par un texte indiquant que l'architecture est obsolète, ou le supprimer. |
| `docs/hermes/services/n8n.md` | 🛡️ Maintenance | 🟡 Obsolète | Fournit des commandes Docker pour vérifier le conteneur, logs, healthcheck, refresh credentials. | Le conteneur n8n n'existe plus, ces commandes sont inutiles pour le système actuel. | Supprimer la section Maintenance car les commandes ne s'appliquent plus à un service retiré. |
| `docs/hermes/services/n8n.md` | Accès (tableau) | 🟡 Obsolète | Fournit URL locale, Tailscale, email, password, version, mode Docker. | Le service n'existe plus, ces accès ne sont plus valides. Les informations sont historiques mais peuvent être gardées comme référence, cependant l'URL locale et Tailscale ne répondent plus. | Ajouter une mention claire que ces accès sont obsolètes et que le service n'est plus accessible. |
| `docs/hermes/utilisation/documentation-map.md` | configuration/providers.md | 🟡 Obsolète | DeepSeek V4 Flash/Pro, Gemini fallback, Ollama | deepseek, openai, gemini, grok, anthropic | Mettre à jour la liste des providers pour inclure openai, grok, anthropic |
| `docs/hermes/utilisation/documentation-map.md` | configuration/providers.md | 🟠 Manquant | Ollama (sans modèle spécifique) | Ollama avec modèle qwen2.5:7b | Ajouter le modèle local utilisé : qwen2.5:7b |
| `docs/hermes/utilisation/documentation-map.md` | configuration/profiles.md | 🟠 Manquant | mémoire (non spécifiée comme unifiée) | Mémoire unifiée entre default et leo-copilot | Préciser que la mémoire est unifiée entre les profils default et leo-copilot |
| `docs/hermes/utilisation/skills-catalogue.md` | BAVI LEO — 5 skills | 🔴 Erreur | BAVI LEO — 5 skills with 6 listed items (governance, robert, sophie, gerard, sylvie, assurance) | 5 profiles/bots: leo-copilot, default, bureau-robert, bavi-leo, emile | Update the number to 6 or correct the list to match reality. The doc lists 6 skills but should reflect the actual 5 profiles (leo-copilot, default, bureau-robert, bavi-leo, emile). Remove skills that do not exist (sophie, gerard, sylvie, assurance) and add missing ones. |
| `docs/hermes/utilisation/skills-catalogue.md` | 1. 🏗️ bavi-leo-governance | 🟡 Obsolète | Skill named 'bavi-leo-governance' v1.4 | Bot named 'bavi-leo' exists, but no separate governance skill; likely the same | Rename skill to 'bavi-leo' or confirm it's the same. Update version if needed. |
| `docs/hermes/utilisation/skills-catalogue.md` | 2. 🏛️ bureau-robert | 🟡 Obsolète | Bureau-robert with 7 sub-experts | Bot 'bureau-robert' exists, but sub-experts may differ; doc mentions sub-experts not confirmed in reality | Verify sub-expert list against actual configuration. Ensure no obsolete references. |
| `docs/hermes/utilisation/skills-catalogue.md` | 3. 💰 bureau-sophie | 🟠 Manquant | Bureau-sophie orchestreur pilotage économique | No such profile or bot exists in reality | Remove this skill entirely or replace with existing corresponding profile (e.g., emile or leo-copilot). |
| `docs/hermes/utilisation/skills-catalogue.md` | 4. 📝 bureau-gerard | 🟠 Manquant | Bureau-gerard documentation T600 | No such profile or bot | Remove this skill entirely. |
| `docs/hermes/utilisation/skills-catalogue.md` | 5. 🧭 bureau-sylvie | 🟠 Manquant | Bureau-sylvie organisation voyages | No such profile or bot | Remove this skill entirely. |
| `docs/hermes/utilisation/skills-catalogue.md` | 6. 🛡️ assurance-obligatoire | 🟠 Manquant | Expert métier transverse (inter-bureaux) | No separate assurance skill; likely integrated into bureau-robert or not present | Remove this skill or merge into bureau-robert if applicable. |
| `docs/hermes/utilisation/architecture-leo.md` | 3. Déploiement | 🔴 Erreur | 1 cron unique collect-v2.py (déploiement toutes les heures) | Il existe 39 crons actifs gérés par leo-copilot, dont un pour le déploiement du dashboard. Le texte laisse entendre qu'il n'y a qu'un seul cron. | Préciser que le cron de déploiement du dashboard fait partie d'un ensemble de 39 crons gérés par leo-copilot. |
| `docs/hermes/utilisation/architecture-leo.md` | 1. Vue d'ensemble | 🟠 Manquant | Le document ne mentionne pas les profils/bots Telegram ni les ports ou modèles d'IA. | Il existe 5 profils/bots Telegram (leo-copilot, default, bureau-robert, bavi-leo, emile), des ports spécifiques (22,53,80,443,631,3389,5901,7681,8123,8765,9119,11434,20241), et des modèles d'IA (qwen2.5:7b local, providers deepseek, openai, gemini, grok, anthropic). | Ajouter une section ou des informations dans le diagramme pour lister les profils/bots, les ports ouverts, les modèles IA, et la mémoire unifiée entre default et leo-copilot. |
| `docs/hermes/utilisation/architecture-leo.md` | 1. Vue d'ensemble (diagramme) | 🟡 Obsolète | Le diagramme montre un seul sous-graphe 'scripts' avec 3 scripts Python, et ne montre pas les 39 crons gérés par leo-copilot. | Il y a 39 crons gérés par leo-copilot, et le diagramme devrait refléter cette réalité (par exemple, un sous-graphe 'Crons' listant les crons clés). | Mettre à jour le diagramme pour inclure un sous-graphe 'Crons LEO' avec les 39 crons, ou au moins mentionner dans le texte que le cron de dashboard n'est qu'un parmi 39. |


> 🤖 Généré automatiquement par l'Auditeur de Wiki LEO le 20/07/2026 à 09:17 (UTC+2)

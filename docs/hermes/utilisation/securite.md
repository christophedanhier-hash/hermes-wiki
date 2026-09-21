# 🛡️ Sécurité — Publication et protection de la documentation

> **Dernière revue : 21/09/2026** — LEO. Cette page définit ce qui peut être publié dans le Wiki Hermes public et ce qui doit rester dans les espaces privés LEO.

## Règle d'or

Tout contenu publié sur GitHub Pages est public, indexable et copiable. Une page doit donc être relue comme si elle était consultée par une personne extérieure à la plateforme.

La sécurité documentaire repose sur trois niveaux :

1. **Public** : architecture générale, rôles des profils, principes de fonctionnement, procédures génériques et modèles/providers déjà rendus publics par le produit.
2. **Interne** : chemins absolus, détails de déploiement, états de services, rapports d'incident, compteurs opérationnels détaillés et procédures d'exploitation.
3. **Secret** : mots de passe, tokens, clés API, fichiers OAuth, secrets de session et données personnelles.

## 🔴 Ne jamais publier

| Donnée | Pourquoi | Traitement public |
|---|---|---|
| Mots de passe, tokens, clés API ou secrets de session | Accès direct à un service | `[REDACTED]` ou omission complète |
| Fichiers `.env`, JSON OAuth, recovery-kit ou vault credentials | Contiennent des secrets réutilisables | Ne jamais les joindre ni les copier |
| Tokens Telegram, GitHub, Google, Azure, OpenRouter ou SMTP | Détournement de comptes | Nommer le service sans la valeur |
| Identifiants personnels, GSM, adresse privée ou coordonnées privées | Vie privée, phishing, doxing | `[coordonnées privées]` |
| Données de clients, médicales, financières ou professionnelles confidentielles | Confidentialité et RGPD | Espace privé autorisé uniquement |
| Contenu de sessions, messages Hive ou mémoires de profils | Contexte et données personnelles | Résumé anonymisé si nécessaire |
| URLs d'authentification, liens signés ou paramètres contenant un secret | Contournement d'accès | Omettre l'URL ou la redacter |
| Chemins internes vers secrets ou bases sensibles | Facilite l'exfiltration | Décrire le composant sans le chemin |

## 🟡 Publier avec précautions

L'architecture générale peut être documentée publiquement lorsqu'elle aide à comprendre le produit :

| Élément | Règle |
|---|---|
| Profils, rôles et séparation des responsabilités | Autorisé si aucun secret ni contexte privé n'est exposé |
| Modèles et providers | Autorisé lorsqu'ils font partie de la documentation produit ; ne jamais publier la clé ni une URL d'accès authentifiée |
| Ports et services | À réserver aux pages d'architecture nécessaires ; ne jamais publier de token, route d'administration ou procédure d'accès |
| Version Hermes | Autorisée dans une page technique si elle est mesurée et utile ; éviter de multiplier la version dans les pages secondaires |
| Workflows et processus métier | Autorisés sans données réelles, identifiants internes ni chemins de secrets |
| Compteurs de crons et statistiques | Mentionner le périmètre, la date et la source ; ne pas publier de données individuelles |
| Incidents | Décrire le symptôme et la décision de sécurité ; exclure PID, traces sensibles, tokens et chemins privés |
| Schémas Mermaid | Autorisés après vérification qu'ils ne contiennent ni secret, ni URL interne, ni donnée personnelle |

La page d'architecture canonique applique cette règle : elle décrit les composants et les rôles, mais ne publie pas les valeurs de credentials ni les fichiers sensibles.

## 🟢 Ce qui doit rester interne

Les informations suivantes restent dans Leo Docs local, les vaults ou les runbooks privés :

- commandes exactes de restauration avec secrets ou comptes administrateurs ;
- chemins absolus de `/home/tofdan/.hermes/`, bases et volumes ;
- sorties complètes de logs et rapports de sécurité ;
- identifiants de jobs, PID, noms de fichiers de tokens et IDs de dossiers cloud ;
- contenu des mémoires, sessions, obligations Hive et dossiers professionnels ;
- détails d'accès aux dashboards d'administration ;
- procédures de rotation et de révocation des credentials.

Une page publique peut renvoyer vers le nom fonctionnel d'un processus, mais pas publier son secret ni reproduire un fichier de configuration sensible.

## 📋 Checklist avant commit ou publication

### Contenu

- [ ] Aucun mot de passe, token, clé API ou secret de session.
- [ ] Aucun fichier `.env`, OAuth, recovery-kit ou credential copié.
- [ ] Aucun email privé, GSM, adresse ou identifiant personnel.
- [ ] Aucun message, session, mémoire ou document professionnel réel.
- [ ] Les rôles des profils sont conformes à l'état actuel.
- [ ] Les chiffres portent une date et un périmètre.
- [ ] Les incidents sont résumés sans PID, log sensible ou chemin privé.

### Structure

- [ ] Les liens internes pointent vers des pages existantes.
- [ ] Les blocs Mermaid sont équilibrés et ne contiennent pas de données sensibles.
- [ ] Les pages retirées de la navigation sont archivées avec un bandeau clair.
- [ ] La carte documentaire est mise à jour dans le même lot.
- [ ] Les pages générées sont corrigées dans leur source, pas dans leur sortie.

### Vérification

```bash
# Depuis le dépôt Wiki Hermes
mkdocs build --strict --site-dir /tmp/hermes-wiki-site
git diff --check

# Recherche indicative de secrets dans les fichiers modifiés
grep -RInE 'AIza[0-9A-Za-z_-]{20,}|sk-[0-9A-Za-z_-]{20,}|BEGIN .*PRIVATE KEY' docs/ || true
```

La recherche automatique ne remplace pas une relecture humaine : un secret peut prendre une autre forme.

## Gestion d'un incident documentaire

Si un secret est publié par erreur :

1. **Ne pas seulement supprimer la ligne dans le fichier courant.** Considérer le secret comme compromis.
2. Révoquer ou faire tourner le credential via la procédure privée appropriée.
3. Retirer le contenu du Wiki et de l'historique public selon la procédure GitHub prévue.
4. Vérifier les caches et les copies générées.
5. Auditer les pages liées et la carte documentaire.
6. Documenter l'incident sans reproduire le secret.

Si une donnée professionnelle ou personnelle est publiée, la retirer du Wiki public et conserver la version légitime uniquement dans l'espace privé autorisé.

## Délimitation des destinations

- **Wiki Hermes public** : architecture et procédures générales nettoyées.
- **Leo Docs local** : index documentaire interne ; il ne transforme pas une donnée sensible en donnée publiable.
- **Vaults et espaces privés** : mémoires, dossiers professionnels, secrets et rapports détaillés.

La présence d'une page dans Leo Docs ne constitue donc pas une autorisation de la publier sur GitHub Pages.

## Historique de la revue

| Date | Revue |
|---|---|
| 07/07/2026 | Création de la page de bonnes pratiques documentaires |
| 21/09/2026 | Révision : distinction public/interne/secret, contrôle des pages générées, processus d'incident et alignement avec l'architecture actuelle |

> **Source de référence :** cette page, la carte documentaire et la procédure de maintenance du Wiki Hermes. Les règles de gestion des credentials restent dans les espaces internes LEO.

# Architecture Système

## 1. Infrastructure

### Host LEO
- **Description**: Le serveur principal où est hébergé l'ensemble du système LEO.

### Container Hermes
- **Description**: Conteneur dédié pour exécuter des tâches et des scripts en arrière-plan, garantissant une isolation optimale.

### Chromebook
- **Description**: Utilisé pour les sessions utilisateur et la communication avec DeepSeek via Telegram et CLI.

## 2. Budget API

- **Balance DeepSeek actuelle**: $41.97
- **Seuils**:
  - Alertes de seuil bas: $30
  - Arrêt automatique des tâches si le budget est inférieur à ce seuil.

## 3. Crons Actifs

| Nom | Horaire | Description |
| --- | ------- | ----------- |
| daily-backup | `0 6 * * *` | Effectue une sauvegarde quotidienne du système à minuit (heure locale) |
| docs-update | `0 8 * * 1` | Met à jour les documents et la documentation du système le lundi matin |

## 4. Sessions & Utilisation

- **Total des sessions**: 41
- **Total des messages**: 2965
- **Sessions récentes**:
  - CLI: 3 sessions
  - Telegram: 17 sessions
- **Taille de la base de données**: 40.4 MB
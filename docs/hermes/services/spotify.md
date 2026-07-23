# 🎵 Spotify — Contrôle musical

Plugin Spotify natif Hermes connecté le **21/06/2026** via OAuth PKCE.

## 🔧 Configuration

- **App développeur :** Spotify Developer (Client ID : `7740b2db...`)
- **Auth :** OAuth PKCE avec refresh token auto
- **Compte :** Spotify Premium (nécessaire pour le contrôle de lecture)

## 📱 Devices connectés

| Device | Type | Statut |
|--------|------|--------|
| Pixel 8 Pro | Smartphone 📱 | ✅ |
| Web Player (Chrome) | Computer 💻 | ✅ |

## 🎮 Commandes disponibles

Depuis Telegram, dire :

- ▶️ `"mets de la musique"` — lecture
- ⏸️ `"stop"` — pause
- ⏭️ `"suivant"` / ⏮️ `"retour"` — navigation
- 🔊 `"volume à 50%"` — volume
- 🔀 `"shuffle"` / 🔁 `"repeat"` — modes
- 📋 `"liste les devices"` — voir appareils
- 🔍 `"cherche du jazz"` — recherche catalogue
- 📚 `"mes playlists"` — liste playlists

## 🛠️ 7 outils Hermes

| Outil | Actions |
|-------|---------|
| `spotify_playback` | play, pause, next, previous, seek, volume, shuffle, repeat, recently played |
| `spotify_devices` | list, transfer |
| `spotify_queue` | get, add |
| `spotify_search` | recherche tracks, albums, artists, playlists |
| `spotify_playlists` | list, get, create, add_items, remove_items |
| `spotify_albums` | get, tracks |
| `spotify_library` | list, save, remove (tracks/albums) |

## ⚠️ Notes

- Spotify doit être **ouvert sur au moins un appareil** pour contrôler la lecture
- Le token se **rafraîchit automatiquement** — aucune intervention nécessaire
- Le compte **Premium** est requis pour play/pause/next
*Document mis à jour le 04/07/2026 à 22:48 — Léo 🦁*

> 🤖 Dernier audit : 23/07/2026 à 05:00 (UTC+2)


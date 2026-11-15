# Orbit Play Mobile

Android client project for local-network PS5 Remote Play.

## Target
- Android 11+ (min SDK 30)
- Local Wi-Fi connection; no cloud relay
- 720p / 30 FPS default target
- Optional 1080p / 30 FPS target
- Arabic and English UI

## Important status
This repository starts the Android application shell and build pipeline. A working PS5 Remote Play session requires integration and validation of the Chiaki-ng Android engine and PSN/console pairing. The UI alone is not a functioning streaming client.

## Build
Open this project in Android Studio (Giraffe or newer), install Android SDK 35 and NDK, then build the debug APK.

GitHub Actions builds a debug APK on pushes to main.

# Orbit Play Mobile

Android Remote Play build workspace targeting Android 11+.

## Remote Play engine
This repository pins the upstream [Chiaki-ng](https://github.com/chiaki-ng/chiaki-ng) project as a Git submodule at `chiaki-ng/`. The Android app and native Remote Play engine are built from that upstream source; this avoids shipping a nonfunctional mock streaming screen.

## Build
GitHub Actions checks out the Chiaki-ng submodule recursively, installs JDK 17, Android SDK 35, NDK 28.2.13676358 and CMake 3.22.1, then runs:

```sh
gradle -p chiaki-ng/android assembleDebug --no-daemon
```

The debug APK is uploaded as the workflow artifact `orbit-play-mobile-chiaki-ng-debug`.

## Important status and scope
- Chiaki-ng's Android client supports PS4/PS5 Remote Play and has minSdk 24, so Android 11 is within its declared minimum.
- The current APK build is the upstream Chiaki-ng Android client with its native engine, not yet a rebranded Orbit Play interface.
- The earlier Orbit Play Compose screen is a separate prototype and is not wired to the native streaming engine yet.
- 720p/30 FPS and 1080p/30 FPS presets are desired Orbit Play targets; actual available stream settings are governed by the integrated upstream client and must be tested on-device.
- This project does not provide cloud relaying. Use the phone and console on the same local network for the intended local-Wi-Fi setup.

## Licensing
Chiaki-ng is licensed under AGPL-3.0. Its source, notices and license must be preserved when redistributing builds or modifications. See the upstream repository for the authoritative license and notices.

This project is not endorsed or certified by Sony Interactive Entertainment.

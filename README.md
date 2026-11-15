# Orbit Play Mobile

Android Remote Play application workspace targeting Android 11+.

## Remote Play engine
Orbit Play currently builds the Android client and native Remote Play engine from the pinned upstream [Chiaki-ng](https://github.com/chiaki-ng/chiaki-ng) Git submodule at `chiaki-ng/`. The app is based on the real Chiaki-ng PS4/PS5 Remote Play client, not a mock streaming screen.

## Current Android build
GitHub Actions installs JDK 17, Android SDK 35, NDK 28.2.13676358, CMake 3.22.1 and Protocol Buffers compiler, then builds:

```sh
gradle -p chiaki-ng/android assembleDebug --no-daemon
```

The workflow applies Orbit Play branding and lightweight defaults before building. The default stream profile is 720p / 30 FPS. The upstream client still exposes its own stream settings, console discovery, registration and on-screen controls. The debug APK is uploaded as `orbit-play-mobile-chiaki-ng-debug`.

## Status and limitations
- The Android client declares minSdk 24, so Android 11 is within its declared minimum; device compatibility still needs a real installation test.
- The current build is the Chiaki-ng Android client with Orbit Play branding and default stream settings. The separate Compose prototype UI is not yet connected to the native streaming engine.
- 1080p / 30 FPS remains selectable through the upstream client's stream settings; actual quality and performance must be tested on the phone and network.
- Intended use is local Wi-Fi with the phone and PS5 on the same network. No cloud relay is included.
- This APK has not yet been verified in a real PS5 session.

## Licensing
Chiaki-ng is licensed under AGPL-3.0. Preserve its source, notices and license when redistributing builds or modifications. See the upstream repository for authoritative notices.

This project is not endorsed or certified by Sony Interactive Entertainment.

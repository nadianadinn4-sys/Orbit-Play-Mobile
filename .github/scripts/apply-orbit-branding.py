#!/usr/bin/env python3
"""Brand the real Chiaki-ng Android client as Orbit Play and set safe defaults."""
from pathlib import Path

root = Path("chiaki-ng/android/app/src/main")
prefs = root / "java/com/metallic/chiaki/common/Preferences.kt"
strings = root / "res/values/strings.xml"

p = prefs.read_text(encoding="utf-8")
# Chiaki-ng already defaults to 720p; assert this so an upstream change cannot
# silently invalidate the Orbit Play profile.
resolution = "val resolutionDefault = Resolution.RES_720P"
if p.count(resolution) != 1:
    raise SystemExit("Expected 720p default was not found; refusing unsafe build")
old_fps = "val fpsDefault = FPS.FPS_60"
new_fps = "val fpsDefault = FPS.FPS_30"
if p.count(old_fps) == 1:
    p = p.replace(old_fps, new_fps)
elif p.count(new_fps) != 1:
    raise SystemExit("Could not safely set the 30 FPS default")
prefs.write_text(p, encoding="utf-8")

s = strings.read_text(encoding="utf-8")
replacements = {
    '<string name="app_name">Chiaki</string>':
        '<string name="app_name">Orbit Play</string>',
    '<string name="title_main">Chiaki 千秋</string>':
        '<string name="title_main">ORBIT PLAY</string>',
}
for old, new in replacements.items():
    if s.count(old) == 1:
        s = s.replace(old, new)
    elif s.count(new) != 1:
        raise SystemExit(f"Could not safely apply branding: {old}")
strings.write_text(s, encoding="utf-8")

print("Orbit Play: branding applied; default resolution 720p; default frame rate 30 FPS.")

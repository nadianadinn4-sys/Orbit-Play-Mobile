#!/usr/bin/env python3
"""Apply Orbit Play branding and lightweight default stream settings to Chiaki-ng."""
from pathlib import Path

root = Path("chiaki-ng/android/app/src/main")
prefs = root / "java/com/metallic/chiaki/common/Preferences.kt"
strings = root / "res/values/strings.xml"

p = prefs.read_text(encoding="utf-8")
old_fps = "val fpsDefault = FPS.FPS_60"
new_fps = "val fpsDefault = FPS.FPS_30"
if p.count(old_fps) != 1:
    raise SystemExit("Could not safely locate Chiaki-ng default FPS setting")
prefs.write_text(p.replace(old_fps, new_fps), encoding="utf-8")

s = strings.read_text(encoding="utf-8")
replacements = {
    '<string name="app_name">Chiaki</string>':
        '<string name="app_name">Orbit Play</string>',
    '<string name="title_main">Chiaki 千秋</string>':
        '<string name="title_main">ORBIT PLAY</string>',
}
for old, new in replacements.items():
    if s.count(old) != 1:
        raise SystemExit(f"Could not safely locate branding string: {old}")
    s = s.replace(old, new)
strings.write_text(s, encoding="utf-8")

print("Orbit Play branding applied; default stream profile is 720p / 30 FPS.")

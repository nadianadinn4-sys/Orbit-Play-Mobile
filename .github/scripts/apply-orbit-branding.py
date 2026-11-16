#!/usr/bin/env python3
"""Apply Orbit Play visual identity to the real Chiaki-ng Android client."""
from pathlib import Path

root = Path("chiaki-ng/android/app/src/main")
prefs = root / "java/com/metallic/chiaki/common/Preferences.kt"
strings = root / "res/values/strings.xml"
colors = root / "res/values/colors.xml"
layout = root / "res/layout/activity_main.xml"

# Keep the real Chiaki-ng streaming and console-management code intact.
p = prefs.read_text(encoding="utf-8")
resolution = "val resolutionDefault = Resolution.RES_720P"
if p.count(resolution) != 1:
    raise SystemExit("Expected 720p default was not found; refusing unsafe build")
old_fps, new_fps = "val fpsDefault = FPS.FPS_60", "val fpsDefault = FPS.FPS_30"
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
    '<string name="display_hosts_empty_discovery_off_info">No consoles added yet.\\nEnable Discovery to automatically find consoles on your local network.</string>':
        '<string name="display_hosts_empty_discovery_off_info">Your PlayStation will appear here\\nTurn on local network discovery or add your PS5 manually.</string>',
    '<string name="display_hosts_empty_discovery_on_info">No consoles added or discovered.</string>':
        '<string name="display_hosts_empty_discovery_on_info">Searching your local network for PlayStation consoles…</string>',
}
for old, new in replacements.items():
    if s.count(old) == 1:
        s = s.replace(old, new)
    elif s.count(new) != 1:
        raise SystemExit(f"Could not safely apply Orbit strings: {old}")
strings.write_text(s, encoding="utf-8")

# Midnight/navy surfaces with a clear cyan Orbit accent.
c = colors.read_text(encoding="utf-8")
color_replacements = {
    '<color name="primary">#162d50</color>': '<color name="primary">#101B2D</color>',
    '<color name="primary_dark">#000128</color>': '<color name="primary_dark">#080E18</color>',
    '<color name="accent">#ffaaee</color>': '<color name="accent">#39C6F4</color>',
    '<color name="floating_action_button_speed_dial_background">#fafafa</color>':
        '<color name="floating_action_button_speed_dial_background">#17263A</color>',
    '<color name="floating_action_button_speed_dial_tint">#333333</color>':
        '<color name="floating_action_button_speed_dial_tint">#EAF7FF</color>',
}
for old, new in color_replacements.items():
    if c.count(old) != 1 and c.count(new) != 1:
        raise SystemExit(f"Could not safely apply Orbit color: {old}")
    c = c.replace(old, new)
colors.write_text(c, encoding="utf-8")

# Give the existing real console list a branded two-line header. All view IDs
# and click handlers used by Chiaki-ng are preserved.
x = layout.read_text(encoding="utf-8")
x = x.replace(
    '    android:clipChildren="false">',
    '    android:clipChildren="false"\\n    android:background="#080E18">',
    1
)
old_title = '''            <androidx.appcompat.widget.AppCompatTextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_gravity="center"
                android:fontFamily="sans-serif-condensed"
                android:text="@string/title_main"
                android:textColor="?attr/colorOnPrimary"
                android:textSize="20dp" />'''
new_title = '''            <LinearLayout
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_gravity="center"
                android:gravity="center"
                android:orientation="vertical"
                android:paddingTop="5dp"
                android:paddingBottom="5dp">
                <androidx.appcompat.widget.AppCompatTextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:fontFamily="sans-serif-black"
                    android:letterSpacing="0.12"
                    android:text="@string/title_main"
                    android:textColor="#39C6F4"
                    android:textSize="21sp"
                    android:textStyle="bold" />
                <androidx.appcompat.widget.AppCompatTextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:fontFamily="sans-serif"
                    android:text="PS5 REMOTE PLAY"
                    android:textColor="#AFC4D8"
                    android:textSize="10sp"
                    android:letterSpacing="0.18" />
            </LinearLayout>'''
if old_title in x:
    x = x.replace(old_title, new_title, 1)
elif new_title not in x:
    raise SystemExit("Could not safely replace the main toolbar title")
layout.write_text(x, encoding="utf-8")

print("Orbit Play visual identity applied to Chiaki-ng; 720p / 30 FPS defaults verified.")

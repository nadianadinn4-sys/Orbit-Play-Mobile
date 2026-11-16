#!/usr/bin/env python3
"""Apply Orbit Play branding to the real Chiaki-ng Android client."""
from pathlib import Path

root = Path("chiaki-ng/android/app/src/main")
prefs = root / "java/com/metallic/chiaki/common/Preferences.kt"
strings = root / "res/values/strings.xml"
colors = root / "res/values/colors.xml"
styles = root / "res/values/styles.xml"
layout = root / "res/layout/activity_main.xml"
host_layout = root / "res/layout/item_display_host.xml"

def replace_once(source, old, new, label):
    count = source.count(old)
    if count != 1:
        if source.count(new) == 1:
            return source
        raise SystemExit(f"Could not safely apply {label}: expected one source match, found {count}")
    return source.replace(old, new, 1)

# Preserve Chiaki-ng's real streaming, discovery, registration and controls code.
p = prefs.read_text(encoding="utf-8")
resolution = "val resolutionDefault = Resolution.RES_720P"
if p.count(resolution) != 1:
    raise SystemExit("Expected 720p default was not found; refusing unsafe build")
p = replace_once(p, "val fpsDefault = FPS.FPS_60", "val fpsDefault = FPS.FPS_30", "30 FPS default") if "val fpsDefault = FPS.FPS_30" not in p else p
if p.count("val fpsDefault = FPS.FPS_30") != 1:
    raise SystemExit("Could not verify exactly one 30 FPS default")
prefs.write_text(p, encoding="utf-8")

s = strings.read_text(encoding="utf-8")
for old, new, label in [
    ('<string name="app_name">Chiaki</string>', '<string name="app_name">Orbit Play</string>', "app name"),
    ('<string name="title_main">Chiaki 千秋</string>', '<string name="title_main">ORBIT PLAY</string>', "main title"),
    ('<string name="display_hosts_empty_discovery_off_info">No consoles added yet.\\nEnable Discovery to automatically find consoles on your local network.</string>',
     '<string name="display_hosts_empty_discovery_off_info">Your PlayStation will appear here\\nTurn on local network discovery or add your PS5 manually.</string>', "empty discovery message"),
    ('<string name="display_hosts_empty_discovery_on_info">No consoles added or discovered.</string>',
     '<string name="display_hosts_empty_discovery_on_info">Searching your local network for PlayStation consoles…</string>', "discovery message"),
]:
    s = replace_once(s, old, new, label)
strings.write_text(s, encoding="utf-8")

c = colors.read_text(encoding="utf-8")
for old, new, label in [
    ('<color name="primary">#162d50</color>', '<color name="primary">#101B2D</color>', "primary color"),
    ('<color name="primary_dark">#000128</color>', '<color name="primary_dark">#080E18</color>', "dark primary color"),
    ('<color name="accent">#ffaaee</color>', '<color name="accent">#39C6F4</color>', "Orbit cyan"),
    ('<color name="floating_action_button_speed_dial_background">#fafafa</color>',
     '<color name="floating_action_button_speed_dial_background">#17263A</color>', "action menu surface"),
    ('<color name="floating_action_button_speed_dial_tint">#333333</color>',
     '<color name="floating_action_button_speed_dial_tint">#EAF7FF</color>', "action menu text"),
    ('<color name="stream_background">@android:color/black</color>',
     '<color name="stream_background">#050912</color>', "stream background"),
    ('<color name="stream_overlay_background">#77000000</color>',
     '<color name="stream_overlay_background">#DD08111F</color>', "stream overlay"),
]:
    c = replace_once(c, old, new, label)
colors.write_text(c, encoding="utf-8")

# Main console screen: retain all original view IDs and event handlers.
x = layout.read_text(encoding="utf-8")
x = replace_once(x, '    android:clipChildren="false">', '    android:clipChildren="false"\\n    android:background="#080E18">', "main screen background") if 'android:background="#080E18"' not in x else x
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

# Branded console cards, without changing any Chiaki-ng IDs or click targets.
h = host_layout.read_text(encoding="utf-8")
for old, new, label in [
    ('android:layout_height="250dp"', 'android:layout_height="224dp"', "console card height"),
    ('app:cardCornerRadius="4dp"', 'app:cardCornerRadius="18dp"\\n    app:cardBackgroundColor="#111C2D"', "console card surface"),
    ('android:layout_marginTop="8dp"', 'android:layout_marginTop="10dp"', "console card top spacing"),
    ('android:layout_marginLeft="8dp"', 'android:layout_marginLeft="14dp"', "console card left spacing"),
    ('android:layout_marginRight="8dp"', 'android:layout_marginRight="14dp"', "console card right spacing"),
    ('android:elevation="8dp"', 'android:elevation="4dp"', "console card elevation"),
    ('android:textSize="32sp"\\n            android:gravity="center"\\n            android:textColor="?attr/colorOnSurface"',
     'android:textSize="27sp"\\n            android:gravity="center"\\n            android:textColor="#39C6F4"',
     "console name styling"),
    ('android:textSize="16sp"\\n            android:gravity="center"\\n            android:textColor="?attr/colorOnSurface"',
     'android:textSize="14sp"\\n            android:gravity="center"\\n            android:textColor="#C5D5E5"',
     "console address styling"),
]:
    h = replace_once(h, old, new, label)
h = h.replace('android:textColor="?attr/colorOnSurface"\\n            android:textSize="16sp"', 'android:textColor="#D8E8F5"\\n            android:textSize="14sp"', 1)
host_layout.write_text(h, encoding="utf-8")

# Dark system bars and matching Material surfaces for the real Chiaki activity.
t = styles.read_text(encoding="utf-8")
anchor = '        <item name="colorOnPrimary">#ffffff</item>'
addition = '''        <item name="colorSurface">#111C2D</item>
        <item name="colorOnSurface">#EAF7FF</item>
        <item name="colorPrimarySurface">#101B2D</item>
        <item name="android:windowBackground">#080E18</item>
        <item name="android:windowLightStatusBar">false</item>
        <item name="android:statusBarColor">#080E18</item>
        <item name="android:navigationBarColor">#080E18</item>'''
if addition not in t:
    t = replace_once(t, anchor, anchor + "\\n" + addition, "dark Orbit Material theme")
styles.write_text(t, encoding="utf-8")

print("Orbit Play identity applied to the real Chiaki-ng console screen; 720p / 30 FPS defaults verified.")

# presets.py
# Saves and loads transcode presets per show

import json
from pathlib import Path

PRESETS_FILE = Path("/Users/rachelmcintire/PycharmProjects/Claude/transcode_presets.json")

def save_preset(show, preset_name, settings):
    """Saves a transcode preset for a show."""
    all_presets = load_all_presets()
    if show not in all_presets:
        all_presets[show] = {}
    all_presets[show][preset_name] = settings
    with open(PRESETS_FILE, "w") as f:
        json.dump(all_presets, f, indent=2)

def load_presets_for_show(show):
    """Returns all presets for a given show."""
    all_presets = load_all_presets()
    return all_presets.get(show, {})

def load_all_presets():
    """Loads all presets from the file."""
    if not PRESETS_FILE.exists():
        return {}
    with open(PRESETS_FILE, "r") as f:
        return json.load(f)

def delete_preset(show, preset_name):
    """Deletes a preset for a show."""
    all_presets = load_all_presets()
    if show in all_presets and preset_name in all_presets[show]:
        del all_presets[show][preset_name]
        with open(PRESETS_FILE, "w") as f:
            json.dump(all_presets, f, indent=2)
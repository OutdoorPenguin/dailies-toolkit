from pathlib import Path
import csv                          # NEW
from datetime import datetime       # NEW

folder = Path("/Users/rachmcintire/Desktop/test_folder")
log_file = folder / "rename_log.csv"  # NEW — log saves in the same folder

media_extensions = {".mov", ".mp4", ".mxf", ".dpx", ".exr", ".jpg", ".jpeg"}

camera = "A"
reel = 1
clip = 1
dry_run = False

files = sorted([f for f in folder.iterdir() if f.suffix.lower() in media_extensions])

log_entries = []  # NEW — collects each rename as we go

for i, file in enumerate(files):
    new_name = f"{camera}{reel:03d}C{clip + i:03d}{file.suffix.lower()}"
    new_path = folder / new_name

    if dry_run:
        print(f"[DRY RUN] {file.name}  →  {new_name}")
    else:
        file.rename(new_path)
        print(f"Renamed: {file.name}  →  {new_name}")
        log_entries.append({          # NEW
            "timestamp": datetime.now().isoformat(),
            "original": file.name,
            "renamed": new_name
        })

# NEW — write the log after all renames are done
if not dry_run and log_entries:
    with open(log_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "original", "renamed"])
        writer.writeheader()
        writer.writerows(log_entries)
    print(f"\nLog saved to: {log_file}")
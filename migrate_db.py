# migrate_db.py
# Adds new columns to existing database — safe to run multiple times

import sqlite3
from pathlib import Path

DB_FILE = Path("/Users/rachelmcintire/PycharmProjects/Claude/dailies.db")

NEW_COLUMNS = [
    ("sound_roll",        "TEXT"),
    ("audio_track_names", "TEXT"),
    ("sound_tc_start",    "TEXT"),
    ("sound_tc_end",      "TEXT"),
    ("sound_notes",       "TEXT"),
    ("is_wild",           "INTEGER DEFAULT 0"),
]

def migrate():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(clips)")
    existing = {row[1] for row in cursor.fetchall()}

    added = []
    skipped = []

    for col_name, col_type in NEW_COLUMNS:
        if col_name not in existing:
            cursor.execute(f"ALTER TABLE clips ADD COLUMN {col_name} {col_type}")
            added.append(col_name)
        else:
            skipped.append(col_name)

    conn.commit()
    conn.close()

    if added:
        print(f"✅ Added columns: {', '.join(added)}")
    if skipped:
        print(f"⏭️  Already existed: {', '.join(skipped)}")
    print("Migration complete.")

if __name__ == "__main__":
    migrate()

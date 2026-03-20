# dailies-toolkit 🎬

A suite of Python tools for post-production dailies workflow. Built for film and TV — handles ingest, metadata, color, and notifications.

---

## Tools

### 📁 File Renamer (`renamer.py`)
Batch renames media files to camera roll convention (e.g. `A001C001.mov`). Includes dry run mode so you can preview before anything changes. Logs every rename to a CSV.

### 📋 Ingest Log Parser (`log_parser.py`)
Reads a media ingest log CSV and flags potential issues — duplicate filenames, missing file sizes, zero-byte files, and bad status flags. Outputs a clean report CSV.

### 🔍 Folder Monitor (`folder_monitor.py`)
Scans a folder of media files and pulls codec, resolution, and frame rate via ffprobe. Flags mixed codecs, resolutions, and frame rates across a camera roll. Logs results to CSV.

### 🗄️ Dailies Database (`dailies_db.py`)
Creates a SQLite database to track clip metadata by show, episode, and camera. Schema includes 37 columns covering video, audio, camera, lens, exposure, color, and production info.

### 📥 CSV Importer (`import_clips.py`)
Imports clip metadata from CSV exports into the database. Supports Premiere, Resolve, Avid, Silverstack, and Pomfort. Normalizes column names automatically, detects duplicates, and matches CDL files by clip name.

### 🎨 CDL Parser (`cdl_parser.py`)
Reads `.cdl` files and extracts slope, offset, power, and saturation values per clip. Called automatically by the importer when CDL files are present.

### 🗺️ Column Mapper (`column_map.py`)
Normalizes column names from different app exports into a standard format so the importer works regardless of source.

### 📣 Slack Notifier (`notifier.py`)
Sends a formatted Slack summary after ingest — show, episode, clip count, codec/resolution/fps, and any consistency warnings.

---

## Requirements
- Python 3.x
- ffmpeg / ffprobe (`brew install ffmpeg`)
- `pip install watchdog pandas requests python-dotenv`
- DB Browser for SQLite — https://sqlitebrowser.org/dl/

---

## Setup
1. Clone the repo
2. Install requirements above
3. Create a `.env` file with your Slack token: `SLACK_TOKEN=xoxb-yourtoken`
4. Run `dailies_db.py` once to create the database
5. Use `import_clips.py` to import from a CSV, or `dailies_db.py` to scan a folder directly

---

*Built by a post production professional learning Python. Project 6 — a full visual dailies app — coming soon.*

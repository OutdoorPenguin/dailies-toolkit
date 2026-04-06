# dailies-toolkit 🎬

A suite of Python tools for post-production dailies workflow. Built for film and TV — handles ingest, metadata, color, transcoding, sync, and notifications.

---

## Tools

### 🖥️ Dailies App (`dailies_app.py`)
Full desktop application for managing dailies. Features:
- Drag and drop media ingest via ffprobe
- CSV import from Premiere, Resolve, Avid, Silverstack, and Pomfort
- 48-column database with search, sort, horizontal scroll
- Customizable column visibility and order — right-click headers or use the Columns button, saved per view
- Active show selector — scopes all operations to a single show
- Filter by show, episode, and camera with saved views
- Consistency report — flags mixed codecs, resolutions, and frame rates
- Checksum generation and verification (MD5, xxHash, SHA-256)
- Transcode pipeline with CDL, LUT (input → CDL → output), retime, and burnins
- Show presets — save transcode configs per show and run all with one click via Render
- Audio sync dialog — TC-based matching, manual offset, scratch audio replacement
- Sound report import — parses sound report CSVs, matches to video clips by TC, flags wild takes, updates circle/select from sound mixer notes
- Slack notifications
- Custom column export to CSV, ALE, FCP7 XML, FCPXML, and EDL

### 🎨 CDL Extractor (`cdl_extractor.py`)
Standalone desktop app — drag an EDL onto it, extract embedded CDL values, and export one `.cdl` or `.cc` file per clip. Name files by clip name, locator, or reel. Dark UI with Netflix red highlights. Distributable as a standalone `.app` — no Python required for end users.

### 📁 File Renamer (`renamer.py`)
Batch renames media files to camera roll convention (e.g. `A001C001.mov`). Dry run mode previews before renaming. Logs every rename to CSV.

### 📋 Ingest Log Parser (`log_parser.py`)
Reads a media ingest log CSV and flags potential issues — duplicate filenames, missing file sizes, zero-byte files, and bad status flags.

### 🔍 Folder Monitor (`folder_monitor.py`)
Scans a folder of media files and pulls codec, resolution, and frame rate via ffprobe. Flags mixed codecs, resolutions, and frame rates.

### 🗄️ Dailies Database (`dailies_db.py`)
Creates the SQLite database schema — 48 columns covering video, audio, camera, lens, exposure, color, checksums, sound report data, and production metadata.

### 📥 CSV Importer (`import_clips.py`)
Imports clip metadata from CSV exports into the database. Normalizes column names automatically across different app exports. Flags duplicates per show.

### 🎨 CDL Parser (`cdl_parser.py`)
Reads `.cdl` files and extracts slope, offset, power, and saturation values per clip.

### 🗺️ Column Mapper (`column_map.py`)
Normalizes column names from Premiere, Resolve, Avid, Silverstack, and Pomfort into a standard format.

### 📣 Slack Notifier (`notifier.py`)
Sends a formatted Slack summary after ingest — show, episode, clip count, codec/resolution/fps, and consistency warnings.

### 📤 Exporters (`exporters.py`)
Handles all export formats: CSV, ALE, FCP7 XML, FCPXML, EDL.

### 🔐 Checksum Verifier (`checksum.py`)
Generates and verifies MD5, xxHash, and SHA-256 checksums for media files. Stored in the database and verifiable any time via the Verify Files button.

### 🎬 Transcoder (`transcoder.py`)
Handles ffmpeg transcoding with CDL baked in, LUT application (input LUT → CDL → output LUT), burnins, and retime. Supports ProRes 422/HQ/LT/4444/4444XQ, H.264, H.265, DNxHD, DNxHR SQ/HQ/HQX/444, JPEG 2000, Uncompressed 10-bit, and MXF OP1a.

### 🔊 Syncer (`syncer.py`)
Audio/video sync engine. Extracts timecode from media files via ffprobe, calculates offset between video and audio TC, and merges audio into video via ffmpeg. Supports embed or separate output, manual offset override, and scratch audio replacement.

### 🎙️ Sound Report Importer (`sound_report.py`)
Parses sound report CSVs (supports multiple naming conventions). Matches audio rows to video clips by Start TC within a configurable frame tolerance. Updates circle/select flag from sound mixer notes. Flags unmatched rows as wild takes and imports them separately so editors know about room tone, wild lines, and other audio without associated video.

### ⚙️ Presets (`presets.py`)
Saves and loads transcode presets per show. Configure once, render every day with one click.

### ⭐ Views (`views.py`)
Saves and loads favorite filter combos — including column visibility and order — in the app sidebar.

---

## Requirements
- Python 3.x
- ffmpeg / ffprobe — `brew install ffmpeg`
- ffmpeg with freetype (for burnins) — download static build from osxexperts.net, place at `/Applications/ffmpeg`
- `pip install watchdog pandas requests python-dotenv PyQt6 Pillow xxhash librosa scipy soundfile`
- DB Browser for SQLite — https://sqlitebrowser.org/dl/

---

## Setup
1. Clone the repo
2. Install requirements above
3. Create a `.env` file with your Slack token: `SLACK_TOKEN=xoxb-yourtoken`
4. Run `dailies_db.py` once to create the database
5. If upgrading an existing database, run `migrate_db.py` to add new columns
6. Launch `dailies_app.py` to start the app

## Building the CDL Extractor as a standalone app
```
pyinstaller --windowed --name "CDL Extractor" --icon "CDL_Extractor.icns" cdl_extractor.py
```
The `.app` will appear in the `dist` folder. Zip and share — no Python needed on the receiving end.

---

## Roadmap
- Burnin UI redesign and field population fix
- Column reordering in column manager dialog
- Framing/resolution change (scale, crop, letterbox, pillarbox)
- Playback/preview with LUT applied
- Timeline/visual view with context-aware rendering
- Sound report conflict resolution UI (multiple TC matches)
- Waveform-based audio sync
- Audio channel remapping

---

*Built by a post production professional learning Python. Active development ongoing.*

# exporters.py
# Handles exporting clips to various formats
# Supports: CSV, ALE, FCP7 XML, FCPXML, EDL

import csv
from pathlib import Path
from datetime import datetime

def export_csv(clips, output_path):
    """Exports clips to a CSV file."""
    if not clips:
        return

    keys = clips[0].keys()
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(clips)

def export_ale(clips, output_path):
    """Exports clips to Avid Log Exchange (.ale) format."""
    with open(output_path, "w") as f:
        # ALE header
        f.write("Heading\n")
        f.write("FIELD_DELIM\tTABS\n")
        f.write("VIDEO_FORMAT\t1080\n")
        f.write("AUDIO_FORMAT\t48000\n")
        f.write(f"FPS\t{clips[0].get('fps', '24') if clips else '24'}\n")
        f.write("\n")

        # Column headers
        columns = ["Name", "Tracks", "Start", "End", "Tape", "Scene", "Take"]
        f.write("Column\n")
        f.write("\t".join(columns) + "\n")
        f.write("\n")

        # Data
        f.write("Data\n")
        for clip in clips:
            row = [
                clip.get("file_name", ""),
                "V",
                clip.get("start_tc", "00:00:00:00"),
                clip.get("end_tc", "00:00:00:00"),
                clip.get("reel", ""),
                clip.get("scene", ""),
                clip.get("circle_take", ""),
            ]
            f.write("\t".join(str(v) for v in row) + "\n")

def export_fcp7_xml(clips, output_path):
    """Exports clips to FCP7 XML format."""
    with open(output_path, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<!DOCTYPE xmeml>\n')
        f.write('<xmeml version="5">\n')
        f.write('  <bin>\n')
        f.write('    <name>Dailies Export</name>\n')
        f.write('    <children>\n')
        for clip in clips:
            f.write('      <clip>\n')
            f.write(f'        <name>{clip.get("file_name", "")}</name>\n')
            f.write(f'        <duration>0</duration>\n')
            f.write(f'        <rate><timebase>{clip.get("fps", "24")}</timebase></rate>\n')
            f.write(f'        <in>{clip.get("start_tc", "")}</in>\n')
            f.write(f'        <out>{clip.get("end_tc", "")}</out>\n')
            f.write('      </clip>\n')
        f.write('    </children>\n')
        f.write('  </bin>\n')
        f.write('</xmeml>\n')

def export_fcpxml(clips, output_path):
    """Exports clips to FCPXML format."""
    with open(output_path, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<!DOCTYPE fcpxml>\n')
        f.write('<fcpxml version="1.9">\n')
        f.write('  <resources>\n')
        for i, clip in enumerate(clips):
            f.write(f'    <asset id="r{i+1}" name="{clip.get("file_name", "")}" />\n')
        f.write('  </resources>\n')
        f.write('  <library>\n')
        f.write('    <event name="Dailies Export">\n')
        f.write('      <project name="Dailies">\n')
        f.write('        <sequence>\n')
        f.write('          <spine>\n')
        for i, clip in enumerate(clips):
            f.write(f'            <asset-clip ref="r{i+1}" name="{clip.get("file_name", "")}" />\n')
        f.write('          </spine>\n')
        f.write('        </sequence>\n')
        f.write('      </project>\n')
        f.write('    </event>\n')
        f.write('  </library>\n')
        f.write('</fcpxml>\n')

def export_edl(clips, output_path):
    """Exports clips to EDL format."""
    with open(output_path, "w") as f:
        f.write("TITLE: Dailies Export\n")
        f.write("FCM: NON-DROP FRAME\n\n")
        for i, clip in enumerate(clips):
            f.write(f"{i+1:03d}  ")
            f.write(f"{clip.get('reel', 'AX'):<8} ")
            f.write("V     C        ")
            f.write(f"{clip.get('start_tc', '00:00:00:00')} ")
            f.write(f"{clip.get('end_tc', '00:00:00:00')} ")
            f.write(f"00:00:00:00 00:00:00:00\n")
            f.write(f"* FROM CLIP NAME: {clip.get('file_name', '')}\n\n")
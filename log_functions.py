from datetime import datetime
import json
LEVELS=["ERROR", "INFO", "WARNING", "UNKNOWN", "INVALID"]

def read_log_file(file):
    text = file.read_text(encoding="utf-8")
    lines = text.splitlines()
    return lines 

def count_log_levels(lines):
    zaehlen = dict.fromkeys(LEVELS, 0)
  
    for line in lines:
        parts = line.split()

        if not parts:
           continue

        if len(parts) < 3:
           zaehlen["INVALID"] += 1
           continue
        try:
           datetime.strptime(parts[0]+ " " + parts[1], "%Y-%m-%d %H:%M:%S")
        except ValueError:
           zaehlen["INVALID"] += 1
           continue
        level = parts[2]
        if level in LEVELS:
           zaehlen[level] += 1
        else:
           zaehlen["UNKNOWN"] += 1
    return zaehlen

def print_report(file, ergebnis, anzahl_zeilen):
   
    print(f"Zeilen: {anzahl_zeilen}")
   
    print(f"Datei: {file}")
   
    for level in ergebnis:
        print(f"{level}: {ergebnis[level]}")

    print("_________________________________")

def write_json_report(results, output_file):
   with open(output_file, "w", encoding="utf-8") as file:
      json.dump(results, file, indent=4)
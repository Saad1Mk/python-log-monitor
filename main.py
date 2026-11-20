from pathlib import Path
from log_functions import LEVELS, read_log_file,count_log_levels,print_report,write_json_report

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"

def main():

    gesamt = dict.fromkeys(LEVELS, 0)

    log_files = list(LOG_DIR.glob("*.log"))
    if not log_files:
        print("Keine .log-Dateien im logs-Ordner gefunden.")
        return

    for file in log_files:
        try:
            lines = read_log_file(file)
        except OSError as error:
            print(f"Fehler beim Lesen der Datei {file}: {error}")
            continue

        ergebnis = count_log_levels(lines)

        print_report(file, ergebnis, len(lines))

        for level in gesamt:
            gesamt[level] += ergebnis[level]

    print("Gesamtergebnis:")

    for level in gesamt:
        print(f"{level}: {gesamt[level]}")
    REPORT_FILE = BASE_DIR / "report.json"
    write_json_report(gesamt, REPORT_FILE)
if __name__ == "__main__":
    main()

   

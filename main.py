from pathlib import Path
from log_functions import LEVELS, read_log_file,count_log_levels,print_report,write_json_report
def main():

    gesamt = dict.fromkeys(LEVELS, 0)

    log_files = Path("logs").glob("*.log")

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
    write_json_report(gesamt, "report.json")
if __name__ == "__main__":
    main()

   

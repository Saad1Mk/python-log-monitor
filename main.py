from pathlib import Path
def count_log_levels(lines):
  zaehlen = {"ERROR" : 0, "INFO" : 0, "WARNING" : 0}
  
  for line in lines:
    parts =line.split()
    if len(parts)<3:
              continue
    level = parts[2]
    if level == "ERROR":
      zaehlen["ERROR"] += 1
    elif level == "INFO" :
      zaehlen["INFO"] += 1
    elif level == "WARNING":
      zaehlen["WARNING"] += 1
  return zaehlen

gesamt ={"ERROR" : 0, "INFO" : 0, "WARNING" : 0}
  
log_files = Path("logs").glob("*.log")

for file in log_files:
   try:
      text = file.read_text(encoding="utf-8")
   except OSError as error:
      print(f"Fehler beim lesen der Datei {file}: {error}")
      continue
      
   print(text)
   lines = text.splitlines()
   print(len(lines))

   ergebnis = count_log_levels(lines)
   print(f"{file}: {ergebnis}")

   for level in gesamt :
    gesamt[level] += ergebnis[level]

print(f"Gesamtergebnis : {gesamt}")
   
   
   


 

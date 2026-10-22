from pathlib import Path
text = Path("sample.log").read_text(encoding="utf-8")
lines = text.splitlines()
print(len(lines))

def count_log_levels(lines):
  zaehlen = {"ERROR":0, "INFO":0, "WARNING":0}
  for line in lines:
    if " ERROR " in line:
      zaehlen["ERROR"]+=1
    elif " INFO " in line:
      zaehlen["INFO"]+=1
    elif " WARNING " in line:
      zaehlen["WARNING"]+=1
  return zaehlen
  
 


print(f"Level-Anzahl={count_log_levels(lines)}")
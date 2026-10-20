from pathlib import Path
text= Path("sample.log").read_text(encoding="utf-8")
lines =text.splitlines()
print(len(lines))
def count_error(lines):
  zaehlen=0
  for line in lines:
    if " ERROR " in line:
      zaehlen+=1
  return zaehlen


print(f"ERROR={count_error(lines)}")
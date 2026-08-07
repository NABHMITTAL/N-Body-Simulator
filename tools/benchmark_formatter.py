raw_text = ""


lines = []
while True:
  line = input()
  if line == "":
    break
  lines.append(line)
raw_text = "\n".join(lines)


lines = raw_text.splitlines()

if "Performance Profile" in raw_text:
  benchmark_type = "performance"
elif "Leapfrog Internal Profile" in raw_text:
  benchmark_type = "leapfrog"
else:
  benchmark_type = "unknown"


#!/usr/bin/env python3

import subprocess
import sys

exe = sys.argv[1]

p = subprocess.run(
    ["ldd", exe],
    capture_output=True,
    text=True,
)

missing = []

for line in p.stdout.splitlines():
    if "not found" in line:
        missing.append(line.strip())

print(f"Executable: {exe}")

if missing:
    print("\nMISSING:")
    for m in missing:
        print(" ", m)
else:
    print("\nOK")

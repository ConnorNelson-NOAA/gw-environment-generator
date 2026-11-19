#!/usr/bin/env python3

import csv
import sys

if len(sys.argv) != 2:
    print("Usage: explain_exec.py <EXECUTABLE>")
    sys.exit(1)

exe = sys.argv[1]

found = None

with open("canonical_runtime_executables.csv") as f:

    for row in csv.DictReader(f):

        if row["executable"] == exe:
            found = row
            break

if not found:
    print("Executable not found")
    sys.exit(1)

print(f"Executable: {exe}")
print(f"Profile: {found['profile']}")

print()
print("Modules:")

for mod in found["modules"].split(";"):
    mod = mod.strip()
    if mod:
        print(f"  {mod}")

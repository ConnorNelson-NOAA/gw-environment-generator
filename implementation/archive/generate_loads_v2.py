#!/usr/bin/env python3

import csv
import sys

if len(sys.argv) != 2:
    print("Usage:")
    print("  generate_loads.py <JOB_NAME>")
    sys.exit(1)

job = sys.argv[1]

#
# job -> executable
#

inventory = {}

with open("final_confluence_inventory_normalized.csv") as f:
    r = csv.DictReader(f)

    for row in r:
        inventory[row["job"]] = row

if job not in inventory:
    print(f"ERROR: {job} not found")
    sys.exit(1)

row = inventory[job]

exe = row["executable"]

if not exe or exe == "N/A":
    print(f"# {job}")
    print("# ORCHESTRATION JOB")
    print("# No executable-derived module environment")
    sys.exit(0)

#
# executable -> modulefiles
#

modulefiles = {}

with open("canonical_modulefile_inventory_v2.csv") as f:
    r = csv.DictReader(f)

    for row in r:
        modulefiles[row["executable"]] = row["modulefiles"]

mods = modulefiles.get(exe, "")

print("module purge")
print()

if mods:
    for mod in mods.split(";"):
        mod = mod.strip()

        if mod:
            print(f"module load {mod}")
else:
    print(f"# No modulefile mapping found for {exe}")

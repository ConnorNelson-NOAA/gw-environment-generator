#!/usr/bin/env python3

import csv
import sys

if len(sys.argv) != 2:
    print("Usage: generate_loads_v3.py <JOB>")
    sys.exit(1)

job = sys.argv[1]

jobs = {}

with open("data/final_confluence_inventory_normalized.csv") as f:
    for row in csv.DictReader(f):
        jobs[row["job"]] = row

if job not in jobs:
    print("ERROR: job not found")
    sys.exit(1)

row = jobs[job]

if row["executable"] == "N/A":
    print("# orchestration job")
    sys.exit(0)

mods = {}

with open("data/canonical_modulefile_inventory_v2.csv") as f:
    for r in csv.DictReader(f):
        mods[r["executable"]] = r["modulefiles"]

print("module purge")
print()

#
# NOAA stack prerequisites
#
print("module load GDAS/orion.intel")
print("module load stack-oneapi/2024.2.1")

exe = row["executable"]

if exe == "gdas.x":
    print("module load intel-oneapi-mkl/2024.2.1")

if exe in mods:

    modulefiles = [
        x.strip()
        for x in mods[exe].split(";")
        if x.strip()
    ]

    if any("stack-intel-oneapi-mpi" in x for x in modulefiles):
        print("module load stack-intel-oneapi-mpi/2021.13")

    for m in modulefiles:

        if "stack-intel-oneapi-mpi" in m:
            continue

        print(f"module load {m}")

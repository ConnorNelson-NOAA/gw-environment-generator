#!/usr/bin/env python3

import csv
import sys

EMBEDDED = {
    "crtm",
    "fv3jedi",
    "ioda",
    "oops",
    "saber",
    "soca",
    "ufo",
    "vader"
}

if len(sys.argv) != 2:
    print("Usage: explain_job_v2.py <JOB>")
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

exe = row["executable"]

print()
print(f"Job:        {job}")
print(f"Executable: {exe}")
print(f"Profile:    {row['profile']}")

#
# Runtime providers
#

providers = []

with open("data/canonical_executable_inventory.csv") as f:
    for r in csv.DictReader(f):

        if r["executable"] == exe:

            providers = [
                x.strip()
                for x in r["modules"].split(";")
                if x.strip()
            ]

            break

#
# Modulefiles
#

modulefiles = []

with open("data/canonical_modulefile_inventory_v2.csv") as f:
    for r in csv.DictReader(f):

        if r["executable"] == exe:

            modulefiles = [
                x.strip()
                for x in r["modulefiles"].split(";")
                if x.strip()
            ]

            break

print()
print("Runtime Providers")
print("-----------------")

for p in sorted(providers):
    print(f"  {p}")

print()
print("Resolved Modulefiles")
print("--------------------")

print("  GDAS/orion.intel")
print("  stack-oneapi/2024.2.1")

if any("stack-intel-oneapi-mpi" in x for x in modulefiles):
    print("  stack-intel-oneapi-mpi/2021.13")

if exe == "gdas.x":
    print("  intel-oneapi-mkl/2024.2.1")

for m in sorted(modulefiles):

    if "stack-intel-oneapi-mpi" in m:
        continue

    print(f"  {m}")

embedded = sorted(
    set(providers).intersection(EMBEDDED)
)

print()
print("Embedded Libraries")
print("------------------")

if embedded:
    for e in embedded:
        print(f"  {e}")
else:
    print("  None")


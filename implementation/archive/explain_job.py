#!/usr/bin/env python3

import csv
import sys

MODULE_PROVIDED = {
    "atlas","bufr","eckit","fckit",
    "hdf5","jasper","jpeg","mpi",
    "netcdf-c","netcdf-cxx4",
    "netcdf-fortran",
    "openblas","parallelio",
    "png","udunits"
}

EMBEDDED = {
    "crtm","fv3jedi","ioda",
    "oops","saber","soca",
    "ufo","vader"
}

if len(sys.argv) != 2:
    print("Usage: explain_job.py <JOB>")
    sys.exit(1)

job = sys.argv[1]

inventory = {}

with open("final_confluence_inventory_normalized.csv") as f:
    r = csv.DictReader(f)

    for row in r:
        inventory[row["job"]] = row

row = inventory[job]

print()
print("Job:", row["job"])
print("Executable:", row["executable"])
print("Profile:", row["profile"])

mods = []

if row["modules"]:
    mods = row["modules"].split(";")

print()
print("Module-provided:")

for m in sorted(mods):
    if m in MODULE_PROVIDED:
        print("  ", m)

print()
print("Embedded libraries:")

for m in sorted(mods):
    if m in EMBEDDED:
        print("  ", m)

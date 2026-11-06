#!/usr/bin/env python3

import csv
import sys

if len(sys.argv) not in (2,3):
    print("Usage: generate_loads_v3.py <JOB>")
    sys.exit(1)

job = sys.argv[1]

import socket
import csv

if len(sys.argv) == 3:
    machine = sys.argv[2]
else:
    host = socket.gethostname().lower()

    mapping = {
        "orion": "orion",
        "orion-login": "orion",

        "ursa": "ursa",
        "ufe": "ursa",

        "hercules": "hercules",
        "hfe": "hercules",

        "hera": "hera",
        "gaea": "gaea",

        "wcoss": "wcoss2",
    }

    machine = "unknown"

    for token, value in mapping.items():
        if token in host:
            machine = value
            break


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

machine_profile = {}

with open("data/machine_profile_inventory.csv") as f:
    for profile_row in csv.DictReader(f):
        machine_profile[profile_row["machine"]] = profile_row


with open("data/canonical_modulefile_inventory_v2.csv") as f:
    for r in csv.DictReader(f):
        mods[r["executable"]] = r["modulefiles"]

print("module purge")
print()

#
# NOAA stack prerequisites
#
if machine in machine_profile:

    modulepaths = [
        x.strip()
        for x in machine_profile[machine]["modulepaths"].split(";")
        if x.strip()
    ]

    for mp in modulepaths:
        print(f"module use {mp}")

    print()

    print(f'module load {machine_profile[machine]["compiler_stack"]}')


exe = row["executable"]

if exe in mods:

    modulefiles = [
        x.strip()
        for x in mods[exe].split(";")
        if x.strip()
    ]

    if machine in machine_profile:
        print(f'module load {machine_profile[machine]["mpi_stack"]}')


    for m in modulefiles:

        if (
            "stack-intel-oneapi-mpi" in m
            or "stack-cray-mpich" in m
        ):
            continue

        print(f"module load {m}")

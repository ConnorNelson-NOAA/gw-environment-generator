#!/usr/bin/env python3

import csv
import sys

from module_utils import render_module

if len(sys.argv) != 2:
    print("Usage: generate_loads.py <JOB>")
    sys.exit(1)

job = sys.argv[1]

job_map = {}

with open("job_executables_phase4.csv") as f:

    for row in csv.DictReader(f):

        job_map[row["job"]] = row["executable"]

if job not in job_map:

    print(
        f"ERROR: no executable mapping for {job}"
    )

    sys.exit(1)

exe = job_map[job]

with open("canonical_runtime_executables.csv") as f:

    for row in csv.DictReader(f):

        if row["executable"] != exe:
            continue

        print("module purge")
        print()

        for mod in row["modules"].split(";"):

            line = render_module(mod)

            if line:
                print(line)

        sys.exit(0)

print(f"ERROR: executable not found: {exe}")
sys.exit(1)

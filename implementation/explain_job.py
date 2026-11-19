#!/usr/bin/env python3

import csv
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: explain_job.py <JOB>")
    sys.exit(1)

job = sys.argv[1]

job_map = {}

with open("job_executables_phase4.csv") as f:
    for row in csv.DictReader(f):
        job_map[row["job"]] = row

if job not in job_map:
    print("Job not found")
    sys.exit(1)

row = job_map[job]
exe = row["executable"]

print(f"Job: {job}")
print(f"Executable: {exe}")
print(f"Confidence: {row['confidence']}")

yaml_file = Path(
    f"yaml/executables_v2/{exe}.yaml"
)

if not yaml_file.exists():
    print(f"Missing YAML: {yaml_file}")
    sys.exit(1)

print()
print("Modules:")

capture = False

with open(yaml_file) as f:

    for line in f:

        if line.startswith("modules:"):
            capture = True
            continue

        if capture:

            if line.startswith("  - "):
                print(f"  {line[4:].strip()}")

            elif (
                line.strip()
                and not line.startswith(" ")
            ):
                break

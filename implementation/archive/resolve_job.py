#!/usr/bin/env python3

import csv
import sys

if len(sys.argv) != 2:
    print("Usage:")
    print("  resolve_job.py <JOB_NAME>")
    sys.exit(1)

job_name = sys.argv[1]

with open("final_confluence_inventory_normalized.csv") as f:

    reader = csv.DictReader(f)

    for row in reader:

        if row["job"] == job_name:

            print()
            print(f"Job:         {row['job']}")
            print(f"Task Class:  {row['task_class']}")
            print(f"Executable:  {row['executable']}")
            print(f"Profile:     {row['profile']}")
            print()
            print("Modules:")

            if row["modules"]:
                for mod in row["modules"].split(";"):
                    print(f"  - {mod}")

            sys.exit(0)

print(f"ERROR: job '{job_name}' not found")
sys.exit(1)

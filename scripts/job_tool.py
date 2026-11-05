#!/usr/bin/env python3

import sys
import subprocess

if len(sys.argv) < 3:
    print("""
Usage:

  job_tool.py explain JOB
  job_tool.py loads JOB

Examples:

  job_tool.py explain JGLOBAL_FCST
  job_tool.py loads JGLOBAL_FCST
""")
    sys.exit(1)

command = sys.argv[1]
job = sys.argv[2]

if command == "explain":
    subprocess.run(
        [
            "python",
            "scripts/explain_job.py",
            job
        ]
    )

elif command == "loads":
    subprocess.run(
        [
            "python",
            "scripts/generate_loads.py",
            job
        ]
    )

else:
    print("Unknown command")

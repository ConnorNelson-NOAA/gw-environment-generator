#!/usr/bin/env python3

import sys
import subprocess

if len(sys.argv) < 3:

    print("""
Usage:

  job_tool.py explain JOB
  job_tool.py loads JOB

  job_tool.py explain-exec EXECUTABLE
  job_tool.py loads-exec EXECUTABLE
""")

    sys.exit(1)

command = sys.argv[1]
target = sys.argv[2]

if command == "explain":

    subprocess.run([
        sys.executable,
        "implementation/explain_job.py",
        target
    ])

elif command == "loads":

    subprocess.run([
        sys.executable,
        "implementation/generate_loads.py",
        target
    ])

elif command == "explain-exec":

    subprocess.run([
        sys.executable,
        "implementation/explain_exec.py",
        target
    ])

elif command == "loads-exec":

    subprocess.run([
        sys.executable,
        "implementation/loads_exec.py",
        target
    ])

else:

    print("Unknown command")

#!/usr/bin/env python3

import csv
import sys

from module_utils import render_module

if len(sys.argv) != 2:
    print("Usage: loads_exec.py <EXECUTABLE>")
    sys.exit(1)

exe = sys.argv[1]

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

print("Executable not found")
sys.exit(1)

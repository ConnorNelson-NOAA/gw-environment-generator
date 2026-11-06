#!/usr/bin/env python3

import csv
import subprocess
import re

MACHINES = {
    "orion": "GDAS/orion.intel",
    "ursa": "GDAS/ursa.intel",
    "hercules": "GDAS/hercules.intel",
    "hera": "GDAS/hera.intel",
    "wcoss2": "GDAS/wcoss2.intel",
    "gaea": "GDAS/gaeac6.intel",
}

rows = []

for machine, gdas_module in MACHINES.items():

    try:
        output = subprocess.check_output(
            f"module show {gdas_module} 2>&1",
            shell=True,
            text=True,
        )

    except subprocess.CalledProcessError as e:
        output = e.output

    modulepaths = []
    compiler_stack = ""
    mpi_stack = ""
    python_stack = ""

    for line in output.splitlines():

        if "MODULEPATH" in line:

            matches = re.findall(r'"([^"]+)"', line)

            if len(matches) >= 2:
                modulepaths.append(matches[1])

        if 'load("stack-oneapi/' in line:

            m = re.search(r'load\("([^"]+)"\)', line)

            if m:
                compiler_stack = m.group(1)

        elif 'load("stack-' in line:

            m = re.search(r'load\("([^"]+)"\)', line)

            if m:

                mod = m.group(1)

                if (
                    "mpi" in mod.lower()
                    or "mpich" in mod.lower()
                ):
                    mpi_stack = mod

        elif 'load("stack-python/' in line:

            m = re.search(r'load\("([^"]+)"\)', line)

            if m:
                python_stack = m.group(1)

    rows.append(
        [
            machine,
            gdas_module,
            ";".join(modulepaths),
            compiler_stack,
            mpi_stack,
            python_stack,
        ]
    )

with open(
    "data/machine_profile_inventory.csv",
    "w",
    newline="",
) as f:

    writer = csv.writer(f)

    writer.writerow(
        [
            "machine",
            "gdas_module",
            "modulepaths",
            "compiler_stack",
            "mpi_stack",
            "python_stack",
        ]
    )

    writer.writerows(rows)

print("built data/machine_profile_inventory.csv")

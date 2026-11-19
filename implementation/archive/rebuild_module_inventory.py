import csv

available = {}

with open("architecture/data/gdas_orion_modules.txt") as f:
    for line in f:
        line = line.strip()

        if "/" not in line:
            continue

        name = line.split("/")[0]

        available[name] = line

#
# manually resolved providers
#

available["mpi"] = "stack-intel-oneapi-mpi/2021.13"
available["jpeg"] = "libjpeg/2.1.0"
available["png"] = "libpng/1.6.37"
available["jasper"] = "jasper/2.0.32"

rows = []

with open("canonical_executable_inventory.csv") as f:

    r = csv.DictReader(f)

    for row in r:

        mods = []

        for provider in row["modules"].split(";"):

            provider = provider.strip()

            if provider in available:
                mods.append(available[provider])

        rows.append([
            row["executable"],
            row["profile"],
            ";".join(sorted(set(mods)))
        ])

with open(
    "canonical_modulefile_inventory_v2.csv",
    "w",
    newline=""
) as out:

    w = csv.writer(out)

    w.writerow([
        "executable",
        "profile",
        "modulefiles"
    ])

    w.writerows(rows)

print("Done")

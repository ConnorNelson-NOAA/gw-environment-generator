import csv

rows = []

maxmods = 0

with open("final_confluence_inventory_normalized.csv") as f:
    r = csv.DictReader(f)

    for row in r:

        mods = []

        if row["modules"]:
            mods = row["modules"].split(";")

        maxmods = max(maxmods, len(mods))

        row["_mods"] = mods

        rows.append(row)

with open(
    "confluence_table_inventory.csv",
    "w",
    newline=""
) as out:

    fields = [
        "job",
        "task_class",
        "executable",
        "profile"
    ]

    for i in range(maxmods):
        fields.append(f"module_{i+1}")

    w = csv.writer(out)

    w.writerow(fields)

    for row in rows:

        outrow = [
            row["job"],
            row["task_class"],
            row["executable"],
            row["profile"]
        ]

        outrow.extend(row["_mods"])

        while len(outrow) < len(fields):
            outrow.append("")

        w.writerow(outrow)

print("Wrote confluence_table_inventory.csv")

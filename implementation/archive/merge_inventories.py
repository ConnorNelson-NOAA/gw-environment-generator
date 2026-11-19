import csv

rows = {}
#
# Inventory A
#
with open("confluence_inventory.csv") as f:
    r = csv.DictReader(f)

    for row in r:
        rows[row["job"]] = row

#
# Inventory B
#
with open("job_profile_inventory.csv") as f:
    r = csv.DictReader(f)

    for row in r:

        job = row["job"]

        if job not in rows:

            rows[job] = {
                "job": job,
                "task_class": row["stack"],
                "executable": row["executable"],
                "profile": row["stack"],
                "modules": row["modules"]
            }

        else:

            if not rows[job]["executable"]:
                rows[job]["executable"] = row["executable"]

            if not rows[job]["profile"]:
                rows[job]["profile"] = row["stack"]

            if not rows[job]["modules"]:
                rows[job]["modules"] = row["modules"]

with open(
    "final_confluence_inventory.csv",
    "w",
    newline=""
) as out:

    w = csv.writer(out)

    w.writerow([
        "job",
        "task_class",
        "executable",
        "profile",
        "modules"
    ])

    for job in sorted(rows):
        r = rows[job]

        w.writerow([
            r["job"],
            r["task_class"],
            r["executable"],
            r["profile"],
            r["modules"]
        ])

print("Rows:", len(rows))

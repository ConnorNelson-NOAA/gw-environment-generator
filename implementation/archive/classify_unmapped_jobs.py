import csv

orchestration = {
    "Archive",
    "Fetch",
    "GlobusHpss",
    "Stage"
}

with open("final_confluence_inventory.csv") as f:
    r = csv.DictReader(f)

    for row in r:

        if row["executable"]:
            continue

        task = row["task_class"]

        if task in orchestration:
            kind = "ORCHESTRATION"
        else:
            kind = "NEEDS_REVIEW"

        print(
            f"{kind},{row['job']},{task}"
        )

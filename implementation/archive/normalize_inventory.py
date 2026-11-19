import csv

ORCHESTRATION_TASKS = {
    "Archive",
    "Fetch",
    "GlobusHpss",
    "Stage"
}

ORCHESTRATION_JOBS = {
    "JGLOBAL_AERO_ANALYSIS_FINALIZE",
    "JGLOBAL_AERO_ANALYSIS_INITIALIZE",
    "JGLOBAL_ATMENS_ANALYSIS_FINALIZE",
    "JGLOBAL_ATMENS_ANALYSIS_INITIALIZE",
    "JGLOBAL_ATM_ANALYSIS_FINALIZE",
    "JGLOBAL_ATM_ANALYSIS_INITIALIZE",
    "JGLOBAL_MARINE_ANAL_FINAL",
    "JGLOBAL_MARINE_ANAL_INIT",
}

with open("final_confluence_inventory.csv") as f:
    rows = list(csv.DictReader(f))

with open(
    "final_confluence_inventory_normalized.csv",
    "w",
    newline=""
) as out:

    fields = [
        "job",
        "task_class",
        "executable",
        "profile",
        "modules"
    ]

    w = csv.DictWriter(out, fieldnames=fields)
    w.writeheader()

    for row in rows:

        if not row["executable"]:

            if (
                row["task_class"] in ORCHESTRATION_TASKS
                or row["job"] in ORCHESTRATION_JOBS
            ):
                row["executable"] = "N/A"
                row["profile"] = "ORCHESTRATION"

        w.writerow(row)

print("Wrote final_confluence_inventory_normalized.csv")

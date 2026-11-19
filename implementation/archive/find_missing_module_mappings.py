import csv

resolved = set()

with open("canonical_modulefile_inventory.csv") as f:
    r = csv.DictReader(f)

    for row in r:
        for mod in row["modulefiles"].split(";"):
            if mod:
                resolved.add(mod.split("/")[0])

providers = set()

with open("canonical_executable_inventory.csv") as f:
    r = csv.DictReader(f)

    for row in r:
        for mod in row["modules"].split(";"):
            if mod:
                providers.add(mod)

print("UNRESOLVED PROVIDERS")
print("--------------------")

for p in sorted(providers - resolved):
    print(p)

import csv

module_provided = {
    "atlas",
    "bufr",
    "eckit",
    "fckit",
    "hdf5",
    "jasper",
    "jpeg",
    "mpi",
    "netcdf-c",
    "netcdf-cxx4",
    "netcdf-fortran",
    "openblas",
    "parallelio",
    "png",
    "udunits"
}

embedded = {
    "crtm",
    "fv3jedi",
    "ioda",
    "oops",
    "saber",
    "soca",
    "ufo",
    "vader"
}

with open("canonical_executable_inventory.csv") as f:

    r = csv.DictReader(f)

    for row in r:

        mods = set(
            m.strip()
            for m in row["modules"].split(";")
            if m.strip()
        )

        unresolved = (
            mods
            - module_provided
            - embedded
        )

        if unresolved:

            print(
                row["executable"],
                sorted(unresolved)
            )

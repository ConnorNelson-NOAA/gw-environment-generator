# Executable-Driven Environment Generation

## Purpose

Prototype framework for deriving runtime environments directly from
Global Workflow jobs and executables instead of sourcing the full
load_modules.sh stack.

## Entry Points

### Explain a Job

Show:

- executable
- runtime providers
- resolved modulefiles
- embedded libraries

Example:

    python job_tool.py explain JGLOBAL_FCST

### Generate Module Loads

Generate a runtime environment for a job.

Example:

    python job_tool.py loads JGLOBAL_FCST

## Inventories

### final_confluence_inventory_normalized.csv

Job inventory.

Contains:

- job
- executable
- profile
- modules

### canonical_executable_inventory.csv

Executable runtime dependency inventory.

Contains:

- executable
- runtime providers

### canonical_modulefile_inventory_v2.csv

Resolved modulefile inventory.

Contains:

- executable
- modulefiles

### provider_module_resolution.csv

Tracks provider classification and modulefile resolution.

## Validation

Validated executables:

- gfs_model.x
- gdas.x

Validation method:

    ldd <executable> | grep "not found"

Result:

    No unresolved libraries after loading generated environments.

## Known Limitations

Some providers are embedded in GDAS/JEDI installations and are not
provided through standalone modulefiles:

- crtm
- fv3jedi
- ioda
- oops
- saber
- soca
- ufo
- vader

These are tracked as embedded libraries.

# Executable-Driven Environment Generation Results

Validated:

JGLOBAL_FCST
    -> gfs_model.x

Generated environment successfully resolves all runtime libraries.

Validation:
    ldd gfs_model.x | grep "not found"

Result:
    No unresolved libraries.

---

JGLOBAL_ATM_ANALYSIS_VARIATIONAL
    -> gdas.x

Generated environment successfully resolves all runtime libraries
when intel-oneapi-mkl/2024.2.1 is included.

Validation:
    ldd gdas.x | grep "not found"

Result:
    No unresolved libraries.

---

Conclusion

Executable-driven environment generation is feasible.

The generated environment can satisfy runtime requirements
without directly sourcing load_modules.sh.

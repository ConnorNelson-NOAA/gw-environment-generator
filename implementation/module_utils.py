MODULE_MAP = {
    "bufr": "${bufr_ver}",
    "crtm": "${crtm_ver}",
    "hdf5": "${hdf5_ver}",
    "netcdf-c": "${netcdf_c_ver}",
    "netcdf-fortran": "${netcdf_fortran_ver}",
    "intel-oneapi-mkl": "${intel_mkl_ver}",
}

def render_module(module):

    module = module.strip()

    if not module:
        return None

    if module in MODULE_MAP:
        return f"module load {module}/{MODULE_MAP[module]}"

    return f"module load {module}"

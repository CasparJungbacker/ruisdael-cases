import netCDF4 as nc
import numpy as np

PROF_NAMES = ["zt", "th_l", "q_t", "u", "v", "tke_init"]

if __name__ == "__main__":
    prof_inp = np.genfromtxt("prof.inp.001", skip_header=2)

    # We have no large-scale forcings, so we don't have to provide these variables
    # in out input file

    with nc.Dataset("init.001.nc", "w") as init_nc:
        init_nc.createDimension("zt", 128)
        
        for i, varname in enumerate(PROF_NAMES):
            var = init_nc.createVariable(varname, "f4", ("zt"))
            var[:] = prof_inp[:,i]

    with nc.Dataset("tracers.001.nc", "w") as tracers_nc:
        tracers_nc.createDimension("zt", 128)

        nox = tracers_nc.createVariable("nox", "f4", ("zt"), fill_value=0.0)
        nox.long_name = "nitrogen dioxide"
        nox.unit = "ppb"
        nox.molar_mass = 30.480
        nox.lemis = 1
        nox.ldep = 1
        nox[:] = 0.0

        co2 = tracers_nc.createVariable("co2", "f4", ("zt"), fill_value=0.0)
        co2.long_name = "carbon dioxide"
        co2.unit = "ppm"
        co2.molar_mass = 44.009
        co2.lemis = 1
        co2.lags = 1
        co2[:] = 0.0

        nh3 = tracers_nc.createVariable("nh3", "f4", ("zt"), fill_value=0.0)
        nh3.long_name = "ammonia"
        nh3.unit = "ppb"
        nh3.molar_mass = 17.031
        nh3.lemis = 1
        nh3.ldep = 1
        nh3[:] = 0.0

from RAPIDpy.inflow.lsm_rapid_process import run_lsm_rapid_process
from datetime import datetime
# from netCDF4 import Dataset
import numpy as np
import cProfile
#from glob import glob
#import pandas as pd
#import xarray as xr
from time import time

RAPID_EXE = '/Users/ricky/rapid'     # path to RAPID executable
RAPIDIO_DIR = '/Users/ricky/Documents/rapidio/rapid'           # path to folder with RAPID input/output directories
LSM_DATA_DIR = '/Users/ricky/Documents/rapidio/ncs'             # path to folder with LSM data

profiler = cProfile.Profile()
if __name__ == "__main__":

    run_lsm_rapid_process(
        rapid_executable_location=RAPID_EXE,
        rapid_io_files_location=RAPIDIO_DIR,
        # rapid_input_location='/Users/ricky/Documents/rapidio/rapid/input',
        # rapid_output_location='/Users/ricky/Documents/rapidio/rapid/output',
        lsm_data_location=LSM_DATA_DIR,
        simulation_start_datetime=datetime(1979, 1, 1),
        simulation_end_datetime=datetime(1984, 1, 1),
        generate_rapid_namelist_file=False,  # if you want to run RAPID manually later
        run_rapid_simulation=False,  # if you want to run RAPID after generating inflow file
        generate_return_periods_file=False,  # if you want to get return period file from RAPID simulation
        return_period_method='weibull',
        generate_seasonal_averages_file=False,
        generate_seasonal_initialization_file=False,  # if you want to get seasonal init file from RAPID simulation
        generate_initialization_file=False,  # if you want to generate qinit file from end of RAPID simulation
        use_all_processors=True
    )


    # output = "/Users/ricky/Documents/rapidio/rapid/output/m3_riv_bas_era5_t720_24hr_19790101to19840101.nc"
    # validation = "/Users/ricky/Documents/rapidio/m3_riv_bas_era5_t720_24hr_19790101to19840101.nc"

    # ods = xr.open_dataset(output)
    # vds = xr.open_dataset(validation)
    # print(ods)
    # print(vds)
    # o = ods['m3_riv'].values
    # o = o[~np.isnan(o)]
    # v = vds['m3_riv'].values
    # v = v[~np.isnan(v)]

    # print(o, len(o))
    # print(v, len(v))
    # ncs = glob("/Users/ricky/Documents/rapidio/ncs/19790*.nc")

    # def read_loop():
    #     df = pd.DataFrame(columns=['t'], index=range(len(ncs)))
    #     i = 0
    #     for nc_file in ncs: # 31271 function calls (31140 primitive calls) in 2.180 seconds
    #         # Read the netcdf dataset
    #         #data_in_nc = Dataset(nc_file)
    #         data_in_nc = xr.open_dataset(nc_file)
    #         inflow_data = data_in_nc.variables['ro'][:]
    #         # get runoff dims
    #         len_time_subset = 1
    #         data_in_nc.close()

    #         #df.loc[i, 'm3_riv'] = inflow_data[0][300]
    #     return df

    # def read_loop2(): # 3224793 function calls (3146754 primitive calls) in 1.566 seconds
    #     df = pd.DataFrame(columns=['t'], index=range(len(ncs)))
    #     i = 0
    #     data_in_nc = xr.open_mfdataset(ncs)

    #     inflow_data = data_in_nc.variables['ro'][:]
    #     # get runoff dims
    #     len_time_subset = 1
    #     data_in_nc.close()

    #         #df.loc[i, 'm3_riv'] = inflow_data[0][300]
    #     return df

    # #read_loop2()

    # profiler = cProfile.Profile()
    # profiler.enable()
    # read_loop()
    # profiler.disable()
    # profiler.print_stats()

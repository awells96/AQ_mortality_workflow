## Directory structure

The jupyter notebooks are set up so that you can configure your `WORK_ROOT`, `SCRATCH_ROOT` and `PLOTTING_ROOT` in `config.py` and data will be stored in the following structure.

Your `WORK_ROOT` is where you will host your final output data. The starred directories below are those can be moved to `SCRATCH_ROOT` if data storage is an issue. However you will need to adjust the corresponding scripts to use `SCRATCH_ROOT` rather than `WORK_ROOT` and adjust the `SCRATCH_ROOT` directory structure.

The `WORK_ROOT` structure is as follows:

    WORK_ROOT/
    ├── BMR/
    │   └── masks/
    │       ├── country/
    │       └── region/
    ├── GBD21/
    │   └── RR_curves/
    ├── GBD23/
    │   └── RR_curves/
    ├── SSP_pop/
    │   └── SSP2/
    ├── O3_obs/
    ├── PM2.5_obs/
    └── {model}/
        ├── ozone/
        │   ├── file_paths*/
        │   ├── MDA8*/
        │   ├── OSDMA8*/
        │   └── OSDMA8_BC/
        ├── pm25/
        │   ├── file_paths*/
        │   ├── monthly_pm25*/
        │   ├── annual_pm25*/
        │   └── annual_pm25_bc/
        ├── temp/
        │   ├── file_paths*/
        │   ├── temp_pres/
        └── mortality/
            ├── ozone/
            │   ├── gridpoint_mortality/
            │   ├── global/
            │   │   └── {n}_samples/
            │   └── region/
            │       └── {n}_samples/
            └── pm25/
                ├── gridpoint_mortality/
                ├── global/
                │   └── {n}_samples/
                └── region/
                   └── {n}_samples/

The `SCRATCH_ROOT` is used for large intermediate data. The structure is as follows:
    
    SCRATCH_ROOT/
    ├── BMR/
    ├── BMR_ozone/
    ├── beta_ozone/
    ├── rr_pm25/
    ├── TMREL/
    └── {model}/
        ├── mortality/
        ├── pm25/
        └── ozone/
            └── hourly_o3/

 The `PLOTTING_ROOT` is used to save figures from the plotting scripts.

    PLOTTING_ROOT/
    ├── example_workflow/
    ├── population/
    ├── bmr/
    ├── ozone/
    │   ├── MDA8/
    │   ├── OSDMA8/
    │   └── OSDMA8_BC/
    └── pm25/
        ├── Annual_PM25
        └── Annual_PM25_BC


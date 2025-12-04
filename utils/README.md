## utils.py description

`utils.py` contains common functions used in air_quality_project/ (see `README.md` for description of how to set up use of utils in jupyter notebooks). 

### Functions in `utils.py`

* `adjust_longitude` Change longitude values from 0-360 to -180-180 

* `lat_weighted_mean` Latitude weighting mean

* `land_filter` Removing ocean

* `autosize_figure` Figure sizing

* `fix_months` Monthly files don't always have the correct dates

* `bilinear_interp` Bilinear interpolation

* `create_global_country_map` Take list of country data and create global map

* `standardise_latlon` Standardise lat and lon coordinate names

* `load_file_list` A function to load json files

* `kgm3_to_µgm3` Conversion function from kg/m3 to µg/m3

* `kgkg_to_ppb` Conversion function from kg/kg to ppb

* `molmol_to_ppb` Conversion function from mol/mol to ppb

* `minus_one_month` Shift month coordinate, often used for CESM data

* `get_scenario_config` Return the configuration for a given model and scenario - *add new scenario details here, e.g.*

  ```python
    _MODEL_CONFIG = {
        "CESM2": {
            "ARISE": {
                "ensemble_members": list(range(1, 11)),
                "years": range(2035, 2069)
            },
            "SSP245_ARISE": {
                "ensemble_members": list(range(1, 11)),
                "years": range(2020, 2069)
            },
            "SSP245_G6": {
                "ensemble_members": [1, 2, 3],
                "years": range(2020, 2084)
            },
            "G6-1.5K": {
                "ensemble_members": [1, 2, 3],
                "years": range(2035, 2084)
            },
            "hist": {
                "ensemble_members": [1],
                "years": range(1990, 2009)
            }
        },
    
        "UKESM1": {
            "G6-1.5K": {
                "ensemble_members": [1, 2, 3],
                "years": range(2035, 2084)
            },
            "SSP245_G6": {
                "ensemble_members": [1, 2, 3],
                "years": range(2020, 2084)
            },
        }
    }
  ```

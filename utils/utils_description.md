## utils.py description

`utils.py` contains common functions used in air_quality_project/ (see `README.md` for description of how to set up use of utils in jupyter notebooks). 

### Functions in `utils.py`

* Change longitude values from 0-360 to -180-180 `adjust_longitude`

* Latitude weighting mean `lat_weighted_mean`

* Removing ocean `land_filter`

* Figure sizing `autosize_figure`

* Monthly files don't always have the correct dates `fix_months`

* Bilinear interpolation `bilinear_interp`

* Take list of country data and create global map `create_global_country_map`

* Return the configuration for a given model and scenario `get_scenario_config` - *add new scenario details here, e.g.*

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

* Standardise lat and lon coordinate names `standardise_latlon`

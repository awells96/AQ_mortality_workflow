# utils.py
# Common functions used in air_quality_project/
# descriptions in utils_description.md

# adjust_longitude
# lat_weighted_mean
# land_filter
# autosize_figure
# fix_months
# bilinear_interp
# create_global_country_map
# get_scenario_config
# standardise_latlon

import os
import xarray as xr
import numpy as np
import regionmask
import xesmf as xe


# === Change longitude values from 0-360 to -180-180 ===
def adjust_longitude(dataset: xr.Dataset) -> xr.Dataset:
    """
    Swaps longitude coordinates from range (0, 360) to (-180, 180)
    Args:
        dataset (xr.Dataset): xarray Dataset
    Returns:
        xr.Dataset: xarray Dataset with swapped longitude dimensions
    """
    lon_name = "lon"  # whatever name is in the data

    # Adjust lon values to make sure they are within (-180, 180)
    dataset["_longitude_adjusted"] = xr.where(
        dataset[lon_name] > 180, dataset[lon_name] - 360, dataset[lon_name])
    dataset = (
        dataset.swap_dims({lon_name: "_longitude_adjusted"})
        .sel(**{"_longitude_adjusted": sorted(dataset._longitude_adjusted)})
        .drop_vars(lon_name)
    )

    dataset = dataset.rename({"_longitude_adjusted": lon_name})
    return dataset


# === Latitude weighting mean ===
def lat_weighted_mean(da):
    weights = np.cos(np.deg2rad(da.lat))
    weights.name = "weights"
    new_da = da.weighted(weights).mean(("lon", "lat"))
    return new_da


# === Removing ocean ===
def land_filter(da):
    # Load in land fraction dataset
    land_110 = regionmask.defined_regions.natural_earth_v4_1_0.land_110
    da = da.where(land_110.mask_3D(da).squeeze())
    return da


# === Figure sizing - thanks to Ben Johnson, UK Met Office ===
def autosize_figure(nrows, ncolumns, scale_factor=1, xscale_factor=1, yscale_factor=1):
    xwidth = (ncolumns+0.67) * 5.0 * scale_factor * xscale_factor
    ylength = (nrows+0.67) * 3.6 * scale_factor * yscale_factor
    return (xwidth, ylength)


# === Monthly files don't always have the correct dates ===
def fix_months(da, expected_start, expected_end, scenario):
    """Fix time and crop"""
    expected_dates = xr.date_range(
        start=expected_start,
        end=expected_end,
        freq="MS",
        calendar="noleap",
        use_cftime=True
    )

    if len(da.time) != len(expected_dates):
        raise ValueError("Time dimension length mismatch with expected range.")

    da["time"] = expected_dates

    # Crop to desired range
    if scenario == "ARISE":
        start_date = "2035-01"
        end_date = "2069-12"
    elif scenario == "SSP245":
        start_date = "2020-01"
        end_date = "2069-12"
    elif scenario == "hist":
        start_date = "1990-01"
        end_date = "2009-12"
    else:
        raise ValueError(f"{scenario} is not known here")
    da = da.sel(time=slice(start_date, end_date))
    return da


# === Bilinear interpolation ===
def bilinear_interp(in_grid, target_grid):
    regridder = xe.Regridder(in_grid, target_grid, method="bilinear")
    return regridder


# === Take list of country data and create global map ===
def create_global_country_map(da):
    # Path config
    MASKS_DIR = "/glade/work/awells/air_quality/BMR/masks/country/"

    # Load in country mask
    mask_file = "GBD_Country_Masks_0.10.nc"
    mask_path = os.path.join(MASKS_DIR, mask_file)
    masks = xr.open_dataarray(mask_path)

    # Create DataArray filled with NaNs
    global_array = xr.DataArray(
        np.full((len(masks.lat), len(masks.lon)), np.nan),
        coords={"lat": masks.lat.values, "lon": masks.lon.values},
        dims=["lat", "lon"]
    )

    # Loop over countries, select the data for each country and apply to
    # empty array using the country mask
    for i in range(len(masks.country)):
        mask = masks.isel(country=i)
        country = masks.isel(country=i)["country"]
        mortality_country = da.sel(country=country)
        global_array = global_array.where(mask == 0, mortality_country)

    return global_array


# === Return the configuration for a given model and scenario ===
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
            "years": range(1990, 2010)
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
        "hist": {
            "ensemble_members": [1],
            "years": range(1990, 2010)
        }
    }
}


def get_scenario_config(model: str, scenario: str):
    """Return the configuration for a given model and scenario."""
    try:
        return _MODEL_CONFIG[model][scenario]
    except KeyError:
        available_models = list(_MODEL_CONFIG.keys())
        available_scenarios = (
            list(_MODEL_CONFIG[model].keys()) if model in _MODEL_CONFIG else []
        )
        raise ValueError(
            f"Config not found for model '{model}', scenario '{scenario}'.\n"
            f"Available models: {available_models}\n"
            f"Available scenarios for {model if model in _MODEL_CONFIG else 'N/A'}: {available_scenarios}"
        )


# === Standardise lat and lon coordinate names ===
def standardise_latlon(da):
    coord_map = {
        "lat": ["lat", "latitude", "Latitude", "LAT"],
        "lon": ["lon", "longitude", "Longitude", "LON"]
    }
    rename_dict = {}
    for std_name, aliases in coord_map.items():
        for alias in aliases:
            if alias in da.coords:
                rename_dict[alias] = std_name
    return da.rename(rename_dict)
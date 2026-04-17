# utils.py
# Common functions used in air_quality_project/
# descriptions in utils_description.md

# require_dir
# adjust_longitude
# lat_weighted_mean
# land_filter
# autosize_figure
# bilinear_interp
# create_global_country_map
# get_scenario_config
# standardise_latlon
# load_file_list
# kgm3_to_µgm3
# kgkg_to_ppb
# molmol_to_ppb
# minus_one_month

import json
import cftime
import xarray as xr
import numpy as np
import regionmask
import xesmf as xe
import pathlib


# === Raise an error directory import ===
def require_dir(path, name=None):
    """Raise a clear error if a required directory does not exist."""
    p = pathlib.Path(path)
    if not p.exists():
        label = name or str(p)
        raise FileNotFoundError(
            f"\n[Path Error] Required directory not found: {p}"
            f"\n  '{label}' must exist before running this script."
            f"\n  See the README for the expected directory structure."
        )
    return p


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


# === Bilinear interpolation ===
def bilinear_interp(in_grid, target_grid):
    regridder = xe.Regridder(in_grid, target_grid, method="bilinear")
    return regridder


# === Take list of country data and create global map ===
def create_global_country_map(da, masks_dir):
    # Load in country mask
    mask_file = "GBD_Country_Masks_0.10.nc"
    mask_path = pathlib.Path(masks_dir) / mask_file
    masks = xr.open_dataarray(mask_path)

    # Create DataArray filled with NaNs
    global_array = xr.DataArray(
        np.full((len(masks.lat), len(masks.lon)), np.nan),
        coords={"lat": masks.lat.values, "lon": masks.lon.values},
        dims=["lat", "lon"]
    )

    for i in range(len(masks.country)):
        mask = masks.isel(country=i)
        country = masks.isel(country=i)["country"]
        mortality_country = da.sel(country=country)
        global_array = global_array.where(mask == 0, mortality_country)

    return global_array


# === Return the configuration for a given model and scenario ===
_MODEL_CONFIG = {
    "CESM2": {
        "SSP245": {
            "ensemble_members": [1, 2, 3],
            "years": range(2020, 2084)
        },
        "hist": {
            "ensemble_members": [1],
            "years": range(1990, 2010)
        }
    },

    "UKESM1": {
        "SSP245": {
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


# === Function to load files ===
def load_file_list(DIR, filename):
    file_path = os.path.join(DIR, filename)
    with open(file_path, "r") as f:
        data = json.load(f)
    return data["files"]


# === Convert kg/m3 to µg/m3 ===
def kgm3_to_µgm3(data):
    # kg/m3 -> µg/m3 (multiply by 1e9)
    return data * 1e9


# === Convert kg/kg to ppb ===
def kgkg_to_ppb(data):
    # kg/kg -> ppb (multiply by 6.0345e8)
    return data * 6.0345e8


# === Convert mol/mol to ppb ===
def molmol_to_ppb(data):
    # mol/mol -> ppb (multiply by 1e9)
    return data * 1e9


# CESM2 naming convention shifts months by 1
# the data represents 2015-01 - 2020-12 but time coord shows 2015-02 - 2021-01
def minus_one_month(date):
    """Subtract one month from a cftime.DatetimeNoLeap object."""
    year, month = date.year, date.month
    if month == 1:
        return cftime.DatetimeNoLeap(year - 1, 12, date.day,
                                     date.hour, date.minute, date.second,
                                     date.microsecond, has_year_zero=date.has_year_zero)
    else:
        return cftime.DatetimeNoLeap(year, month - 1, date.day,
                                     date.hour, date.minute, date.second,
                                     date.microsecond, has_year_zero=date.has_year_zero)
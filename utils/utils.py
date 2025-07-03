# utils.py
# Common functions used in air_quality_project/

# adjust_longitude
# latitude_weighted_mean
# land_filter
# autosize_figure
# fix_months

import xarray as xr
import numpy as np
import regionmask


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


# === Figure sizing ===
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
    elif scenario == "SSP245":
        start_date = "2020-01"
    else:
        raise ValueError(f"{scenario} is not known here")
    da = da.sel(time=slice(start_date, "2069-12"))
    return da

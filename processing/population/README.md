# Population Data (POP)  

## Data inputs
From [Gao et al. (2020)](https://doi.org/10.7910/DVN/TLJ99B)
- `baseYr_total_2000.nc4`
- `ssp2_total_{year}.nc4`

## Processing  
- The population data used in this example are at a 1km resolution (0.0083° x 0.0083°) which is too high relative to the ozone and PM2.5 observations which are at 0.1° x 0.1° resolution
- Aggregating the population to a new grid (conserving the total population count) is performed using `1__Regrid_population.ipynb` 
  - From the GBD21 “Aggregation to each 0.1 × 0.1 grid cell was accomplished by summing the central 12 × 12 population cells.”
- It is useful to interpolate the population data from decadal to annual so that we can create a time series of mortality, exposure etc. which doesn’t feature decadal jumps due to changes in population size. This is applied in `2__Interpolate_population.ipynb` 

## Extra optional processing  
- The total population by country or region can be calculated with `3a__Save_country_level_population.ipynb` and `3b__Save_region_level_population.ipynb` 


### Expected file outputs  
`ssp2_coarse_grid_{year}.nc`  
`ssp2_coarse_grid_2000-2100.nc`  
`ssp2_coarse_grid_annual_2000-2100.nc`  
`ssp2_country_level_2000-2100.nc`  
`ssp2_region_level_2000-2100.nc`  

## Data citations  
Gao, Jing, 2020, "Global 1-km Downscaled Population Grids, SSP-Consistent Projections and Base Year, v1.01 (2000 - 2100)", https://doi.org/10.7910/DVN/TLJ99B, Harvard Dataverse, V1




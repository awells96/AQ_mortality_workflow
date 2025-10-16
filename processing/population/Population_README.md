# Population Data (POP)  

## Data citations  
Gao, J. (2017). Downscaling global spatial population projections from 1/8-degree to 1-km grid cells. NCAR Technical Note NCAR/TN-537+STR, National Center for Atmospheric Researcher, Boulder, CO., USA. DOI: 10.5065/D60Z721H  
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/TLJ99B

### Processing  
- Data is at 1km grid resolution which is too high relative to the ozone and PM2.5 observations which are at 0.1x0.1 degree resolution
- Aggregating the population to a new grid (conserving the total population count) is performed using `1__Regrid_population.ipynb` 
  - From the GBD21 “Aggregation to each 0.1 × 0.1 grid cell was accomplished by summing the central 12 × 12 population cells.”
- It is useful to interpolate the population data from decadal to annual so that we can create a time series of mortality, exposure etc. which doesn’t feature decadal jumps due to changes in population size. We apply this in `2__Interpolate_population.ipynb` 

### Extra optional processing  
- We can save the total population by country or region with `3__Save_country_level_population.ipynb` and `4__Save_region_level_population.ipynb` 


### Expected file outputs  
`ssp2_coarse_grid_{year}.nc`
`ssp2_coarse_grid_2000-2100.nc`
`ssp2_coarse_grid_annual_2000-2100.nc`
`ssp2_country_level_2000-2100.nc`
`ssp2_region_level_2000-2100.nc`


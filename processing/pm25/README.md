# PM<sub>2.5</sub> - Annual mean PM<sub>2.5</sub>

## Data inputs
- [Shaddick et al. (2018)](https://doi.org/10.1021/acs.est.8b02864) observations
- Monthly mass mixing ratios (mmr) for black carbon, sea salt, primary and secondary organic aerosols, dust and sulfate aerosol. 

To follow the example (CESM2-WACCM SSP2-4.5 ensemble 1) start at step 1 with:
- `{VAR}_mmr_CESM2_SSP245_01_2015-2100.nc`
- `{VAR}_mmr_CESM2_hist_01_2015-2100.nc`
- `T_CESM2_hist_01_1990-2010.nc`
- `T_CESM2_SSP245_01_2015-2100.nc`

## Pre-processing steps
- Convert obervations from R data to netcdf using `0a_Save_DIMAQ_PM2.5_data.ipynb`
- Write a .json file of file paths for data `0b__Write_file_paths_PM_components`
- Converting mmr (kg/kg) to a concentration (µg/m³) requires calculating air density from pressure and temperature. Process temperature on pressure levels `0c_Monthly_temperature`

## Processing
- Calculating the total PM<sub>2.5</sub> concentration from mass mixing ratios following the [Turnock et al. (2022)](https://doi.org/10.1029/2022EF002687) equation. 
    - Examples for CESM2 are given in `1__Monthly_PM2.5_calculation.ipynb`  
- Calculate the annual mean using `2__Save_annual_PM2.5.ipynb`
- Bias correct the climate model product using `3__Bias_correct_PM25.ipynb` with the observations and historical data. 
    - This step includes downscaling the climate model data to the same grid as the observations (0.1°x0.1° resoluution)

### Expected file outputs
`{PM_var}_mmr_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`Monthly_PM25_{model}_{scenario}_{ens_num:02d}_{dates-yyyy}.nc`  
`Annual_PM25_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`Annual_PM25_BC_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  


## Data Citations

### CESM2  
*SSP2-4.5*  
Mike Mills, Daniele Visioni, Jadwiga (Yaga) Richter. (2022). CESM2-WACCM6-SSP245. UCAR/NCAR - Climate and Global Dynamics Laboratory. https://doi.org/10.26024/0cs0-ev98. Accessed 20 May 2025.

*Historical CESM-WACCM*  
**find citation**


### UKESM1
*SSP2-4.5*  
**find citation**  

*Historical*  
**find citation**  
https://data.ceda.ac.uk/badc/cmip6/data/CMIP6/CMIP/MOHC/UKESM1-0-LL/historical/r1i1p1f2  

### Observations
Gavin Shaddick, Matthew L. Thomas, Heresh Amini, David Broday, Aaron Cohen, Joseph Frostad, Amelia Green, Sophie Gumy, Yang Liu, Randall V. Martin, Annette Pruss-Ustun, Daniel Simpson, Aaron van Donkelaar, and Michael Brauer Environmental Science & Technology 2018 52 (16), 9069-9078 DOI: 10.1021/acs.est.8b02864  
*Saved as an .Rdata file in appendix*  




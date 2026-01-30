# PM<sub>2.5</sub> - Annual mean PM<sub>2.5</sub>

## Data inputs
To run this portion of the example workflow, you will need to have available the following data:

- [Shaddick et al. (2018)](https://doi.org/10.1021/acs.est.8b02864) observations
- Monthly mass mixing ratios (mmr) for black carbon, sea salt, primary and secondary organic aerosols, dust and sulfate aerosol. 

To follow the example in the [paper](ADD DOI FOR PAPER) (CESM2-WACCM SSP2-4.5 ensemble 1) start at step 1 with the following data, which can be found [here](ADD DOI FOR ZENODO UPLOAD):
- `{VAR}_mmr_CESM2_SSP245_01_2015-2100.nc`
- `{VAR}_mmr_CESM2_hist_01_2015-2100.nc`
- `T_CESM2_hist_01_1990-2010.nc`
- `T_CESM2_SSP245_01_2015-2100.nc`

## Pre-processing steps
First, you will need to collate climate model data ready to calculate monthly PM<sub>2.5</sub> concentrations.

- Convert obervations from R data to netcdf using `0a_Save_DIMAQ_PM2.5_data.ipynb`
- Write .json files of file paths for each mass mixing ratio in the directory `0b__Write_file_paths_PM_components`
- Calculate the total mass mixing ratios for each component `Oc_Calculate_total_mmrs.ipynb`
    - For mass mixing ratios of small particles in CESM2, the variables are usually separated by mode - for example, the so4 variables are called so4_a1, so4_a2, so4_a3, so4_c1, so4_c2, and so4_c3, where 1-3 are accumulation, aitken, and coarse modes, respectively, and "a" variables are for dry particles and "c" are for in-cloud. Likewise, for BC, you can look for bc_a1, bc_a2, etc. This may not be the case for other climate model output, this script calculated the sum of all modes for each variable. 
- Converting mmr (kg/kg) to a concentration (µg/m³) requires calculating air density from pressure and temperature. Process temperature on pressure levels `0d_Monthly_temperature`


## Processing
Next, you will need to calculate the annual PM<sub>2.5</sub> concentration, downscale and bias correct the climate model data. 

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




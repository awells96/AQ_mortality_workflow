# PM<sub>2.5</sub> - Annual mean PM<sub>2.5</sub>

## Data Citations

### CESM2  
*SSP2-4.5*  
Mike Mills, Daniele Visioni, Jadwiga (Yaga) Richter. (2022). CESM2-WACCM6-SSP245. UCAR/NCAR - Climate and Global Dynamics Laboratory. https://doi.org/10.26024/0cs0-ev98. Accessed 20 May 2025.

*Historical CESM-WACCM*  
**find citation**

*ARISE-SAI-1.5K*  
Richter, J. H., Visioni, D., MacMartin, D. G., Bailey, D. A., Rosenbloom, N., Dobbins, B., Lee, W. R., Tye, M., and Lamarque, J.-F.: Assessing Responses and Impacts of Solar climate intervention on the Earth system with stratospheric aerosol injection (ARISE-SAI): protocol and initial results from the first simulations, Geosci. Model Dev., 15, 8221–8243, https://doi.org/10.5194/gmd-15-8221-2022, 2022. 

*G6-1.5K*  
**find citation - Walker?**

### UKESM1
*SSP2-4.5*  
**find citation**  

*Historical*  
**find citation**  
https://data.ceda.ac.uk/badc/cmip6/data/CMIP6/CMIP/MOHC/UKESM1-0-LL/historical/r1i1p1f2  

*ARISE-SAI-1.5K*  
**find citation - Matthew?**  

*G6-1.5K*  
**find citation - Walker?**  

### Observations
Gavin Shaddick, Matthew L. Thomas, Heresh Amini, David Broday, Aaron Cohen, Joseph Frostad, Amelia Green, Sophie Gumy, Yang Liu, Randall V. Martin, Annette Pruss-Ustun, Daniel Simpson, Aaron van Donkelaar, and Michael Brauer Environmental Science & Technology 2018 52 (16), 9069-9078 DOI: 10.1021/acs.est.8b02864  
*Saved as an .Rdata file in appendix*  

## Data inputs
- Monthly PM2.5 at all pressure levels
- Shaddick et al. (2018) observations

### Pre-processing steps
- Convert obervations from R data to netcdf using `1pp_Save_DIMAQ_PM2.5_data.ipynb`
- Converting climate model output to surface measurements in µg/m<sup>3</sup>
    - Potentially calculating the total PM<sub>2.5</sub> from mass mixing ratios **add more here when this has been done with UKESM**
- Examples for CESM2 and UKESM1 are given in `1pp_CESM2_monthly_pm25.ipynb` and `1pp_UKESM1_monthly_pm25.ipynb`

### Processing
- Calculate the annual mean using `2__Save_annual_PM2.5.ipynb`
- Bias correct the climate model product using `3__Bias_correct_PM25.ipynb` with the observations and historical data. 
    - This step includes downscaling the climate model data to the same grid as the observations (0.1x0.1 deg)

### Expected file outputs
`Annual_PM25_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`Annual_PM25_BC_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  



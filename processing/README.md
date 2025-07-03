**Data processing**

**Baseline Mortality Rate (BMR)**

<ins>Data citations</ins>  
Global Burden of Disease Collaborative Network.  
Global Burden of Disease Study 2021 (GBD 2021\) Results.  
Seattle, United States: Institute for Health Metrics and Evaluation (IHME), 2022\.  
Available from [https://vizhub.healthdata.org/gbd-results/](https://vizhub.healthdata.org/gbd-results/).

<ins>Search terms</ins>  
GBD Estimate: Cause of death or injury  
Measure: Deaths  
Metric: Number, Percent, Rate (***use rate to calculate BMR \- rate is given as x per 100K***)  
Cause: Chronic obstructive pulmonary disease  
Location: *Select all countries and territories*  
Age: All ages  
Sex: Both  
Year: 1990-2009

<ins>Country masks</ins>   
Available through the zenodo link associated with McDuffie et al. (2021).   
McDuffie, E. E., Martin, R. V., Spadaro, J. V., Burnett, R., Smith, S. J., O'Rourke, P., Hammer, M., van Donkelaar, A., Bindle, L., Shah, V., Jaegle, L., Luo, G., Yu, F., Adeniran, J., Lin, J., Brauer, M. Source Sector and Fuel Contributions to Ambient PM2.5 Attributable Mortality Across Multiple Spatial Scales, Nature Communications, 12, 3594 (2021). [https://doi.org/10.1038/s41467-021-23853-y](https://doi.org/10.1038/s41467-021-23853-y)  
McDuffie, E., Brauer, M., Martin, R., Spadaro, J., Burnett, R., Hammer, M., & van Donkelaar, A. (2021). GBD-MAPS-Global: Analysis Input Dataset \[Data set\]. Zenodo. [https://doi.org/10.5281/zenodo.4642700](https://doi.org/10.5281/zenodo.4642700)  
Country and Region masks are derived from country shapefiles from the GBD, as well as the GBD country and region classifications

<ins>Processing</ins>

- GBD download saves as a csv file.  
- Process to calculate the BMR for the years 1990-2009 for each country (lower, mean, upper) using `1__GBD_BMR_to_netcdf.ipynb`  
  - The average BMR across 1990-2009 is calculated and applied to all future mortality estimates.  
- Country masks are saved as a `.mat` file. Use `2__GBD_country_masks.ipynb` to convert to xarray (.nc).  
- Country labels do not match between country masks dataset and BMR dataset. Use `3__Relabel_country_mask.ipynb` to correct the mismatching labels.  
- Apply country level BMR to global lat/lon grid using `4__Create_BMR_country_mask.ipynb`

*Extra processing steps*

- GBD also provides region masks at 0.1x0.1 degree resolution. A similar method to the above is used to process these. `2a__GBD_region_masks.ipynb` converts from .mat file to netcdf. 

*Expected file outputs*  
`GBD_BMR_Country_COPD_1990-2009.nc`  
`GBD_Country_Masks_0.10.nc`  
`GBD_Region_Masks_0.10.nc`  
`GBD_Country_Masks_0.10_newlabels.nc`  
`GBD_BMR_Country_Mask_COPD_1990-2009.nc`

**Population Data (POP)**

<ins>Data citations</ins>  
Gao, J. (2017). Downscaling global spatial population projections from 1/8-degree to 1-km grid cells. NCAR Technical Note NCAR/TN-537+STR, National Center for Atmospheric Researcher, Boulder, CO., USA. [DOI: 10.5065/D60Z721H](https://doi.org/10.5065/D60Z721H)  
[https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/TLJ99B](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/TLJ99B)

<ins>Processing</ins>

- Data is at 1km grid resolution which is too high relative to the ozone observations which are at 0.1x0.1 degree resolution  
- Aggregating the population to a new grid (conserving the total population count) is performed using `1__Regrid_population.ipynb`   
- From the GBD21 “Aggregation to each 0.1 × 0.1 grid cell was accomplished by summing the central 12 × 12 population cells.”  
- It is useful to interpolate the population data so that we can create a time series of mortality, exposure etc. which doesn’t feature decadal jumps due to changes in population size. We apply this in `2__Interpolate_population.ipynb` 

*Expected file outputs*  
`ssp2_coarse_grid_{year}.nc`

`ssp2_coarse_grid_2000-2100.nc`

`ssp2_coarse_grid_annual_2000-2100.nc`

**Ozone data (X)**

<ins>Data citations</ins>  
*ARISE-SAI-1.5K*  
Richter, J. H., Visioni, D., MacMartin, D. G., Bailey, D. A., Rosenbloom, N., Dobbins, B., Lee, W. R., Tye, M., and Lamarque, J.-F.: Assessing Responses and Impacts of Solar climate intervention on the Earth system with stratospheric aerosol injection (ARISE-SAI): protocol and initial results from the first simulations, Geosci. Model Dev., 15, 8221–8243, [https://doi.org/10.5194/gmd-15-8221-2022](https://doi.org/10.5194/gmd-15-8221-2022), 2022\. 

*SSP2-4.5*  
Mike Mills, Daniele Visioni, Jadwiga (Yaga) Richter. (2022). CESM2-WACCM6-SSP245. UCAR/NCAR \- Climate and Global Dynamics Laboratory. [https://doi.org/10.26024/0cs0-ev98](https://doi.org/10.26024/0cs0-ev98). Accessed 20 May 2025\.

*Historical CESM-WACCM*  
\*email from Simone Tilmes pointing me to data\*   
\*\*find citation\*\*

*Observations*  
Marissa N. DeLang, Jacob S. Becker, Kai-Lan Chang, Marc L. Serre, Owen R. Cooper, Martin G. Schultz, Sabine Schröder, Xiao Lu, Lin Zhang, Makoto Deushi, Beatrice Josse, Christoph A. Keller, Jean-François Lamarque, Meiyun Lin, Junhua Liu, Virginie Marécal, Sarah A. Strode, Kengo Sudo, Simone Tilmes, Li Zhang, Stephanie E. Cleland, Elyssa L. Collins, Michael Brauer, and J. Jason West: Mapping Yearly Fine Resolution Global Surface Ozone through the Bayesian Maximum Entropy Data Fusion of Observations and Model Output for 1990–2017  
Environmental Science & Technology 2021 55 (8), 4389-4398. DOI: 10.1021/acs.est.0c07742

<ins>Processing</ins>

- Climate model (CESM2) output  (ARISE-SAI-1.5K, SSP2-4.5 and historical runs) provides hourly surface ozone. Step 1 is to calculate the daily 8-hr maximum using `1__Save_MDA8_O3.ipynb` (MDA8: 8hr Daily Maximum Calculates the 8-hour daily maximum surface ozone concentration)   
- Step 2 is to calculate the OSDMA8: Highest seasonal (6-month) average of 8-hour daily maximum ozone concentrations across 15 months (Jan-Mar) using `2__Save_OSDMA8.ipynb`  
- Step 3 is to bias correct the climate model product using `3__Bias_correct_OSDMA8.ipynb` with the observations and historical data.   
  - This step includes downscaling the climate model data to the same grid as the observations (0.1x0.1 deg)

*Extra processing steps*

- To explore the global mean OSDMA8 over time, we calculate the global mean using `4__Save_global_mean_OSDMA8.ipynb`  
- To explore the country level changes in OSDMA8 over time, we calculate the country level averages using `5__Save_country_OSDMA8.ipynb`  
- To explore the regional changes in OSDMA8 over time, we calculate the regional averages using `6__Save_regional_OSDMA8.ipynb`

*Expected file outputs*

`MDA8_CESM2_{scenario}_{ens_num}_{dates-yyyymmdd}.nc`

`OSDMA8_CESM2_{scenario}_{ens_num}_{dates-yyyy}.nc`

`OSDMA8_BC_CESM2_{scenario}_{ens_num}_{dates-yyyy}.nc`

`OSDMA8_BC_globalmean_CESM2_{scenario}_{ens_num}_{dates-yyyy}.nc`

`OSDMA8_BC_Country_mean_CESM2_{scenario}_{ens_num}_{dates-yyyy}.nc`

`OSDMA8_BC_Regional_mean_CESM2_{scenario}_{ens_num}_{dates-yyyy}.nc`

**Mortality** 

M(x,y) \= AF(x,y) *  BMR *  POP(x,y)

AF(x,y) \= \frac{RR(x,y) - 1}{RR(x,y)}

RR(x,y) \= e^{(X-TMREL)}

<ins>Notes</ins>  
When calculating mortality there are a few caveats that need to be addressed:

- The BMR is calculated as an average from 1990-2009 and used for the future projections. Whilst this could over or underestimate total mortality due to changes in demographics or health care in the future, it could reduce uncertainty in the projections of BMR.   
- The relative risk (RR) was taken from GBD (2021), for an increase of 10 ppb RR=1.074 \[95% CI 1.014 – 1.137\]. This is applie for all ages and all countries. 

<ins>Processing</ins>

- To calculate the total mortality (per grid point) for each ensemble member we calculate the attributable fraction (AF) and then multiply by the BMR and the population (POP) using `1__Calculate_mortality.ipynb`  
- For plotting mortality changes, it is useful to calculate the total mortality by country or region. We calculate the total mortality per country using `2__Country_level_mortality.ipynb`  
- We calculate the total mortality per region using `3__Region_level_mortality.ipynb`  
- To calculate the global sum of mortality we use `4__Global_mortality.ipynb`

*Extra processing steps*

- In order to test the method of calculating mortality, we have applied the workflow to the year 2000 using observations of OSDMA8 (since bias correcting the model data during the years 1990-2009 would have yielded the same results). We calculate global mortality and plot the total mortality per country to match those seen in the supplementary information of Akritidis et al. (2024). `5__Caclulate_mortality_2000.ipynb`

*Expected file outputs*

`Mortality_CESM2_{scenario}_{ens_num}_{dates-yyyy}.nc`

`Mortality_Country_sum_CESM2_{scenario}_{dates-yyyy}.nc`

`Mortality_Regional_sum_CESM2_{scenario}_{dates-yyyy}.nc`

`Mortality_global_sum_CESM2_{scenario}_{dates-yyyy}.nc`


# Baseline Mortality Rate (BMR)

## Data inputs

To run this portion of the example workflow, you will need to have available the following data: 

From [Duffey et al. (2021)](https://doi.org/10.5281/zenodo.4642700)
- `GBD_Country_Masks_0.10.mat`
- `GBD_Region_Masks_0.10.mat`

From [VizHub data search](#search-terms)
- `IHME-GBD_2021_DATA-{mortality_outcome}.csv`

To follow the example in the [paper](https://doi.org/10.22541/essoar.177170388.88002537/v1) data can be found [here](https://doi.org/10.5281/zenodo.18436835)

## Pre-processing steps

First, you will need to convert country and region masks into a different file format, so they can be integrated with other data. 

- Country and region masks (0.1°x0.1° resolution) from [Duffey et al. (2021)](https://doi.org/10.5281/zenodo.4642700) can be converted from .mat to .nc using `0a__GBD_country_masks.ipynb` and `0b__GBD_region_masks.ipynb`   

## Processing

Next, you will need to download data on baseline mortality rates and prepare them to integrate with other country-level data in the pipeline. 

- [GBD Results VizHub](https://vizhub.healthdata.org/gbd-results/) download saves as a csv file - see [Search terms](#search-terms) for more information regarding the data download used in this example.  
- Calculate the BMR for the years 1990-2009 for each country (lower, mean, upper) and each health variable using `1__GBD_BMR_to_netcdf.ipynb`  
  - The average mortality rate across 1990-2009 is calculated and applied to all future mortality estimates.  
  - Runs for all given health variables  
- Country labels do not always match between datasets. Use `2__Relabel_countries.ipynb` to correct the mismatching labels and apply to BMR dataset(s).  

### Expected file outputs
`GBD_Country_Masks_0.10.nc`  
`GBD_Region_Masks_0.10.nc`  
`GBD_BMR_Country_{health_var}_1990-2009.nc`  
`GBD_BMR_Country_{health_var}_newlabels_1990-2009.nc`  

## Data citations

### Mortality rates
Global Burden of Disease Collaborative Network.  
Global Burden of Disease Study 2021 (GBD 2021) Results.  
Seattle, United States: Institute for Health Metrics and Evaluation (IHME), 2022.  
Available from https://vizhub.healthdata.org/gbd-results/.  

### Country masks 
Available through the zenodo link associated with McDuffie et al. (2021).  
  
McDuffie, E. E., Martin, R. V., Spadaro, J. V., Burnett, R., Smith, S. J., O'Rourke, P., Hammer, M., van Donkelaar, A., Bindle, L., Shah, V., Jaegle, L., Luo, G., Yu, F., Adeniran, J., Lin, J., Brauer, M. Source Sector and Fuel Contributions to Ambient PM2.5 Attributable Mortality Across Multiple Spatial Scales, Nature Communications, 12, 3594 (2021). https://doi.org/10.1038/s41467-021-23853-y
  
McDuffie, E., Brauer, M., Martin, R., Spadaro, J., Burnett, R., Hammer, M., & van Donkelaar, A. (2021). GBD-MAPS-Global: Analysis Input Dataset [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4642700  
  
“Country and Region masks are derived from country shapefiles from the GBD, as well as the GBD country and region classifications”  

## Search terms
The following search terms were used for the example provided here.  

GBD Estimate: Cause of death or injury  
Measure: Deaths  
Metric: Number, Percent, Rate (use rate to calculate BMR - rate is given as x per 100K)  
Cause(s):  
- Chronic obstructive pulmonary disease  
- Lower Respiratory Infection  
- Type II Diabetes  
- Ischemic Heart Disease  
- Stroke  
- Tracheal, bronchus, and lung cancer  
  
Location: Select all countries and territories  
Age: All ages  
Sex: Both  
Year: 1990-2009  




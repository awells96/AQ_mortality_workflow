# Mortality due to PM<sub>2.5</sub>

## Data inputs
To run this portion of the example workflow, you will need to have available the following data:

Relative Risk curves from the [Global Burden of Disease](https://ghdx.healthdata.org/record/ihme-data/gbd-2023-air-pollution-exposure-estimates-1990-2023)
- `IHME_GBD_2023_AIR_POLLUTION_{date_range}_PM_{mortality_outcome}_MEAN_Y{year}M{month}D{day}.CSV`  

[Population](/processing/population) estimates on a 0.1° × 0.1° resolution  

[Baseline Mortality Rate](/processing/bmr)
    - These are given at a country level and can be mapped to the same 0.1° × 0.1° resolution  

[Annual PM<sub>2.5</sub>](/processing/pm25) projections

To follow the example in the [paper](https://doi.org/10.22541/essoar.177170388.88002537/v1) data can be found [here](https://doi.org/10.5281/zenodo.18436835)  
- When the example has been updated using the GBD 2023, these links will be updated, along with the paper.

## Pre-processing steps
- The RR curves from the GBD 2023 (and previous GBD versions) can be converted from csv files to netCDFs using `0__Save_RR_curves_GBD.ipynb`.

## Processing
Three of the components to the mortality calculations include a range of uncertainty, *BMR*, *RR* and *TMREL*. Therefore there are two parts to this processing:

1. Calculating mortality using central estimates
    - Calulating mortality on a gridpoint scale using `1a__Calculate_mortality.ipynb`.
    - Sum these gridpoint estimates to a country level scale using `1b__Country_level_mortality.ipynb`.
    - The country level script can be easily adjusted to calculate regional level mortality using central estimates.

2. Calculating mortality and including uncertainty with parametric bootstrapping
    - First calculate the samples for *BMR*, *RR* and *TMREL* using `2__Save_sample_size.ipynb`.
    - Calculate the global sum mortality for each outcome using parametric bootstrapping with `3a__Global_mortality_samples.ipynb`.
    - Merge yearly global and outcome data files using `3b__Merge_global_mortality.ipynb`.
        - The total mortality is the sum of the six mortality outcomes
    - Calculate regional mortality using parametric bootstrapping with `4a__Regional_mortality_samples.ipynb`.
    - Merge yearly, regional and outcome data files using `4b__Merge_regional_mortality.ipynb`.

### Expected file outputs
`Mortality_{GBD_version}_{outcome}_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`Mortality_{GBD_version}_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`Mortality_Country_sum_{GBD_version}_{model}_{scenario}_{dates-yyyy}.nc`  
`Global_mortality_{GBD_version}_{outcome}_{n_samples}_{model}_{scenario}_{ens_num}_{yyyy}.nc` 
`Global_mortality_{GBD_version}_{outcome}_{n_samples}_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`Global_mortality_{GBD_version}_{n_samples}_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`Regional_mortality_{GBD_version}_{outcome}_{n_samples}_{model}_{scenario}_{ens_num}_{region}_{yyyy}.nc`  
`Regional_mortality_{GBD_version}_{outcome}_{n_samples}_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`Regional_mortality_{GBD_version}_{n_samples}_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  

## Mortality equations

The following equations have been used to calculate mortality *(M)* due to ambient PM<sub>2.5</sub>:  

```math
M(x, y) = POP(x, y) \; \times \; BMR_c \; \times \; AF(x, y)  
```
<br>

where *POP(x, y)* is the population at point (x, y), *BMR<sub>c</sub>* is the [Baseline Mortality Rate](/processing/bmr) for each country and *AF(x, y)* is the Attributable Fraction at point (x, y). 

```math
AF(x, y) = \frac{1 - RR(x, y)}{RR(x, y)}  
```
<br>

where *RR(x,y)* is the Relative Risk at point (x, y) provided by the [Global Burden of Disease (2023)](https://ghdx.healthdata.org/record/ihme-data/gbd-2023-air-pollution-exposure-estimates-1990-2023).

## Global Burden of Disease (GBD)
The GBD provide relative risk estimates for a range of risk factors, including PM<sub>2.5</sub>.  

There are six included outcomes for particulate matter pollution. The GBD estimate the particulate-matter-attributable burden of disease based on the relation of long-term exposure to PM2.5 with ischaemic heart disease, stroke (ischaemic and haemorrhagic), COPD, lung cancer, acute lower respiratory infection, and type 2 diabetes. 
The GBD perform a literature review of studies and use the meta-regression—Bayesian, regularised, trimmed (MR-BRT) meta-regression tool to conduct a meta-analysis on those studies. The RR data from the GBD can be found through the [Global Burden of Disease](https://ghdx.healthdata.org/record/ihme-data/gbd-2023-air-pollution-exposure-estimates-1990-2023).

The TMREL is based on outdoor air pollution cohort studies exposure distributions conducted in North America. It is a uniform distribution around the minimum and 5th percentile values observed in the cohort, ~U(2.4, 5.9), in µg/m3. Relative risk curves are scaled using the TMREL.






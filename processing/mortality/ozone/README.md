# COPD Mortality due to surface ozone

## Data inputs
To run this portion of the example workflow, you will need to have available the following data:

- [Population](/processing/population) estimates on a 0.1° × 0.1° resolution
- [Baseline Mortality Rate](/processing/bmr)
    - These are given at a country level and can be mapped to the same 0.1° × 0.1° resolution
- [OSDMA8 projections](/processing/ozone)

To follow the example in the [paper](https://doi.org/10.22541/essoar.177170388.88002537/v1) data can be found [here](https://doi.org/10.5281/zenodo.18436835)  
- When the example has been updated using the GBD 2023, these links will be updated, along with the paper.

## Pre-processing steps
- `Test_sample_size.ipynb` provides some code to test the number of samples needed for the parametric bootstrapping. 1000 samples would be optimal but would require a lot of compute time due to the high resolution nature of the data. This script compares smaller sample sizes with 1000 samples to identify the best fit. It calculates the global mortality using n samples for one year and produces figures to help determine the best sample size. 

## Processing
Three of the components to the mortality calculations include a range of uncertainty, *BMR*, $\beta$ and *TMREL*. Therefore there are two parts to this processing:

1. Calculating mortality using central estimates only
    - Calulating mortality on a gridpoint scale using `1a__Calculate_mortality.ipynb`.
    - Sum these gridpoint estimates to a country level scale using `1b__Country_level_mortality.ipynb`.
    - The country level script can be easily adjusted to calculate regional level mortality using central estimates.

2. Calculating mortality including uncertainty using parametric bootstrapping
    - First calculate the samples for *BMR*, $\beta$ and *TMREL* using `2__Save_sample_size.ipynb`.
        - Selecting the number of samples is a balance between computational cost, given the high spatial resolution and associated memory requirements, and the need for a sufficiently large sample size to robustly span the uncertainty space.  
    - Calculate the global sum mortality using parametric bootstrapping with `3a__Global_mortality_samples.ipynb`.
    - Merge yearly global data files using `3b__Merge_global_mortality.ipynb`.
    - Calculate regional mortality using parametric bootstrapping with `4a__Regional_mortality_samples.ipynb`.
    - Merge yearly and regional data files using `4b__Merge_regional_mortality.ipynb`.

### Expected file outputs
`Mortality_{GBD_version}_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`Mortality_Country_sum_{GBD_version}_{model}_{scenario}_{dates-yyyy}.nc`  
`Global_mortality_{GBD_version}_{n_samples}_{model}_{scenario}_{ens_num}_{yyyy}.nc` 
`Global_mortality_{GBD_version}_{n_samples}_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`Regional_mortality_{GBD_version}_{n_samples}_{model}_{scenario}_{ens_num}_{region}_{yyyy}.nc`  
`Regional_mortality_{GBD_version}_{n_samples}_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  

## Mortality equations

The following equations have been used to calculate mortality *(M)* due to surface ozone:  

```math
M(x, y) = POP(x, y) \; \times \; BMR_c \; \times \; AF(x, y)  
```
<br>

where *POP(x, y)* is the population at point (x, y), *BMR<sub>c</sub>* is the [Baseline Mortality Rate](/processing/bmr) for each country and *AF(x, y)* is the Attributable Fraction at point (x, y). 

```math
AF(x, y) = \frac{1 - RR(x, y)}{RR(x, y)}  
```
<br>

where *RR(x,y)* is the Relative Risk at point (x, y) calculated by:

```math
RR(x, y) = e^{\beta \, (OSDMA8(x, y) - TMREL)}  
```
<br>

where *[OSDMA8(x, y)](/processing/ozone)* is the Highest seasonal (6-month) average of 8-hour daily maximum ozone concentrations across 15 months (Jan-Mar) at point (x, y) and *TMREL* is the Theoretical Minimum Risk Exposure Level provided by the [Global Burden of Disease (2023)](https://ghdx.healthdata.org/record/ihme-data/gbd-2023-air-pollution-exposure-estimates-1990-2023). $\beta$ is calculated using the relationship provided by the GBD.

## Global Burden of Disease (GBD)
The GBD provide relative risk estimates for a range of risk factors, including surface ozone and PM<sub>2.5</sub>.  

COPD is the only included outcome for ambient ozone pollution. The GBD perform a literature review of studies examining long-term ozone exposure and COPD and use the meta-regression—Bayesian, regularised, trimmed (MR-BRT) meta-regression tool to conduct a meta-analysis on those studies. The inverse-standard error weighted meta-analysis provided an estimated relative risk of 1.074 (95% CI 1.014–1.137) per 10 ppb. This is used to calculate $\beta$. 
  
The TMREL is based on the exposure distribution from the ACS CPS-II study ([Turner et al., 2016](https://doi.org/10.1164/rccm.201508-1633oc)). It is a uniform distribution around the minimum and 5th percentile values observed in the cohort, ~U(29.1, 35.7), in ppb.  

# Ozone - OSDMA8: Highest seasonal (6-month) average of 8-hour daily maximum ozone concentrations across 15 months (Jan-Mar)

## Data inputs  
- Hourly or 3hrly surface ozone
- DeLang et al. (2021) observations

## Pre-processing steps
- Write .json file with list of file paths `0a__Write_file_paths.ipynb`
- Converting climate model output to hourly surface ozone measurements in ppb.
    - Examples for CESM2 and UKESM1 are given in `0b__CESM2_hourly_o3.ipynb` and `0b__UKESM1_hourly_o3.ipynb`

## Processing
- Calculate a monthly mean of the daily 8-hr maximum using `1__Save_MDA8_O3.ipynb` (MDA8: 8hr Daily Maximum)
- Calculate the OSDMA8: Highest seasonal (6-month) average of 8-hour daily maximum ozone concentrations across 15 months (Jan-Mar) using `2__Save_OSDMA8.ipynb`
- Bias correct the climate model product using `3__Bias_correct_OSDMA8.ipynb` using the observations and historical data. 
    - This step includes downscaling the climate model data to the same grid as the observations (0.1x0.1 deg)

### Expected file outputs
`MDA8_{model}_{scenario}_{ens_num}_{dates-yyyymm}.nc`  
`OSDMA8_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  
`OSDMA8_BC_{model}_{scenario}_{ens_num}_{dates-yyyy}.nc`  

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
Marissa N. DeLang, Jacob S. Becker, Kai-Lan Chang, Marc L. Serre, Owen R. Cooper, Martin G. Schultz, Sabine Schröder, Xiao Lu, Lin Zhang, Makoto Deushi, Beatrice Josse, Christoph A. Keller, Jean-François Lamarque, Meiyun Lin, Junhua Liu, Virginie Marécal, Sarah A. Strode, Kengo Sudo, Simone Tilmes, Li Zhang, Stephanie E. Cleland, Elyssa L. Collins, Michael Brauer, and J. Jason West: Mapping Yearly Fine Resolution Global Surface Ozone through the Bayesian Maximum Entropy Data Fusion of Observations and Model Output for 1990–2017
Environmental Science & Technology 2021 55 (8), 4389-4398. DOI: 10.1021/acs.est.0c07742  
*Note: All observations and model output are converted to OSDMA8 using the same algorithm, and estimates are reported here as OSDMA8.*  








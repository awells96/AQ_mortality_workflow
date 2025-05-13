# Description of each file and pre-requisites 

## Ozone

```Save_MDA8_O3.ipynb```  
MDA8: 8hr Daily Maximum
Calculates the 8-hour daily maximum surface ozone concentration
- Takes hourly O3 data, calculates the daily rolling 8-hour mean and finds the maxmimum
- Returns daily output

```Save_OSDMA8.ipynb```  
OSDMA8: Highest seasonal (6-month) average of 8-hour daily maximum ozone concentrations across 15 months (Jan-Mar)
- Takes daily output from ```Save_MDA8_O3```, calculates rolling 6 monthly mean and finds the maximum
- Returns yearly output

```Bias_correct_OSDMA8.ipynb```  
Bias corrected version of OSDMA8
- Takes yearly output from ```Save_OSDMA8``` and uses observations of O3 to bias correct model data. Regrids model data to 0.1x0.1deg grid
- Returns 20 year averages in 5 year intervals

```Save_monthly_O3.ipynb```  
Processes monthly ozone data, corrects incorrect month labels and crops to interested years
- Takes monthly data
- Returns monthly output

## NO2

```Save_MDA8_NO2.ipynb```  
Calculates the surface NO2 concentration during the same 8-hour period as the 8-hour daily maximum surface ozone concentration
- Takes hourly O3 and NO2 data
- Returns daily output

```Save_NO2_6m.ipynb```  
Calculates the surface NO2 concentration during the same period as OSDMA8
- Takes daily output from ```Save_MDA8_O3``` and ```Save_MDA8_NO2```
- Returns yearly output

## PM2.5

```Save_annual_PM25.ipynb```  
Processes monthly PM2.5 data, corrects incorrect month labels and calculated annual average
- Takes monthly data and calculates annual mean
- Returns yearly output

## Precipitation

```Save_monthly_PRECT.ipynb```  
Processes monthly precipitation data, corrects incorrect month labels and crops to interested years
- Takes monthly data
- Returns monthly output

```Save_PRECT_6m.ipynb```  
Calculates the precipitation during the same months as OSDMA8
- Takes monthly output from ```Save_monthly_PRECT``` and daily output from ```Save_MDA8_O3```
- Returns yearly output

## Temperature

```Save_monthly_TREFHT.ipynb```  
Processes monthly temperature data, corrects incorrect month labels and crops to interested years
- Takes monthly data
- Returns monthly output

```Save_OSDMA8_with_T.ipynb```  
***This script needs fixing***

```Save_T6M.ipynb```  
***This script needs fixing***

## Tropopause Height 

```Save_monthly_TROP_pres.ipynb```  
Processes monthly tropopause height data (in pressure), corrects incorrect month labels and crops to interested years
- Takes monthly data
- Returns monthly output




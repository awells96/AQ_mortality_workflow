# mortality_utils.py
# Functions specific to mortality calculations

# att_frac
# mortality

import xarray as xr
import numpy as np


# === Attributal fraction ===
def att_frac(x, TMREL, beta):
    # equation is: AF = (RR - 1)/RR
    # where RR = e^(beta*(x-TMREL)), GBD 2021

    O3_diff = x - TMREL
    TMREL_O3 = xr.where(O3_diff > 0, O3_diff, 0)  # where the difference < 0 set to 0

    RR = np.exp(beta * TMREL_O3)
    AF = (RR - 1)/RR
    return AF


# === Mortality equation ===
def mortality(AF, bmr, pop):
    # equation is: M(x,y) = AF(x,y) * BMR_c * POP(x,y)
    M = AF * bmr * pop
    return M

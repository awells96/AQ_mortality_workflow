# COPD Mortality due to surface ozone

## Mortality equations

```math
M(x,y) = POP(x,y) * BMR_c * AF(x,y)
```

```math
AF(x,y) = \frac{1 - RR(x,y)}{RR(x,y)}
```

```math
RR(x,y) = e^{\beta \, (OSDMA8(x,y) - TMREL)}
```



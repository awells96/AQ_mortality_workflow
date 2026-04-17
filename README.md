# An Open-Access Workflow Combining Climate Model Projections with Epidemiological Frameworks to Assess Air Quality Mortality

> A reproducible workflow to calculate excess mortality due to changes in surface ozone and PM<sub>2.5</sub>.

This repository contains the workflow presented in **[An Open-Access Workflow Combining Climate Model Projections with Epidemiological Frameworks to Assess Air Quality Mortality](https://doi.org/10.22541/essoar.177170388.88002537/v1)**. The aim is to allow users to apply the workflow directly to address specific research questions, modify individual components (for example, exposure metrics, epidemiological inputs, or scenarios) to suit their study design, or extend it to related applications. It can also be used as a tutorial to understand the framework using an [example dataset](https://doi.org/10.5281/zenodo.18436835), reproducing the results and figures in the paper. 

**A. F. Wells**, J. W. Hurrell, E. Gilleland, & G. B. Anderson (2026).  
An Open-Access Workflow Combining Climate Model Projections with Epidemiological Frameworks
to Assess Air Quality Mortality.
ESS Open Archive. 21 February 2026. <https://doi.org/10.22541/essoar.177170388.88002537/v1>

## Getting Started

### 1. Fork and clone the repository

To use or adapt this workflow, start by forking the repository to your own GitHub account:

1. Click the **Fork** button at the top-right of this page.
2. Once forked, clone your copy locally:

```bash
git clone https://github.com/<your-username>/AQ_mortality_workflow.git
cd AQ_mortality_workflow
```

### 2. Download the example data

The input data required to run an example of the workflow are hosted on Zenodo:

> Wells, A. F., Anderson, G. B., Hurrell, J. W., & Gilleland, E. (2026). Air Quality Mortality Workflow: Input Datasets (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.18436835

Download and extract the dataset. **The directory structure inside the archive should be preserved** — the scripts assume a specific layout and will not find inputs correctly if files are moved or reorganised. When a notebook calls a specific directory it runs a check to see if the file path exists and throws an error if it does not. More on the file path structure below.

### 3. Configure file paths

Open `config.py` and update the root data path to point to wherever you extracted the example data on your machine. For example:

```python
# config.py

# Set this to the root of the downloaded example data directory
WORK_DIR = "/path/to/your/working/data"
SCRATCH_DIR = "/path/to/your/scratch/data"
PLOTTING_DIR = "/path/to/your/figures/"
```

All other paths in the workflow are constructed relative to each root, so these are the only paths you should need to change to get started with the example dataset.

### 4. Configure the directory structure

The notebooks are set up so that you can configure your file path roots and the scripts will save and pull the relevant data relative to those roots. Therefore to save data in the correct location, and to ensure file paths are present, create the directory structure using the outline below.

The directory structure is explained [here](https://github.com/awells96/AQ_mortality_workflow/blob/d840c3f7254259db3cd58c5d72893dbef205cbe5/directory_structure.md). 

### 5. Run the workflow

The workflow is structured into three parallel tracks — `population`, `bmr`, and climate variables (`ozone` and `pm25`) — before converging in the `mortality` step. A recommended execution order is:

1. Run `population` processing scripts
2. Run `bmr` processing scripts
3. Run `ozone` and `pm25` processing scripts (these can be run in parallel)
4. Run the `mortality` scripts for each variable

Each script is designed to be run independently once its inputs are available. To reproduce Figures 2 and 3 from the paper, run the scripts in `/plotting/mortality/` after completing the steps above.

### 6. (Optional) Edit the workflow

If you are happy that you understand how the workflow operates, you can make your own edits. For example you can apply your own climate variable data or use different exposure functions.

## Abstract

Surface-level air pollution is a major contributor to human mortality worldwide, and future climate change is expected to alter concentrations of pollutants such as ozone and particulate matter. Estimating the health burden of these changes requires combining climate model projections with epidemiological frameworks, such as those developed in the Global Burden of Disease (GBD) study. However, significant barriers hinder this integration. Climate model outputs differ from health metrics in spatial resolution, temporal aggregation, and pollutant definitions. For example, GBD quantifies ozone exposure as the highest seasonal average of 8-hour daily maximum concentrations, while most climate models provide hourly or monthly mean data. Furthermore, model outputs often require bias correction and spatial downscaling to align with exposure-response functions derived from observational data.

We present an open-access workflow designed to bridge this gap, enabling researchers to process climate model data for health impact assessments of air quality. The workflow processes climate model pollutant data to align with GBD metrics, applies bias correction and downscaling methods, and calculates mortality using established GBD exposure-response functions and baseline demographic data. This approach allows consistent, reproducible estimation of future health impacts across scenarios and models. By making the workflow publicly available, we aim to lower barriers for interdisciplinary research and support collaboration between climate scientists and epidemiologists. This work provides a foundation for quantifying the health implications of changing air quality under future climate conditions, improving decision-making around mitigation and adaptation strategies.

<img src="Workflow_figure.png" alt="drawing" width="500"/>

## Citation

If you use this workflow, please cite:

> **A. F. Wells**, J. W. Hurrell, E. Gilleland, & G. B. Anderson (2026). An Open-Access Workflow Combining Climate Model Projections with Epidemiological Frameworks
to Assess Air Quality Mortality. ESS Open Archive. 21 February 2026. <https://doi.org/10.22541/essoar.177170388.88002537/v1>

## Contact

For questions or issues related to the workflow, please contact:

* **Author**: Alice F. Wells
* **Affiliation**: Colorado State University
* **Email**: awells96@rams.colostate.edu

## 📝 License

This repository is released under the **MIT** license. See `LICENSE` for details.

[![GitHub release](https://img.shields.io/github/v/release/awells96/AQ_mortality_workflow)](https://github.com/awells96/AQ_mortality_workflow/releases/latest)
[![GitHub license](https://img.shields.io/github/license/awells96/AQ_mortality_workflow?color=blue)](https://github.com/awells96/AQ_mortality_workflow/blob/main/LICENSE)

[![GitHub stars](https://img.shields.io/github/stars/awells96/AQ_mortality_workflow)](https://github.com/awells96/AQ_mortality_workflow)
[![GitHub forks](https://img.shields.io/github/forks/awells96/AQ_mortality_workflow)](https://github.com/awells96/AQ_mortality_workflow/fork)
</div>

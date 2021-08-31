# Data Science for Land Use and Land Cover Samples Assessment & Classification

[![Miniconda](https://img.shields.io/badge/miniconda-3-green)](https://docs.conda.io/en/latest/miniconda.html)
[![Docker SITS](https://img.shields.io/badge/BDC_SITS_RStudio-1.4.1103-green)](https://hub.docker.com/r/brazildatacube/sits-rstudio)
[![Docker SITS](https://img.shields.io/badge/BDC_SITS_RStudio-0.12.0-green)](https://hub.docker.com/r/brazildatacube/sits-rstudio)
[![R SITS](https://img.shields.io/badge/BDC_R_SITS-0.12.0-green)](https://github.com/e-sensing/sits)

This repository contains a test environment for the web interface for exploratory samples analysis [Sample Assessment App](https://github.com/AbnerErnaniADSFatec/sample-assessment).

## Abstract

Land Use and Land Cover (LULC) classification became a difficult task due to current changes that are increasingly unpredictable and dynamic. However this is increasing the development of auxiliary tools based on programming language that facilitate the Earth Observation Data (EO Data) acquisition and analysis. This approach aims to demonstrate a classification method based on image data extraction and analysis tools using SITS - Satellite Image Time Series Tool and Random Forest algorithm. This method has been tested with LULC samples in Southwest Amazon in Brazil localized in the State of Rondonia due to the increase of land use change in this area. The tests demonstrated that the available tools are important because it facilitates the customization of necessary parameters for image download and data cube construction.

## Introduction

Changes in land use and land cover are increasingly unforeseen and dynamic, which makes the classification of its characteristics an arduous task, so the use of tools that help in the process of acquisition and analysis of land observation data is debatable. were developed due to the extensive mass of data that is generated daily by satellite images.

Unforeseen changes in usage and coverage classes can bring challenges such as models that do not represent the desired variability or that have been misclassified. This study seeks to demonstrate how these tools can make the classification process fast and efficient by presenting a case study on the identification of certain land use and land cover classes in the southwestern Amazon over the state of Rondônia.

This Approach intends to use the SOM method implemented by the SITS package in R language combined with the Shiny package for the development of web applications with an R language and Jupyter Lab to provide the user with a collaborative environment for an efficient analysis of software as a solution . The software solutions aim to facilitate access to analysis methods for researchers who do not have specific technical knowledge of information technology, such as the application of programming languages and the construction of algorithms. Currently, the market for software building tools is overheated and new products are increasingly appearing to develop more specific and customized applications. Thus, it is possible to build a graphical interface that applies the previous training methods using the R programming language, then there are tools like the Shiny package for developing web applications with support for data manipulation and graph generation.

## Material and Methods

For this approach, a dataset of LULC samples identified by specialists based on high-resolution images combined with time series collected with the creation of a Sentinel-2 satellite local data cube, acquired with the STAC Client tool in Python programming language, was used. This images was previously processed and analyzed in the Jupyter Notebook workflow publishing and presentation platform.

With the [SITS - Satellite Image Time Series](https://github.com/e-sensing/sits) package for the R programming language, time series were extracted to perform the exploratory analysis of the samples, evaluating the quality of the samples and forming a new data set, thus calculating the statistical moments for each series associated with a class, where the Random Forest algorithm was used for classification, demonstrated that the accuracy of the classification process was somehow interesting.

This project uses a [Miniconda](https://docs.conda.io/en/latest/miniconda.html) virtual environment with the installation of necessary libraries.

Miniconda is a free minimal installer for conda. It is a small, bootstrap version of Anaconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others. Use the conda install command to install 720+ additional conda packages from the Anaconda repository.

Follow the steps for installation and configuration below:


 - **Step 1**. Update and install the virtual environment management with command line interface for Miniconda and creates the environment for run the Jupyter Notebooks:

~~~dos
conda update -n base -c defaults conda && \
    conda create --name sample-assessment r-base
~~~

 - Starts the last virtual environment created:

~~~dos
conda activate sample-assessment
~~~

 - **Step 2**. Generate the R Kernel for the environment. First install the packages `R-kernel`, `Jupyter`, `SITS` dependencies and the `stars` library for image raster data manipulation:

~~~dos
conda install -c conda-forge r-recommended r-irkernel jupyterlab r-sits r-gdalcubes r-gdal r-stars r-tensorflowc
~~~

 - Install the necessary dependencies for data visualization and analysis that are listed in this file [`./utils/R/install-requirements.r`](./utils/install-requirements.r) to facilitate the installation for R packages:

~~~dos
R -e "source('./utils/R/install-requirements.r')"
~~~

 - Add `R-Kernel` kernel specification to `Jupyter` installation, so long the `Jupyterhub` will recognize the kernel installation to work interactively:

~~~dos
R -e "IRkernel::installspec(name = 'R3', displayname = 'sample-assessment')"
~~~

 - **Step 3**. Update the `Python` dependencies installation. Update the `pip` to the last version and install the requirements listed in this file [`./utils/Python/requirements.txt`](./utils/requirements.txt). Maybe you need github login, because there are a dependency called `EO Cubes` that will need permission user for installation:

~~~dos
python -m pip install --upgrade pip &&
    python -m pip install -r ./utils/Python/requirements.txt
~~~

 - **Step 4**. Run jupyter lab environment server and enjoy:

~~~dos
jupyter lab
~~~

With the dependencies installed it is possible to run the Jupyter notebook environment and also possible to run the _scripts_ present in this repository. This apprach is based on two `Jupyter Notebooks` as you see below:

 - The notebook for image pre-processing and download for creation of data cube using Python programming language: [Jupyter Notebook for Image Pre-Processing](./ImageProcessingSER413TrabalhoFinalAbnerAnjos.ipynb);
 - The notebook for creation of data cube and analysis and classification land use and land cover using the R programming language: [Jupyter Notebook for a Sample Analysis and Classification](./DataScienceCAP394TrabalhoFinalAbnerAnjos.ipynb).

All test data can be acquired from github via the link ["Data Source"](https://github.com/AbnerErnaniADSFatec/computational-statistics-data/tree/main/data-science).

## Conclusion

As a result, it is expected to develop a case study about the environment for an exploratory analysis of UCT combined with time series collected from remote sensing images to present attributes that demonstrate the calculation of accuracy and quality of classified maps. It also seeks to develop software solutions for the dissemination of these methods to a scientific community that does not master information technology techniques.

The reproducibility in publications of methods in the area of knowledge is an important characteristic that has not been explored much in previous studies, at this point it is debatable the development of a platform that applies this method of structured graduation and that allows the sharing of information previously by means of a collaborative environment.

## References

 - [1] Lorena A. Santos, Karine R. Ferreira, Gilberto Camara, Michelle C. A. Picoli, and Rolf E. Simoes. Quality control and class noise reduction of satellite image time series. ISPRS Journal of Photogrammetry and Remote Sensing, 177:75–88, 2021. 

 - [2] Rwanga, S.S. and Ndambuki, J.M. (2017) Accuracy Assessment of Land Use/Land Cover Classification Using Remote Sensing and GIS. International Journal of Geosciences, 8, 611-622. 

 - [3] Lorena Alves Santos, Karine Ferreira, Michelle Picoli, Gilberto Camara, Raul Zurita-Milla, and Ellen-Wien Augustijn. Identifying spatiotemporal patterns in land use and cover samples from satellite image time series. MDPI - Remote Sensing, 13(5):974, 2021. 


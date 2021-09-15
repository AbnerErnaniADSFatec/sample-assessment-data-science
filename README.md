# Data Science for Land Use and Land Cover Samples Assessment & Classification

[![Miniconda](https://img.shields.io/badge/miniconda-3-green)](https://docs.conda.io/en/latest/miniconda.html)
[![Docker SITS](https://img.shields.io/badge/BDC_SITS_RStudio-1.4.1103-green)](https://hub.docker.com/r/brazildatacube/sits-rstudio)
[![Docker SITS](https://img.shields.io/badge/BDC_SITS_RStudio-0.12.0-green)](https://hub.docker.com/r/brazildatacube/sits-rstudio)
[![R SITS](https://img.shields.io/badge/BDC_R_SITS-0.12.0-green)](https://github.com/e-sensing/sits)

This repository contains a test environment for the web interface for exploratory samples analysis [Sample Assessment App](https://github.com/AbnerErnaniADSFatec/sample-assessment).

## Abstract

Land Use and Land Cover (LULC) classification became a difficult task due to problems about data collection and current changes that are increasingly unpredictable and dynamic. This approach aims to demonstrate a classification method based on usage of image data extraction and analysis tools to calculate the skewness and kurtosis of the time series distribution curve and the Random Forest algorithm to classify this features in areas of difficult data collection. This method has been tested with LULC samples in Southwest Amazon in Brazil localized in the State of Rondônia due to the difficulty in collecting data in this area.

**Key words** – Time Series, Land Use Classification, Random Forest, Satellite Image Data, Spatial Temporal Analysis, Software Tools, Image Processing.

## Resumo

A classificação do Uso e Cobertura da Terra (UCT) tornou-se uma árdua tarefa devido aos problemas na aquisição de dados e as mudanças que são cada vez mais imprevisíveis e dinâmicas. Este estudo visa demonstrar um método de classificação baseado no uso de ferramentas de extração e análise de dados de imagens para o cálculo da assimetria e achatamento da curva das séries temporais e o algoritmo Random Forest para a classificação destas características em áreas de difícil coleta. Este método foi testado com amostras UCT no sudoeste da Amazônia no Brasil localizadas no estado de Rondônia devido a dificuldade de coleta de dados nesta área.

**Palavras-chave** – Séries temporais, Classificação do Uso da Terra, Random Forest, Imagens de Satélite, Análise Espaço-Temporal, Soluções de Software, Processamento de Imagens.

## Introduction

Changes in Land Use and Land Cover (LULC) are increasingly unpredictable and dynamic, which makes the classification of their characteristics a difficult task [[1]](./README.md#References). Classified maps of LULC change can visually demonstrate deforestation, disturbances, pressure and urbanization [[2]](./README.md#References).

Remote Sensing techniques and Earth Observation Data (EO Data) satellites provide a continuous and consistent set of information about land use due to their dense amount of data that is generated daily [[3]](./README.md#References). Therefore this is increasing the development of auxiliary tools based on programming language that facilitate the EO Data acquisition and analysis and the extensive use of these information, there is a growing demand to optimize the map classification process.

Spatial temporal analysis is an important feature for LULC classification due to the biodiversity change and climate change throughout the year. Understanding these patterns is essential for studies addressing environmental modeling and design and monitoring of land use policies [[4]](./README.md#References). However, there are current problems in data acquisition related to the sensors used, the climate of the region of interest that causes cloud coverage and other variables that can cause nodata in the collections.

The legal Amazon extends over an area of approximately 5,200,000 km2 and represents 59% of Brazil’s land mass. The region is home to a very high ecological and socioeconomic diversity [[4]](./README.md#References). Although, there is difficulties in collecting data from Amazon biome due to the high cloud coverage and the tasks for processing of images takes time until the final classification result. This study aims to demonstrate how these tools can make the classification process faster and efficient by presenting a case study on the identification of certain LULC classes.

## Material and Methods

This approach uses a dataset of LULC samples coupled with time series collected with the creation of a local data cube. The Data extraction was performed by three steps: (1) the images download and analysis of quality, (2) the time series data extraction and (3) the samples quality analysis for the Random Forest algorithm input.

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

 - **Step 3**. Update the `Python` dependencies installation. Update the `pip` to the last version and install the requirements listed in this file [`.utils/Python/requirements.txt`](./utils/requirements.txt). Maybe you need github login, because there are a dependency called `EO Cubes` that will need permission user for installation:

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

This approach presented a classification method based on usage of image data extraction and analysis tools to calculate the asymmetry and flattening of the time series distribution curve and the Random Forest algorithm to classify this features.

The tests demonstrated that the available tools are important because it facilitates the customization of necessary parameters for image download and data cube construction. Time series extraction tools as SITS have demonstrated high usability when dealing with time series analysis, mainly with the application of cloud coverage and data interpolation.

The classification of time series based on the distribution of values using statistical moment calculation tools such as asymmetry and flattening of the distribution curve demonstrated high accuracy to classify four LULC samples. However, this approach needs more studies related to better use of data extraction and analysis tools and how these tools can influence the final result.

## References

 - [1] Sophia S. Rwanga and Ndambuki J. M. Accuracy assessment of land use/land cover classification using remote sensing and GIS. International Journal of Geosciences, 8(4):611–622, 2017.
 - [2] Pontus Olofsson, Giles M. Foody, Martin Herold, Stephen V. Stehman, Curtis E. Woodcock, and Michael A. Wulder. Good practices for estimating area and assessing accuracy of land change. Journal of Remote Sensing of Environment, 148:42–57, 2014.
 - [3] Adeline Marinho Maciel and Lúbia Vinhas. Time series classification using features extraction to identification of use land and cover land: A case study in the municipality of itaqui, south region of brazil. Anais do XVIII Simpósio Brasileiro de Sensoriamento Remoto, 2017.
 - [4] Cláudio Aparecido de Almeida, Alexandre Camargo Coutinho, Júlio César Dalla Mora Esquerdo, Marcos Adami, Adriano Venturieri, Cesar Guerreiro Diniz, Nadine Dessay, Laurent Durieux, and Alessandra Rodrigues Gomes. High spatial resolution land use and land cover mapping of the Brazilian Legal Amazon in 2008 using Landsat-5 TM and MODIS data. Acta Amazonia, 46(3):291 – 302, September 2016.
 - [5] Gilberto Camara and Rolf Simoes. Data sets for the sits package, 2021.
 - [6] Matheus C Zaglia, Lubia Vinhas, Gilberto R Queiroz, and Rolf Simoes. Catalogação de Metadados do Cubo de Dados do Brasil com o SpatioTemporal Asset Catalog. Proceedings XX GEOINFO, pages 280–285, 2019.
 - [7] Mathieu Lepot, Jean-Baptiste Aubin, and François H.L.R. Clemens. Interpolation in time series: An introductive overview of existing methods, their performance criteria and uncertainty assessment. MDPI, 9:796, 2017.
 - [8] Rolf Simoes, Gilberto Camara, Felipe Souza, Pedro Andrade, Lorena Santos, Karine Ferreira, Gilberto Queiroz, Alexandre Ywata de Carvalho, and Victor Maus. sits: Data Analysis and Machine Learning using Satellite Image Time Series. INPE - Brazilian National Institute for Space Research, Sao Jose dos Campos, Brazil, 2021.
 - [9] Lorena A. Santos, KarinerR. Ferreira, Gilberto Camara, Michelle C. A. Picoli, and Rolf E. Simoes. Quality control and class noise reduction of satellite image time series. ISPRS Journal of Photogrammetry and Remote Sensing, 177:75–88, 2017.
 - [10] Ronald E. Walpole, Raymond H. Myers, Sharon L. Myers, and Keying Ye. Probability & Statistics for Engineers & Scientists. Pearson, 9 edition, 2012.
 - [11] R Core Team. R: A Language and Environment for Statistical Computing. R Foundation for Statistical Computing, Vienna, Austria, 2013.
 - [12] Serhii Havryliuk, Mykola Korol, Olha Tokar, Vovk Olena, and Lubov Kolyasa. Using the random forest classification for land cover interpretation of landsat images in the prykarpattya region of ukraine. 2018 IEEE 13th International Scientific and Technical Conference on Computer Science and Information Technologies (CSIT), 2018.

# Sample Assessment Data Science

[![Miniconda](https://img.shields.io/badge/miniconda-3-green)](https://docs.conda.io/en/latest/miniconda.html)
[![Docker SITS](https://img.shields.io/badge/BDC_SITS_RStudio-1.4.1103-green)](https://hub.docker.com/r/brazildatacube/sits-rstudio)
[![Docker SITS](https://img.shields.io/badge/BDC_SITS_RStudio-0.12.0-green)](https://hub.docker.com/r/brazildatacube/sits-rstudio)
[![R SITS](https://img.shields.io/badge/BDC_R_SITS-0.12.0-green)](https://github.com/e-sensing/sits)

Este repositório contém um ambiente de testes para a interface de análise exploratória de amostras [Sample Assessment App](https://github.com/AbnerErnaniADSFatec/sample-assessment).

## Abstract (Provisório)

Esta proposta pretende utilizar o método SOM implementado pelo pacote SITS em linguagem R combinado com o pacote Shiny para o desenvolvimento de aplicações web com a linguagem R e Jupyter Lab para disponibilizar para o usuário um ambiente colaborativo para a análise eficiente das amostras como uma solução de software. As soluções de software têm como objetivo facilitar o acesso aos métodos de análise a pesquisadores que não possuem conhecimentos técnicos específicos de tecnologia da informação como aplicação de linguagens de programação e construção de algoritmos. Atualmente o mercado para ferramentas de construção de software está superaquecido e cada vez mais surgem novos produtos para desenvolver aplicações mais específicas e customizadas. Assim é possível construir uma interface gráfica que aplique os métodos apresentados anteriormente que utilizam a linguagem de programação R, logo há ferramentas como o pacote Shiny para o desenvolvimento de aplicações para a web com suporte para a manipulação de dados e geração de gráficos.

## Dependências

### SITS

O pacote [`SITS - Satellite Image Time Series`](https://github.com/e-sensing/sits) Analysis for Earth Observation Data Cubes fornece um conjunto de ferramentas para a análise, visualização e classificação de séries temporais provenientes de imagens de satélite.

A principal funcionalidade do pacote `sits` é o suporte para a classificação de mudanças de uso e cobertura da terra em imagens de satélite.

Fluxo de Trabalho do `sits`:

 - Criação de um cubo de dados utilizando coleções de imagens provenientes de serviços em nuvem ou locais;
 - Extração das séries temporais;
 - Análise e avaliação de amostras;
 - Treinamento de algoritmos de aprendizagem de máquina;
 - Classificação de um cubo de dados utilzando o modelo de aprendizagem de máquina;
 - Pós processamento das imagens;
 - Avaliação da acurácia gerada pelo modelo utilizando boas práticas;

## Ambiente de desenvolvimento em R MiniConda

Atualizar a instalação do gerenciador de ambientes Miniconda e criar o ambiente virtual conda pela linha de comando:

~~~dos
conda update -n base -c defaults conda && \
    conda create --name sample-assessment r-base
~~~

Iniciar o ambiente virtual criado acima:

~~~dos
conda activate sample-assessment
~~~

Gerar o _kernel_ para o ambiente criado, instalando os pacotes `R-kernel` e `Jupyter`, além de instalar as dependências do `sits` com o ambiente virtual conda iniciado acima:

~~~dos
conda install -c conda-forge r-recommended r-irkernel jupyterlab r-sits
~~~

Intalar as dependências como a biblioteca `stars` para a manipulação de dados raster:

~~~dos
conda install -c conda-forge r-stars
conda install -c conda-forge/label/cf202003 r-stars
~~~

Instalar mais as dependências para a visualização dos dados listadas no arquivo [`install-requirements.r`](./install-requirements.r) para facilitar a instalação:

~~~dos
R -e "source('install-requirements.r')"
~~~

Adicione o R-kernel ao Jupyter instalando anteriormente uma especificação do kernel. Isso permite que o Jupyter reconheça o kernel e trabalhar com ele interativamente:

~~~dos
R -e "IRkernel::installspec(name = 'R3', displayname = 'sample-assessment')"
~~~

Com as dependências instaladas é possível executar o ambiente do Jupyter notebook, os testes e códigos podem ser encontrados em [Jupyter Notebook para a Análise de Amostras](./DataScienceCAP394TrabalhoFinalAbnerAnjos.ipynb). Também é possível executar os _scripts_ presentes no [Jupyter Notebook para o Processamento de Imagens](./ImageProcessingSER413TrabalhoFinalAbnerAnjos.ipynb).

Alguns testes em `Python` e `R` podem ser encontrados em [`./testes`](./testes):

 - Testes em Linguagem `R`: [`./testes_r.ipynb`](./testes/testes_r.ipynb);
 - Testes em Linguagem `Python`: [`./testes_python.ipynb`](./testes/testes_python.ipynb).

Os dados de teste podem ser adiquiridos no github por meio do link ["Fonte de dados de amostras de UCT com séries temporais"](./data).

Execute o comando abaixo para iniciar o servidor do `Jupyter Lab`:

~~~dos
jupyter lab
~~~

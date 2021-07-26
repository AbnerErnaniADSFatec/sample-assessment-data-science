# Sample Assessment App

[![Miniconda](https://img.shields.io/badge/miniconda-3-green)](https://docs.conda.io/en/latest/miniconda.html)
[![Docker SITS](https://img.shields.io/badge/BDC_SITS_-1.4.1103-green)](https://hub.docker.com/r/brazildatacube/sits-rstudio)

Esta proposta pretende utilizar o método SOM implementado pelo pacote SITS em linguagem R combinado com o pacote Shiny para o desenvolvimento de aplicações web com a linguagem R e Jupyter Lab para disponibilizar para o usuário um ambiente colaborativo para a análise eficiente das amostras como uma solução de software.

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

Atualizar e criar o ambiente conda:

~~~dos
conda update -n base -c defaults conda && \
    conda create --name sample-assessment r-base
~~~

Executar o ambiente virtual criado acima:

~~~dos
conda activate sample-assessment
~~~

Gerar o _kernel_ para o ambiente criado, instalando os pacotes `R-kernel` e `Jupyter`, além de instalar as dependências do sits com um ambiente virtual conda:

~~~dos
conda install -c conda-forge r-recommended r-irkernel jupyterlab r-sits
~~~

Intalar as dependências como a biblioteca `stars` para a manipulação de dados raster:

~~~dos
conda install -c conda-forge r-stars
conda install -c conda-forge/label/cf202003 r-stars
~~~

Instalar mais as dependências para a visualização dos dados:

~~~dos
R -e "source('install-requirements.r')"
~~~

Adicione o R-kernel ao Jupyter instalando uma especificação do kernel. Isso permite que o Jupyter reconheça o kernel e trabalhe com ele interativamente:

~~~dos
R -e "IRkernel::installspec(name = 'R3', displayname = 'sample-assessment')"
~~~

Instalar os requisitos necessários do arquivo [`install-requirements.r`](./install-requirements.r).

Com as dependências instaladas é possível executar o ambiente do  Jupyter notebook, os testes podem ser encontrados em [Arquivo de Testes](./DataScienceCAP394TrabalhoFinalAbnerAnjos.ipynb):

~~~dos
jupyter lab
~~~

Os dados de teste podem ser adiquiridos no github por meio do link ["Fonte de dados de amostras de UCT com séries temporais"](https://www.kaggle.com/abneranjos/luccsamples).

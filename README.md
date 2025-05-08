# Análise Exploratória de Dados de Admissões Hospitalares com Foco em Cardiologia e Influência da Poluição

## Visão Geral do Projeto

Este projeto consiste em uma análise exploratória de dados (EDA) abrangente de admissões hospitalares em uma unidade de cardiologia. O objetivo principal é compreender os padrões, características e fatores associados às admissões, bem como investigar a possível influência da poluição na saúde dos pacientes cardíacos.

A análise utiliza um conjunto de dados do mundo real, permitindo obter insights relevantes sobre o cenário de saúde em questão.

## Conjunto de Dados

Os dados utilizados neste projeto foram coletados do **Hero DMC Heart Institute**, uma unidade do **Dayanand Medical College and Hospital**, em Ludhiana, Punjab, Índia, durante o período de **1 de abril de 2017 a 31 de março de 2019**.

O conjunto de dados é composto por quatro arquivos:

- `table_headings.csv`: Dicionário de dados, contendo os nomes das colunas e suas descrições.
- `HDHI Admission data.csv`: Dados detalhados sobre as admissões dos pacientes na unidade de cardiologia.
- `HDHI Mortality Data.csv`: Informações sobre os pacientes que faleceram durante o período de estudo.
- `HDHI Pollution Data.csv`: Dados diários sobre a qualidade do ar e as condições climáticas na região.

Mais detalhes sobre o dataset podem ser encontrados [aqui](https://doi.org/10.3390/diagnostics12020241).

## Estrutura do Repositório

A estrutura do projeto é organizada da seguinte forma:

- **data/**: Contém os dados brutos em formato CSV relacionados às admissões hospitalares, mortalidade e poluição.
- **notebooks/**: Contém notebooks Jupyter para análise exploratória de dados (EDA), incluindo visualizações, cálculos estatísticos e insights gerados a partir dos dados.
- **scripts/**: Scripts Python usados para pré-processamento de dados, modelagem e geração de relatórios. Pode conter funções reutilizáveis.
- **README.md**: Documento com as informações principais sobre o projeto, como objetivos, estrutura e instruções de uso.

## Como Rodar o Projeto

### Pré-requisitos

Certifique-se de ter o Python 3 instalado em sua máquina. Além disso, será necessário instalar as bibliotecas necessárias, que estão listadas no arquivo `requirements.txt`. Para instalar as dependências, execute o seguinte comando:

```bash
pip install -r requirements.txt

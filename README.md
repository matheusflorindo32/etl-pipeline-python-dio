<div align="center">

# ETL PIPELINE COM IA GENERATIVA

### Extração, transformação e carga de dados com Python

[![Status](https://img.shields.io/badge/status-laboratório%20funcional-16A34A?style=flat-square)](#fluxo-etl)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](#execução-local)
[![Pandas](https://img.shields.io/badge/Pandas-transformação-150458?style=flat-square&logo=pandas&logoColor=white)](#stack)
[![Origem](https://img.shields.io/badge/origem-Desafio%20DIO-F97316?style=flat-square)](https://www.dio.me/)

</div>

---

## Visão geral

Laboratório educacional de engenharia de dados que implementa um fluxo **Extract, Transform, Load (ETL)** em Python. O pipeline lê registros de um CSV ou de uma base mock, gera mensagens personalizadas em modo local ou com integração opcional à OpenAI e exporta os resultados em JSON e CSV.

## Fluxo ETL

| Etapa | Operação | Saída |
|---|---|---|
| **Extract** | leitura de `SDW2023.csv` ou dados mock | registros normalizados |
| **Transform** | geração de mensagens personalizadas | registros enriquecidos |
| **Load** | serialização dos resultados | `output.json` e `output.csv` |

## Execução local

```bash
git clone https://github.com/matheusflorindo32/etl-pipeline-python-dio.git
cd etl-pipeline-python-dio
python -m venv .venv
```

Ative o ambiente virtual conforme seu sistema e execute:

```bash
pip install -r requirements.txt
python main.py
```

A integração externa é opcional. Quando utilizada, configure a chave por variável de ambiente e nunca grave segredos no código ou no repositório.

## Modos de transformação

- **local/mock** — permite executar o laboratório sem serviço externo;
- **OpenAI opcional** — gera conteúdo com modelo de linguagem quando configurado;
- **fallback** — mantém o fluxo demonstrável caso a API não esteja disponível.

## Stack

`Python` · `Pandas` · `CSV` · `JSON` · `OpenAI API (opcional)` · `Git/GitHub`

## Estrutura esperada

```text
etl-pipeline-python-dio/
├── main.py
├── requirements.txt
├── SDW2023.csv
├── output.csv
├── output.json
└── README.md
```

## Escopo

O projeto demonstra fundamentos de ETL e integração de IA em pequena escala. Para produção, seriam necessários testes, observabilidade, validação de esquema, tratamento de erros, controle de custos e políticas de proteção de dados.

## Competências demonstradas

`Engenharia de Dados` · `ETL` · `Python` · `Pandas` · `Integração de API` · `Documentação Técnica`

---

<div align="center">

Desenvolvido por **Matheus Florindo de Deus**  
[Tropa Científica](https://www.tropacientifica.com) · [Portfólio GitHub](https://github.com/matheusflorindo32)

</div>

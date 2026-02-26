# 🚀 ETL Pipeline com Python e IA Generativa

Projeto desenvolvido no Lab da DIO (Santander Dev Week 2023) com foco na construção de um pipeline ETL (Extract, Transform, Load) utilizando Python.

---

## 📌 Objetivo

Simular o uso de IA Generativa para criação de mensagens personalizadas para clientes bancários, demonstrando o fluxo completo de dados.

---

## 🔄 Estrutura do Pipeline

### 🔹 1. Extract (Extração)
- Leitura de usuários a partir de:
  - Arquivo CSV (`SDW2023.csv`)
  - OU lista mock local (caso CSV não exista)

### 🔹 2. Transform (Transformação)
- Geração de mensagens personalizadas sobre investimentos.
- Pode funcionar:
  - 🔸 Simulação local (sem API externa)
  - 🔸 Com API OpenAI (se configurada via variável de ambiente)

### 🔹 3. Load (Carregamento)
- Exportação dos dados gerados para:
  - `output.json`
  - `output.csv`

---

## 🛠 Tecnologias Utilizadas

- Python
- Pandas
- OpenAI API (opcional)
- Git & GitHub

---

## ▶️ Como Executar

```bash
pip install -r requirements.txt
python main.py

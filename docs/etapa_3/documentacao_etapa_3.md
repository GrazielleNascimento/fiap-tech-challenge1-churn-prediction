# Documentação da Etapa 3: Engenharia de Software e API de Inferência

Esta etapa foca na disponibilização do modelo treinado como uma API REST para predição de churn, com validação de entrada, testes automatizados e execução local em ambiente virtual.

---

## 1. Como iniciar o projeto e o ambiente virtual

Abra o terminal na raiz do projeto e execute os passos abaixo.

### 1.1 Criar o ambiente virtual

```bash
python -m venv venv
```

### 1.2 Ativar o ambiente virtual

No Windows com Git Bash:

```bash
source venv/Scripts/activate
```

No Windows com CMD ou PowerShell:

```bash
venv\Scripts\activate
```

### 1.3 Instalar as dependências

```bash
pip install -r requirements.txt
```

### 1.4 Executar os testes automatizados

```bash
python -m pytest -v
```

### 1.5 Iniciar a API

```bash
uvicorn src.main:app --reload
```

A documentação interativa da API fica disponível em:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

---

## 2. Estrutura dos arquivos da etapa 3

### `src/model.py`

Este módulo é responsável por carregar o modelo treinado salvo em `models/` e aplicar a inferência sobre novos dados.

Funções principais:

- carrega o artefato `.joblib` do modelo campeão;
- extrai o pipeline e o threshold de decisão;
- recebe um DataFrame com os dados do cliente;
- calcula a probabilidade de churn;
- retorna a previsão final em formato binário (`0` ou `1`).

Em resumo, esse arquivo encapsula toda a lógica de Machine Learning da aplicação.

### `src/main.py`

Este arquivo monta a aplicação FastAPI e expõe os endpoints da API.

Principais elementos:

- `ChurnInput`: modelo de entrada com validação via Pydantic;
- `GET /health`: endpoint de verificação de disponibilidade da API;
- `POST /predict`: recebe os dados do cliente e retorna a previsão e a probabilidade estimada.

A API converte o payload em um DataFrame e chama a função `predictor.predict(...)` do módulo `src/model.py`.

### `tests/test_api.py`

Arquivo de testes automatizados com Pytest e `TestClient` do FastAPI.

Os testes validam:

- `GET /health` retorna status `200` e mensagem esperada;
- `POST /predict` com payload válido retorna estrutura correta;
- os campos de retorno possuem tipos esperados: `churn_prediction` como inteiro e `probability` como float.

---

## 3. Endpoints da API

### `GET /health`

Retorna o status da API:

```json
{
  "status": "API is online"
}
```

### `POST /predict`

Recebe um payload com as características do cliente e devolve:

```json
{
  "churn_prediction": 0,
  "probability": 0.1784
}
```

Onde:

- `churn_prediction`: previsão do modelo (`0` ou `1`);
- `probability`: probabilidade estimada de churn.

---

## 4. Casos de teste para validação da API

### Caso 1: cliente com baixo risco de churn

Objetivo: verificar se o modelo identifica corretamente um cliente estável e fiel.

```json
{
  "gender": "Female",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "Yes",
  "tenure": 71,
  "PhoneService": "Yes",
  "MultipleLines": "Yes",
  "InternetService": "DSL",
  "OnlineSecurity": "Yes",
  "OnlineBackup": "Yes",
  "DeviceProtection": "Yes",
  "TechSupport": "Yes",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Two year",
  "PaperlessBilling": "No",
  "PaymentMethod": "Bank transfer (automatic)",
  "MonthlyCharges": 85.2,
  "TotalCharges": 6015.5
}
```

### Caso 2: cliente com alto risco de churn

Objetivo: validar se o modelo identifica um cliente com perfil de provável cancelamento.

```json
{
  "gender": "Male",
  "SeniorCitizen": 1,
  "Partner": "No",
  "Dependents": "No",
  "tenure": 2,
  "PhoneService": "Yes",
  "MultipleLines": "Yes",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "No",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "Yes",
  "StreamingMovies": "Yes",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 95.5,
  "TotalCharges": 180.5
}
```

---

## 5. Fluxo de uso da API

1. Criar e ativar o ambiente virtual.
2. Instalar as dependências do projeto.
3. Rodar os testes com `pytest`.
4. Subir a aplicação com Uvicorn.
5. Acessar a interface Swagger em `/docs`.
6. Enviar um JSON válido para `/predict`.
7. Verificar a resposta com a predição e a probabilidade.

---

## 6. Resumo

A Etapa 3 transforma o modelo de Machine Learning em um serviço de inferência pronto para uso em produção. O projeto organiza a lógica em módulos separados, valida entradas com Pydantic, disponibiliza a aplicação via FastAPI e garante qualidade com testes automatizados.

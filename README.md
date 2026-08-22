# Churn Prediction
## Descrição

Projeto de Machine Learning que treina um modelo com Scikit-Learn para previsão de churn de clientes e disponibiliza o modelo campeão por meio de uma API de inferência usando FastAPI. O repositório inclui o pipeline de treinamento, notebooks de análise e modelagem, artefatos dos modelos, testes automatizados e documentação técnica.

O código da aplicação está organizado em `src/churn_prediction`, com módulos separados para treinamento (`train`), API (`api`) e configurações compartilhadas (`common`).


Para conhecer o contexto de negócio, as premissas e as características da solução:

* [ML Canvas](docs/manual/ml_canvas.md)
* [Model Card](docs/manual/model_card.md)

# Setup
## Requisitos

* [Python 3.12+](https://wiki.python.org/moin/BeginnersGuide(2f)Download.html)
* [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Instalação

Na raiz do projeto, sincronize o ambiente com as dependências do projeto:

```bash
uv sync
```

O `uv` cria o ambiente virtual `.venv` e instala as dependências declaradas no `pyproject.toml`, incluindo as dependências de desenvolvimento.

# Execução
## Treinamento

O pipeline de treinamento pode ser executado com:

```bash
uv run python -m churn_prediction.train.main
```

Os artefatos de modelo são armazenados em `models/`.

## API local

Inicie o servidor com:

```bash
uv run uvicorn churn_prediction.api.main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa da API pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

Para testar a API, utilize os endpoints disponíveis na documentação interativa.

## Notebooks

Os notebooks estão em `notebooks/` e dependem do ambiente `.venv` criado pelo `uv`.

Após executar `uv sync`:

1. Abra o notebook desejado.
2. Selecione o kernel correspondente ao ambiente `.venv` do projeto.
3. Execute as células do notebook.

O ambiente já inclui `ipykernel` como dependência de desenvolvimento, portanto os notebooks utilizam as mesmas dependências instaladas pelo projeto.

Também é possível validar a reprodutibilidade dos notebooks:

```bash
uv run pytest --nbval notebooks/
```
# Desenvolvimento
## Testes

Execute os testes automatizados com:

```bash
uv run pytest
```

## Qualidade e tipagem

Verificação de lint:

```bash
uv run ruff check src/
uv run ruff check tests/
```

Formatação:

```bash
uv run ruff format src/
uv run ruff format tests/
```

Verificação de tipos:

```bash
uv run mypy src/
```

## Documentação

A documentação técnica da aplicação é construída com Sphinx.

Para preparar as dependências de documentação:

```bash
uv sync --group docs
```

Gere a documentação da técnica a partir do código:

```bash
rm -rf docs/build
rm -rf docs/source/generated

uv run sphinx-apidoc -f -o docs/source/generated src/churn_prediction
uv run sphinx-build -b html docs/source docs/build/html
```

O resultado fica em:

```text
docs/build/html/
```

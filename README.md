# Tech Challenge — Fase 1

Repositório do grupo para o desenvolvimento do Tech Challenge — Fase 1.

## Etapas

- Etapa 1: entendimento, preparação, AED e modelo de referência;
- Etapa 2: modelagem e avaliação;
- Etapa 3: engenharia e disponibilização;
- Etapa 4: documentação e entrega.

## Etapa 1

# Previsão de churn — Etapa 1

Primeira etapa do Tech Challenge de Machine Learning.  
O objetivo é entender a base de clientes, realizar a análise exploratória e criar um modelo inicial de Regressão Logística.

## Estrutura

```text
churn-etapa-1/
├── data/raw/                        # base original
├── notebooks/
│   └── etapa_1/
│       └── 01_eda_baseline.ipynb   # análise exploratória e baseline
├── docs/                            # ML Canvas e dicionário de dados
├── models/                          # modelos salvos
├── reports/                         # métricas e resultados
├── requirements.txt
└── README.md
```

## Como executar no VS Code

1. Abra esta pasta no VS Code.
2. Instale as extensões **Python** e **Jupyter**.
3. No terminal, crie o ambiente virtual:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

4. Instale as dependências:

```powershell
py -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

5. Abra `notebooks/etapa_1/01_eda_baseline.ipynb`.
6. Selecione o kernel da `.venv`.
7. Execute as células de cima para baixo.

O CSV já está em `data/raw`. Caso o arquivo seja movido, o notebook abre uma janela para selecioná-lo.

## Resultados do baseline

Os resultados esperados são próximos de:

- accuracy: 0.8055
- precision: 0.6572
- recall: 0.5588
- F1-score: 0.6040
- ROC-AUC: 0.8419

Esses valores podem variar um pouco conforme a versão das bibliotecas.

## ML Canvas

O ML Canvas está disponível em dois locais:

- dentro do notebook `notebooks/etapa_1/01_eda_baseline.ipynb`;
- no documento separado `docs/ml_canvas.md`.

## Etapa 2

# Modelagem e avaliação

Na etapa 2, o foco é treinar, comparar e avaliar modelos de classificação para churn, com destaque para:

- Rede Neural simples com `MLPClassifier`;
- comparação com modelos lineares e base line;
- aplicação de validação cruzada;
- avaliação com métricas como acurácia, precision, recall, F1-score e ROC-AUC;
- teste de estratégias para lidar com desbalanceamento (threshold, undersampling, oversampling e SMOTE);
- exportação do modelo final salvo em `.joblib` e dos resultados em arquivos JSON/CSV.

## Estrutura da etapa 2

```text
churn-etapa-1/
├── data/raw/                        # base original
├── notebooks/
│   ├── etapa_1/
│   │   └── 01_eda_baseline.ipynb
│   └── etapa_2/
│       ├── 02_mlp_model.ipynb
│       └── 03_ensemble_models.ipynb # notebook futuro
│
├── docs/                            # documentação e referências
├── models/                          # modelos salvos
├── reports/metrics/                 # métricas exportadas em JSON/CSV
├── requirements.txt
└── README.md
```

## Resultados do MLP campeão

- accuracy: 0.7881
- precision: 0.5920
- recall: 0.6511
- F1-score: 0.6192
- ROC-AUC: 0.8433

## Fluxo sugerido para a etapa 2

1. Executar o notebook de redes neurais em `notebooks/etapa_2/02_mlp_model.ipynb`.
2. Em seguida, utilizar um notebook complementar em `notebooks/etapa_2/03_ensemble_models.ipynb` para treinar modelos de ensemble.
3. Comparar os resultados em uma tabela consolidada.
4. Escolher um modelo campeão e salvar o artefato final em `models/`.

## Entregáveis esperados

- tabela comparativa de modelos;
- modelo final escolhido e salvo em `.joblib`;
- métricas registradas em arquivos de relatório.

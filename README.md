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

- Rede Neural simples com `MLPClassifier` (notebook `02_mlp_model.ipynb`);
- modelos de ensemble e baseline linear — Random Forest, Gradient Boosting e Regressão Logística (notebook `03_ensemble_models.ipynb`);
- comparação entre os modelos (linear, árvore/ensemble e MLP) e escolha de um modelo campeão;
- aplicação de validação cruzada estratificada;
- avaliação com métricas como acurácia, precision, recall, F1-score e ROC-AUC;
- teste de estratégias para lidar com desbalanceamento (threshold, undersampling, oversampling, class weight e SMOTE);
- análise de trade-off de custo entre falso positivo e falso negativo;
- exportação do modelo final salvo em `.joblib` e dos resultados em arquivos JSON/CSV.

Os dois notebooks da etapa 2 compartilham a mesma metodologia (mesmo pré-processador, mesma validação cruzada estratificada em 5 folds e as mesmas funções de métrica), o que torna a comparação entre modelos justa.

## Estrutura da etapa 2

```text
churn-etapa-1/
├── data/raw/                        # base original
├── notebooks/
│   ├── etapa_1/
│   │   └── 01_eda_baseline.ipynb
│   └── etapa_2/
│       ├── 02_mlp_model.ipynb        # rede neural (MLPClassifier)
│       └── 03_ensemble_models.ipynb  # RF, GB e baseline linear
│
├── docs/                            # documentação e referências
├── models/                          # modelos salvos (.joblib)
├── reports/                         # tabelas comparativas e de custo (CSV)
│   └── metrics/                     # métricas dos campeões (JSON)
├── requirements.txt
└── README.md
```

## Resultados do MLP campeão

Modelo campeão do notebook `02_mlp_model.ipynb` (MLP com threshold 0,40):

- accuracy: 0.7881
- precision: 0.5920
- recall: 0.6511
- F1-score: 0.6192
- ROC-AUC: 0.8433

## Resultados do ensemble campeão

Modelo campeão do notebook `03_ensemble_models.ipynb` (Gradient Boosting com threshold 0,35):

- accuracy: 0.7826
- precision: 0.5747
- recall: 0.6961
- F1-score: 0.6296
- ROC-AUC: 0.8459

Comparado ao MLP campeão, o Gradient Boosting apresentou maior recall (0,696 contra 0,651) e maior F1-score (0,630 contra 0,619), com ROC-AUC praticamente igual. Como o objetivo do problema é identificar clientes propensos ao cancelamento, o recall e o custo de negócio pesam mais do que a acurácia pura — por isso o Gradient Boosting com threshold 0,35 foi escolhido como modelo campeão consolidado da etapa 2 e exportado como artefato final.

Esses valores podem variar um pouco conforme a versão das bibliotecas.

## Fluxo sugerido para a etapa 2

1. Executar o notebook de redes neurais em `notebooks/etapa_2/02_mlp_model.ipynb`. Ele treina o MLP e salva os resultados em `reports/mlp_resultados.csv`.
2. Executar o notebook de ensembles em `notebooks/etapa_2/03_ensemble_models.ipynb`. Ele treina RF, GB e a Regressão Logística, carrega os resultados do MLP e monta a tabela comparativa consolidada.
3. Comparar os resultados na tabela consolidada e na análise de custo.
4. Escolher o modelo campeão e salvar o artefato final em `models/`.

> A ordem importa: o notebook de ensembles lê `reports/mlp_resultados.csv` para montar a tabela consolidada, então o notebook do MLP deve ser executado antes.

## Entregáveis esperados

- tabela comparativa de modelos (MLP, RF, GB e Regressão Logística);
- análise de custo (falso positivo vs. falso negativo);
- modelo final escolhido e salvo em `.joblib`;
- métricas registradas em arquivos de relatório (CSV/JSON).

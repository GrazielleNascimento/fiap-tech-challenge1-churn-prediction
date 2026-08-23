# ML Canvas

## Problema

A operadora precisa identificar clientes com maior chance de cancelar o contrato para organizar melhor as ações de retenção.

## Objetivo

Criar um modelo de classificação que estime a probabilidade de churn de cada cliente.

## Usuários do resultado

- equipe de retenção;
- marketing e CRM;
- atendimento;
- gestão;
- time de dados.

## Dados de entrada

Informações cadastrais, serviços contratados, tipo de contrato, tempo de relacionamento, mensalidade, valor total e método de pagamento.

## Saída do modelo

- previsão de churn ou não churn;
- probabilidade estimada de churn.

## Decisão apoiada

Ordenar os clientes por risco e priorizar os casos mais relevantes para contato ou análise.

## Métricas

### Técnicas

- F1-score;
- recall;
- precision;
- ROC-AUC;
- acurácia;
- matriz de confusão.

### Priorização

- Capture Rate@30%;
- Lift@30%.

## Metas iniciais

- ROC-AUC maior ou igual a 0,80;
- F1-score maior ou igual a 0,60;
- recall maior ou igual a 0,55;
- Capture Rate@30% maior ou igual a 0,60;
- Lift@30% maior ou igual a 2,00.

## Limitações

A base não possui dados de campanhas de retenção, ofertas, custos ou resultado financeiro. Por isso, não é possível medir diretamente clientes retidos, redução real de churn, receita preservada ou retorno sobre investimento.

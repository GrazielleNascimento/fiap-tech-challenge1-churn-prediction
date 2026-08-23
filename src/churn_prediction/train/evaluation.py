"""Funções para avaliação do modelo."""

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline


def calculate_metrics(
    y_true: pd.Series,
    y_pred: np.ndarray,
    y_proba: np.ndarray,
) -> dict[str, float]:
    """Calcula as métricas de classificação."""
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_true, y_proba)),
    }


def cross_validate_model(
    pipeline: Pipeline,
    X: pd.DataFrame,  # noqa: N803
    y: pd.Series,
    cv: StratifiedKFold,
    threshold: float,
) -> tuple[dict[str, float], np.ndarray]:
    """Avalia o modelo usando a mesma estratégia de CV do notebook."""
    fold_metrics = []
    confusion_matrices = []

    for train_idx, test_idx in cv.split(X, y):
        X_train = X.iloc[train_idx]  # noqa: N806
        X_test = X.iloc[test_idx]  # noqa: N806
        y_train = y.iloc[train_idx]
        y_test = y.iloc[test_idx]

        fold_pipeline = clone(pipeline)
        fold_pipeline.fit(X_train, y_train)

        probabilities = fold_pipeline.predict_proba(X_test)[:, 1]
        predictions = (probabilities >= threshold).astype(int)

        fold_metrics.append(
            calculate_metrics(
                y_true=y_test,
                y_pred=predictions,
                y_proba=probabilities,
            ),
        )

        confusion_matrices.append(
            confusion_matrix(
                y_test,
                predictions,
                labels=[0, 1],
            ),
        )

    mean_metrics = {
        str(key): float(value)
        for key, value in pd.DataFrame(fold_metrics).mean().items()
    }

    total_confusion_matrix = np.sum(confusion_matrices, axis=0)

    return mean_metrics, total_confusion_matrix

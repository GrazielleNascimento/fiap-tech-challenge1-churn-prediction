# ruff: noqa: N806
"""Lógica para treinamento do modelo."""

import json

import joblib
import pandas as pd
from numpy import ndarray
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline

from src.common.config import (
    CHAMPION_NAME,
    CHAMPION_THRESHOLD,
    DATA_PATH,
    METRICS_PATH,
    MODEL_PATH,
)
from src.train.model import build_model
from src.train.preprocessing import (
    load_dataset,
    split_features_target,
)


def main() -> None:
    """Orquestra treinamento do modelo."""
    df = load_dataset(DATA_PATH)
    X, y = split_features_target(df)

    pipeline = build_model()
    pipeline.fit(X, y)

    save_artifact(pipeline)

    probabilities = pipeline.predict_proba(X)[:, 1]
    save_metrics(
        y_true=y,
        y_pred=(probabilities >= CHAMPION_THRESHOLD).astype(int),
        y_proba=probabilities,
    )

    print(f"Modelo treinado e salvo em: {MODEL_PATH}")  # noqa: T201


def save_artifact(pipeline: Pipeline) -> None:
    """Salva artefato do modelo."""
    artifact = {
        "pipeline": pipeline,
        "threshold": CHAMPION_THRESHOLD,
        "model_name": CHAMPION_NAME,
    }

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, MODEL_PATH)


def save_metrics(
    y_true: pd.Series,
    y_pred: pd.Series,
    y_proba: ndarray,
) -> None:
    """Calcula e salva as métricas do modelo em arquivo .json."""
    METRICS_PATH.parent.mkdir(parents=True, exist_ok=True)

    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0),
        "roc_auc": roc_auc_score(y_true, y_proba),
    }

    METRICS_PATH.write_text(
        json.dumps([metrics], indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

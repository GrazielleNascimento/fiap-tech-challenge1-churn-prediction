# ruff: noqa: N806
"""Lógica para treinamento do modelo."""

import json

import joblib
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline

from src.common.config import (
    CHAMPION_NAME,
    CHAMPION_THRESHOLD,
    DATA_PATH,
    METRICS_PATH,
    MODEL_PATH,
    N_SPLITS,
    RANDOM_STATE,
)
from src.train.evaluation import cross_validate_model
from src.train.model import build_model
from src.train.preprocessing import (
    load_dataset,
    split_features_target,
)


def main() -> None:
    """Orquestra avaliação, treinamento final e persistência."""
    df = load_dataset(DATA_PATH)
    X, y = split_features_target(df)

    pipeline = build_model()

    cv = StratifiedKFold(
        n_splits=N_SPLITS,
        shuffle=True,
        random_state=RANDOM_STATE,
    )

    metrics, _ = cross_validate_model(
        pipeline=pipeline,
        X=X,
        y=y,
        cv=cv,
        threshold=CHAMPION_THRESHOLD,
    )

    save_metrics(metrics)

    pipeline.fit(X, y)
    save_artifact(pipeline)


def save_artifact(pipeline: Pipeline) -> None:
    """Salva o artefato final treinado com todos os dados."""
    artifact = {
        "pipeline": pipeline,
        "threshold": CHAMPION_THRESHOLD,
        "model_name": CHAMPION_NAME,
    }

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, MODEL_PATH)


def save_metrics(metrics: dict[str, float]) -> None:
    """Salva as métricas do campeão no formato do notebook."""
    output = {
        key: metrics[key]
        for key in (
            "accuracy",
            "precision",
            "recall",
            "f1",
            "roc_auc",
        )
    }

    METRICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    METRICS_PATH.write_text(
        json.dumps([output], indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

"""Testes relativos à src/train/main."""

import json

import joblib
import pandas as pd
from sklearn.dummy import DummyClassifier

import src.train.main as train_main


def test_save_artifact(tmp_path, monkeypatch) -> None:
    threshold = 0.6
    model_path = tmp_path / "model.joblib"

    monkeypatch.setattr(train_main, "MODEL_PATH", model_path)
    monkeypatch.setattr(train_main, "CHAMPION_THRESHOLD", threshold)
    monkeypatch.setattr(train_main, "CHAMPION_NAME", "test-model")

    pipeline = DummyClassifier(strategy="prior")

    train_main.save_artifact(pipeline)

    assert model_path.exists()

    artifact = joblib.load(model_path)

    assert artifact["pipeline"] is not None
    assert artifact["threshold"] == threshold
    assert artifact["model_name"] == "test-model"


def test_save_metrics_writes_expected_metrics(tmp_path, monkeypatch) -> None:
    metrics_path = tmp_path / "metrics.json"

    monkeypatch.setattr(train_main, "METRICS_PATH", metrics_path)

    y_true = pd.Series([0, 0, 1, 1])
    y_pred = pd.Series([0, 1, 1, 1])
    y_proba = pd.Series([0.1, 0.7, 0.8, 0.9])

    train_main.save_metrics(
        y_true=y_true,
        y_pred=y_pred,
        y_proba=y_proba,
    )

    assert metrics_path.exists()

    data = json.loads(metrics_path.read_text())

    assert len(data) == 1

    metrics = data[0]

    assert set(metrics) == {
        "accuracy",
        "precision",
        "recall",
        "f1",
        "roc_auc",
    }

    assert metrics["accuracy"] == 3 / 4
    assert metrics["precision"] == 2 / 3
    assert metrics["recall"] == 1.0
    assert metrics["f1"] == 0.8  # noqa: PLR2004
    assert 0 <= metrics["roc_auc"] <= 1

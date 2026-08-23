"""Testes relativos à churn_prediction/train/main."""

import joblib
from sklearn.dummy import DummyClassifier

import churn_prediction.train.main as train_main


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

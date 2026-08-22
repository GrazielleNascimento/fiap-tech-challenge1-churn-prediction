"""Fornece a lógica para criar modelo."""

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline

from src.common.config import RANDOM_STATE
from src.train.preprocessing import build_preprocessor


def build_model() -> Pipeline:
    """Cria pipeline do modelo Gradient Boosting."""
    classifier = GradientBoostingClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=3,
        random_state=RANDOM_STATE,
    )

    return Pipeline(
        [
            ("preprocessador", build_preprocessor()),
            ("classificador", classifier),
        ],
    )

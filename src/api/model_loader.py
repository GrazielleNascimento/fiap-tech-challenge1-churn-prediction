"""Fornece a lógica para carregar o artefatos do modelo."""

from functools import lru_cache
from typing import TypedDict

import joblib
from sklearn.pipeline import Pipeline

from src.common.config import MODEL_PATH


class ModelArtifact(TypedDict):
    """Estrutura do artefato do modelo."""

    pipeline: Pipeline
    threshold: float
    model_name: str


@lru_cache
def get_artifact() -> ModelArtifact:
    """Carrega os artefato do modelo."""
    return joblib.load(MODEL_PATH)


@lru_cache
def get_pipeline() -> Pipeline:
    """Retorna pipeline do modelo."""
    return get_artifact()["pipeline"]


@lru_cache
def get_threshold() -> float:
    """Retorna threshold do modelo."""
    return get_artifact()["threshold"]

"""Define e configura a API FastAPI para previsão de churn."""

from typing import Annotated

import pandas as pd
from fastapi import Depends, FastAPI
from sklearn.pipeline import Pipeline

from src.api.model_loader import get_pipeline, get_threshold
from src.api.schemas import HealthResponse, PredictInput, PredictResponse

app = FastAPI(title="Churn Prediction API")


@app.get("/health")
def health_check() -> HealthResponse:
    """Verifica se a API está disponível."""
    return HealthResponse(status="API is online")


@app.post("/predict")
def predict_churn(
    churn_input: PredictInput,
    pipeline: Annotated[Pipeline, Depends(get_pipeline)],
    threshold: Annotated[float, Depends(get_threshold)],
) -> PredictResponse:
    """Realiza a previsão de churn para um cliente."""
    df_input = pd.DataFrame([churn_input.model_dump()])
    proba = pipeline.predict_proba(df_input)[:, 1]
    prediction = (proba >= threshold).astype(int)

    return PredictResponse(
        churn_prediction=int(prediction[0]),
        probability=float(proba[0]),
    )

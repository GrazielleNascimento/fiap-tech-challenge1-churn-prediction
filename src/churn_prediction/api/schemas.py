"""Define os schemas de entrada da API de previsão de churn."""

from pydantic import BaseModel


class PredictInput(BaseModel):
    """Representa os dados de um cliente usados para prever churn."""

    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


class PredictResponse(BaseModel):
    """Representa os dados da predição do churn do cliente."""

    churn_prediction: int
    probability: float


class HealthResponse(BaseModel):
    """Representa a resposta do endpoint de saúde da API."""

    status: str

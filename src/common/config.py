"""Variáveis de configurações."""

from pathlib import Path

RANDOM_STATE = 42
CHAMPION_NAME = "ensemble_gb_threshold_0.35"
CHAMPION_THRESHOLD = 0.35

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
MODEL_PATH = PROJECT_ROOT / "models" / f"{CHAMPION_NAME}.joblib"
METRICS_PATH = PROJECT_ROOT / "reports" / "metrics" / f"metricas_{CHAMPION_NAME}.json"

TARGET_COLUMN = "Churn"
ID_COLUMN = "customerID"

NUMERIC_COLUMNS = ["tenure", "MonthlyCharges", "TotalCharges"]
CATEGORICAL_COLUMNS = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
]

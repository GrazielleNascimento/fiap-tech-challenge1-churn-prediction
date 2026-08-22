"""Testes relativos à src/api/main."""

from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)

STATUS_CODE_OK = 200


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == STATUS_CODE_OK
    assert response.json() == {"status": "API is online"}


def test_predict() -> None:
    payload = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 1,
        "PhoneService": "No",
        "MultipleLines": "No phone service",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 29.85,
        "TotalCharges": 29.85,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == STATUS_CODE_OK

    data = response.json()
    assert "churn_prediction" in data
    assert "probability" in data

    assert isinstance(data["churn_prediction"], int)
    assert isinstance(data["probability"], float)

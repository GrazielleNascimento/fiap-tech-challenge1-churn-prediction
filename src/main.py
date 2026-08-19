from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from src.model import predictor

app = FastAPI(title="Churn Prediction API")

class ChurnInput(BaseModel):
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

@app.get("/health")
def health_check():
    return {"status": "API is online"}

@app.post("/predict")
def predict_churn(data: ChurnInput):
    try:

        df = pd.DataFrame([data.dict()])
        

        prediction, probability = predictor.predict(df)
        
        return {
            "churn_prediction": prediction,
            "probability": probability
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
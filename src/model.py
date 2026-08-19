import joblib
import pandas as pd
from pathlib import Path


MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "ensemble_gb_threshold_0.35.joblib"

class ModelPredictor:
    def __init__(self):
        self.artifact = joblib.load(MODEL_PATH)
        self.pipeline = self.artifact["pipeline"]
        self.threshold = self.artifact["threshold"]

    def predict(self, input_df: pd.DataFrame):
        # O pipeline já contem o preprocessamento, só passamos o DF bruto
        proba = self.pipeline.predict_proba(input_df)[:, 1]
        prediction = (proba >= self.threshold).astype(int)
        
        return int(prediction[0]), float(proba[0])


predictor = ModelPredictor()
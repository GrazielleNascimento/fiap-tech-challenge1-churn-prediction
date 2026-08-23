"""Fornece de preprocessamento para `WA_Fn-UseC_-Telco-Customer-Churn.csv`."""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from churn_prediction.common.config import (
    CATEGORICAL_COLUMNS,
    ID_COLUMN,
    NUMERIC_COLUMNS,
    TARGET_COLUMN,
)


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Carrega e realiza tratamento nos dados brutos do csv."""
    df = pd.read_csv(path)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    return df


def split_features_target(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Extraí features e targets."""
    X = df.drop(columns=[ID_COLUMN, TARGET_COLUMN])  # noqa: N806
    y = (df[TARGET_COLUMN].str.lower() == "yes").astype(int)
    return X, y


def build_preprocessor() -> ColumnTransformer:
    """Cria pipeline de pré-processamento dos dados."""
    numeric_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ],
    )

    categorical_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ],
    )

    return ColumnTransformer(
        [
            ("num", numeric_pipeline, NUMERIC_COLUMNS),
            ("cat", categorical_pipeline, CATEGORICAL_COLUMNS),
        ],
    )

"""Testes relativos à churn_prediction/train/preprocessing."""

import pandas as pd

from churn_prediction.train.preprocessing import (
    load_dataset,
    split_features_target,
)


def test_load_dataset_converts_total_charges_to_numeric(tmp_path) -> None:
    csv_path = tmp_path / "data.csv"
    charge = 100.50

    pd.DataFrame(
        {
            "customerID": ["1", "2"],
            "TotalCharges": [f"{charge:.2f}", " "],
        },
    ).to_csv(csv_path, index=False)

    df = load_dataset(str(csv_path))

    assert pd.api.types.is_numeric_dtype(df["TotalCharges"])
    assert df.loc[0, "TotalCharges"] == charge
    assert pd.isna(df.loc[1, "TotalCharges"])


def test_split_features_target_is_case_insensitive() -> None:
    df = pd.DataFrame(
        {
            "customerID": ["1", "2", "3"],
            "tenure": [1, 2, 3],
            "MonthlyCharges": [10, 20, 30],
            "Churn": ["YES", "yes", "No"],
        },
    )

    _, y = split_features_target(df)

    assert y.tolist() == [1, 1, 0]

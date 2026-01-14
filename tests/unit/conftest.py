import pandas as pd
import pytest


@pytest.fixture
def sample_df():
    """
    Generates a sample banking dataset for client analysis.

    The dataset contains numerical, categorical, and binary target variables
    commonly used in banking and credit risk modeling tasks.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with 10 rows and 5 columns:
        - age : int
        - monthly_salary : int
        - has_car_loan : This column contains only null values
        - employment_type : str
        - account_type : str
        - defaulted : int
    """
    data = {
        "client_id": [f"C_{i * 100}" for i in range(10)],
        "age": [25, 34, 45, 29, 52, None, 37, 23, 48, 31],
        "monthly_salary": [2500, 4200, 6000, 3100, 7500, 5800, 4600, 2200, 6800, 50000],
        "has_car_loan": [None] * 10,
        "employment_type": [
            "salaried",
            "salaried",
            "self-employed",
            "salaried",
            "self-employed",
            "salaried",
            "salaried",
            "unemployed",
            "self-employed",
            "salaried",
        ],
        "account_type": [
            "basic",
            "basic",
            "basic",
            "basic",
            "premium",
            "basic",
            "basic",
            "basic",
            "premium",
            "basic",
        ],
        "transaction_code": [f"T{i}" for i in range(10)],
        "defaulted": [0, 0, 1, 0, 1, 0, 0, 1, 1, 0],
    }

    return pd.DataFrame(data)

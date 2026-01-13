import pandas as pd


def generate_test_banking_dataframe():
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
        "age": [25, 34, 45, 29, 52, None, 37, 23, 48, 31],
        "monthly_salary": [2500, 4200, 6000, 3100, 7500, 5800, 4600, 2200, 6800, 50000],
        "has_car_loan": [None, None, None, None, None, None, None, None, None, None],
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
        "defaulted": [0, 0, 1, 0, 1, 0, 0, 1, 1, 0],  # binary target
    }

    return pd.DataFrame(data)

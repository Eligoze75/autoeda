"""
Functions to support automated exploratory data analysis (EDA)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def check_na_outliers(
    df,
    outlier_method="auto",
    na_threshold=0.1,
    outlier_threshold=0.05,
    return_risk=True,
    return_suggestions=True,
):
    """
    Diagnose missing values and outliers in a DataFrame.

    This function summarizes the amount of missing values
    and potential outliers for each column in the input dataset.
    It is intended for exploratory data analysis and provides
    interpretable diagnostics for future data preprocessing.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset for exploratory data analysis.
    outlier_method : {"auto", "iqr", "zscore", "mad"}, default="auto"
        Method used to detect outliers in numeric columns. If "auto",
        the most appropriate method is selected,
        based on the distribution of each column.
    na_threshold : float, default=0.1
        Proportion threshold above which missing values are flagged
        as high risk. Further investigation or imputation may be needed
        if there are lots of missing values.
    outlier_threshold : float, default=0.05
        Proportion threshold above which outliers are flagged
        as high risk.
    return_risk : bool, default=True
        Whether to compute and return qualitative risk levels
        (e.g., "low", "medium", "high") based on the specified
        thresholds.
    return_suggestions : bool, default=True
        Whether to include suggested actions for handling missing
        values and outliers (e.g., imputation or transformation).

    Returns
    -------
    pandas.DataFrame
        A summary table with one row per column, including
        missing value statistics, outlier statistics (for numeric
        columns), and optional risk levels and suggested actions.
    """
    pass



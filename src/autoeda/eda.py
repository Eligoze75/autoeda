"""
Functions to support automated exploratory data analysis (EDA)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_unary(df, threshold=0.75, dropna=False):
    """
    Returns a list of columns with a single value with a relative
    frequency percentage over a threshold (75% as default).
    In case user want only unary columns then threshold should be set to 1.

    Parameters:
    df: pandas dataframe to analyze.
    threshold: If the relative frequency of the value with the highest counting
    is over this threshold then column is selected. Default is 0.75.
    dropna: If considering or not null values as a value in frequencies.
    Default is False.

    Returns:
    unary_cols: list of unary columns.
    """


def get_summary_df(df):
    """
    Returns a summary dataframe with the main statistics, datatypes,
    counts/missing values for numerical and categorical columns.

    Parameters:
    df: dataframe to summarize

    Returns:
    summary_df: dataframe with the summary statistics
    """

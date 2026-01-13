"""
Functions to support automated exploratory data analysis (EDA)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_summary_df(df):
    """
    Returns a summary dataframe with the main statistics, datatypes,
    counts/missing values for numerical and categorical columns.

    Parameters:
    df: dataframe to summarize

    Returns:
    summary_df: dataframe with the summary statistics
    """
    pass
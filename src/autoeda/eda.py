"""
functions to support automated exploratory data analysis (EDA)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_unary(df, threshold=0.75, dropna=False):
    """Returns a list of columns with a single value with a relative
    frequency percentage over a threshold (75% as default).
    In case user want only unary columns then threshold should be set to 1.

    Keyboards:
    df: dataframe to analyze
    threshold: If the relative frequency of the value with the highest counting
    is over this threshold then column is selected.
    dropna: If considering or not null values as a value in frequencies
    """
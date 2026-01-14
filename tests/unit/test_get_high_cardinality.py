"""
Unit tests for the get_high_cardinality function.

These tests validate the detection of high cardinality columns using
configurable uniqueness thresholds, including edge cases such as empty
dataframes and invalid input types.
"""

from autoeda.inspect import get_high_cardinality
import pandas as pd
import pytest


def test_high_cardinality_detected(sample_df):
    """
    Detect columns with a high unique to row ratio.
    """
    out = get_high_cardinality(sample_df, max_unique_ratio=0.8)
    assert "transaction_code" in out


def test_no_high_cardinality_with_strict_threshold(sample_df):
    """
    Return empty list when threshold is too strict.
    """
    out = get_high_cardinality(sample_df, max_unique_ratio=1.0)
    assert out == []


def test_numeric_columns_can_be_high_cardinality(sample_df):
    """
    Numeric columns with many unique values should be detected.
    """
    out = get_high_cardinality(sample_df, max_unique_ratio=0.8)
    assert "client_id" in out


def test_empty_dataframe():
    """
    Handle empty DataFrame gracefully.
    """
    assert get_high_cardinality(pd.DataFrame()) == []


def test_invalid_input_type():
    """
    Raise TypeError when input is not a DataFrame.
    """
    with pytest.raises(TypeError):
        get_high_cardinality("not a dataframe")

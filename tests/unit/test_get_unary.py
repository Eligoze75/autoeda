"""
Unit tests for the get_unary function.

This module verifies that get_unary correctly identifies unary categorical
columns under different parameter configurations and properly validates
input types.
"""

from autoeda.eda import get_unary
import pytest


def test_single_unary_col(sample_df):
    """
    Verify that unary columns are correctly detected using default parameters.
    """
    out = get_unary(sample_df)
    expected_out = list(["has_car_loan", "account_type"])
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_not_consider_null_cols(sample_df):
    """
    Verify that columns containing null values are excluded when dropna=True.
    """
    out = get_unary(sample_df, dropna=True)
    expected_out = list(["account_type"])
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_no_unary_cols(sample_df):
    """
    Verify that an empty list is returned when no columns meet the unary threshold.
    """
    out = get_unary(sample_df, threshold=0.9, dropna=True)
    expected_out = list()
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_wrong_input_type_error():
    """
    Verify that a TypeError is raised when the input is not a pandas DataFrame.
    """
    with pytest.raises(TypeError, match="df must be a pandas DataFrame"):
        get_unary("this is not a dataframe")

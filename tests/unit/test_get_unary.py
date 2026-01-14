"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

from autoeda.eda import get_unary
import pytest

# import sys
# import os


def test_single_unary_col(sample_df):
    """
    Test that get_unary works as expected with default params.
    """
    out = get_unary(sample_df)
    expected_out = list(["has_car_loan", "account_type"])
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_not_consider_null_cols(sample_df):
    """
    Test that get_unary works as expected. With dropna=True
    """
    out = get_unary(sample_df, dropna=True)
    expected_out = list(["account_type"])
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_no_unary_cols(sample_df):
    """
    Test that get_unary works as expected. With dropna=True and
    no unary cols.
    """
    out = get_unary(sample_df, threshold=0.9, dropna=True)
    expected_out = list()
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_wrong_input_type_error():
    with pytest.raises(TypeError, match="df must be a pandas DataFrame"):
        get_unary("this is not a dataframe")

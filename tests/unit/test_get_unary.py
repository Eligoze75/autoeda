"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

from autoeda.eda import get_unary
import pandas as pd
import sys
import os


def test_single_unary_col(sample_df):
    """
    Test that get_unary works as expected.
    """
    out = get_unary(sample_df, threshold=0.75, dropna=False)
    expected_out = list(["has_car_loan","account_type"])
    assert out == expected_out, f"Expected {expected_out} but got {out}"


def test_null_cols(sample_df):
    """
    Test that get_unary works as expected.
    """
    out = get_unary(sample_df, threshold=0.75, dropna=False)
    expected_out = list(["has_car_loan","account_type"])
    assert out == expected_out, f"Expected {expected_out} but got {out}"

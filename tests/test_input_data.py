__author__ = "Regenplatz"
__version__ = "1.0.0"


import numpy as np
import pandas as pd
from nelson_rules import NelsonRules
import pytest


##### INPUT DATA #################################################################

def test_inputData_formatIsListWithFloats() -> None:
    """
    Test Rule 1: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule1 = [
        1.22, 3.54, 7.80, 1.16, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, 1.22, 5.00]
    tr = NelsonRules(arr_input_rule1)
    tr.rule1()
    arr_expected_result_rule1 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule1"] == arr_expected_result_rule1).all()


def test_inputData_formatIsListWithInt() -> None:
    """
    Test Rule 1: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule1 = [
        1, 3, 7, 1, 0, 6, 1, 5, 6, 6,
        3, 6, 3, 2, 3, 2, 2, 10, 1, 5]
    tr = NelsonRules(arr_input_rule1)
    tr.rule1()
    arr_expected_result_rule1 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule1"] == arr_expected_result_rule1).all()


def test_inputData_formatIsListWithString() -> None:
    """
    Test Rule 1: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule1 = [
        "1.22", "3.54", "text", "something", "0.32", "6.59", "1.23", "any", "test", "6.10",
        "1.22", "3.54", "text", "something", "0.32", "6.59", "1.23", "any", "test", "6.10"]
    try:
        tr = NelsonRules(arr_input_rule1)
        raise Exception("Test is excepting the module to raise an exception!")
    except Exception as e:
        if str(e) == "Please provide 1D numpy array as input data!":
            pass
        else:
            raise Exception("Unknown exception raised: " + str(e))


def test_inputData_formatIsPandasSeriesWithFloat() -> None:
    """
    Test Rule 1: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule1 = pd.Series([
        1.22, 3.54, 7.80, 1.16, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, 1.22, 5.00])
    tr = NelsonRules(arr_input_rule1)
    tr.rule1()
    arr_expected_result_rule1 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule1"] == arr_expected_result_rule1).all()


def test_inputData_formatIsPandasSeriesWithInt() -> None:
    """
    Test Rule 1: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule1 = pd.Series([
        1, 3, 7, 1, 0, 6, 1, 5, 6, 6,
        3, 6, 3, 2, 3, 2, 2, 10, 1, 5])
    tr = NelsonRules(arr_input_rule1)
    tr.rule1()
    arr_expected_result_rule1 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule1"] == arr_expected_result_rule1).all()


def test_inputData_formatIsPandasSeriesWithString() -> None:
    """
    Test Rule 1: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule1 = pd.Series([
        "1.22", "3.54", "text", "something", "0.32", "6.59", "1.23", "any", "test", "6.10",
        "1.22", "3.54", "text", "something", "0.32", "6.59", "1.23", "any", "test", "6.10"])
    try:
        tr = NelsonRules(arr_input_rule1)
        raise Exception("Test is excepting the module to raise an exception!")
    except Exception as e:
        if str(e) == "Please provide 1D numpy array as input data!":
            pass
        else:
            raise Exception("Unknown exception raised: " + str(e))


##### NANs in input data ##########################################################

def test_rule1_withNANs_nothing_conspicuous() -> None:
    """
    Test Rule 1: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule1 = np.array([
        1.22, 3.54, 7.80, np.nan, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, np.nan, 5.00])
    tr = NelsonRules(arr_input_rule1)
    tr.rule1()
    arr_expected_result_rule1 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule1"] == arr_expected_result_rule1).all()

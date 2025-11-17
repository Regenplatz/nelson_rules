__author__ = "Regenplatz"
__version__ = "1.0.0"


import numpy as np
from nelson_rules import NelsonRules
import pytest


##### RULE 1 #####################################################################

def test_rule1_nothing_conspicuous() -> None:
    """
    Test Rule 1: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule1 = np.array([
        1.22, 3.54, 7.80, 1.16, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, 1.22, 5.00])
    tr = NelsonRules(arr_input_rule1)
    tr.rule1()
    arr_expected_result_rule1 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule1"] == arr_expected_result_rule1).all()


def test_rule1_out_of_control() -> None:
    """
    Test Rule 1: Out-Of-Control.
    :return: Not applicable
    """
    arr_input_rule1 = np.array([
        1.22, 3.54, 4.20, 1.16, 0.32, 11.30, 1.23, 5.44, 5.50, 6.10,
        2.90, 1.00, 3.37, 1.50, 2.90, 1.66, 2.23, 4.50, 1.22, 5.00])
    tr = NelsonRules(arr_input_rule1)
    tr.rule1()
    arr_expected_result_rule1 = np.array([
        0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule1"] == arr_expected_result_rule1).all()


##### RULE 2 #####################################################################

def test_rule2_nothing_conspicuous() -> None:
    """
    Test Rule 2: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule2 = np.array([
        1.22, 3.54, 7.80, 1.10, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, 1.22, 5.00])
    tr = NelsonRules(arr_input_rule2)
    tr.rule2()
    arr_expected_result_rule2 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule2"] == arr_expected_result_rule2).all()


def test_rule2_out_of_control() -> None:
    """
    Test Rule 2: Out-Of-Control.
    :return: Not applicable
    """
    arr_input_rule2 = np.array([
        0.90, 0.87, 0.92, 0.95, 0.97, 0.87, 0.89, 0.90, 0.91, 0.89,
        3.10, 3.12, 5.20, 0.95, 4.12, 3.98, 3.97, 3.50, 3.29, 3.90])
    tr = NelsonRules(arr_input_rule2)
    tr.rule2()
    arr_expected_result_rule2 = np.array([
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule2"] == arr_expected_result_rule2).all()


##### RULE 3 #####################################################################

def test_rule3_nothing_conspicuous() -> None:
    """
    Test Rule 3: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule3 = np.array([
        1.22, 3.54, 7.80, 1.10, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, 1.22, 5.00])
    tr = NelsonRules(arr_input_rule3)
    tr.rule3()
    arr_expected_result_rule3 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule3"] == arr_expected_result_rule3).all()


def test_rule3_out_of_control() -> None:
    """
    Test Rule 3: Out-Of-Control.
    :return: Not applicable
    """
    arr_input_rule3 = np.array([
        1.20, 1.22, 1.23, 1.30, 1.33, 1.37, 1.40, 0.90, 1.01, 1.05,
        0.98, 1.33, 1.31, 1.30, 1.27, 1.25, 1.22, 1.19, 1.17, 1.30])
    tr = NelsonRules(arr_input_rule3)
    tr.rule3()
    arr_expected_result_rule3 = np.array([
        1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 1, 1, 1, 0
    ])
    assert (tr.d_results["rule3"] == arr_expected_result_rule3).all()



##### RULE 4 #####################################################################

def test_rule4_nothing_conspicuous() -> None:
    """
    Test Rule 4: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule4 = np.array([
        1.22, 3.54, 7.80, 1.10, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, 1.22, 5.00])
    tr = NelsonRules(arr_input_rule4)
    tr.rule4()
    arr_expected_result_rule4 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule4"] == arr_expected_result_rule4).all()


def test_rule4_out_of_control() -> None:
    """
    Test Rule 4: Out-Of-Control.
    :return: Not applicable
    """
    arr_input_rule4 = np.array([
        5.00, 1.20, 7.20, 1.03, 8.28, 0.98, 8.46, 0.87, 8.73, 0.82,
        8.89, 0.76, 8.99, 0.72, 9.04, 6.20, 3.40, 3.91, 0.98, 1.30])
    tr = NelsonRules(arr_input_rule4)
    tr.rule4()
    arr_expected_result_rule4 = np.array([
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule4"] == arr_expected_result_rule4).all()


##### RULE 5 #####################################################################

def test_rule5_nothing_conspicuous() -> None:
    """
    Test Rule 5: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule5 = np.array([
        1.22, 3.54, 7.80, 1.10, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, 1.22, 5.00])
    tr = NelsonRules(arr_input_rule5)
    tr.rule5()
    arr_expected_result_rule5 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule5_points"] == arr_expected_result_rule5).all()


def test_rule5_nothing_conspicuous_windows() -> None:
    """
    Test Rule 5: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule5 = np.array([
        1.22, 3.54, 7.80, 1.10, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, 1.22, 5.00])
    tr = NelsonRules(arr_input_rule5)
    tr.rule5()
    arr_expected_result_rule5_windows = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule5_windows"] == arr_expected_result_rule5_windows).all()


def test_rule5_out_of_control() -> None:
    """
    Test Rule 5: Out-Of-Control.
    :return: Not applicable
    """
    arr_input_rule5 = np.array([
        1.22, 3.54, 4.10, 1.10, 0.32, 3.72, 1.23, 6.30, 6.40, 3.60,
        2.90, 3.90, 3.37, 1.50, 2.90, 1.66, 2.23, 3.30, 1.22, 4.20])
    tr = NelsonRules(arr_input_rule5)
    tr.rule5()
    arr_expected_result_rule5_points = np.array([
        0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule5_points"] == arr_expected_result_rule5_points).all()


def test_rule5_out_of_control_windows() -> None:
    """
    Test Rule 5: Out-Of-Control.
    :return: Not applicable
    """
    arr_input_rule5 = np.array([
        1.22, 3.54, 4.10, 1.10, 0.32, 3.72, 1.23, 6.30, 6.40, 3.60,
        2.90, 3.90, 3.37, 1.50, 2.90, 1.66, 2.23, 3.30, 1.22, 4.20])
    tr = NelsonRules(arr_input_rule5)
    tr.rule5()
    arr_expected_result_rule5_windows = np.array([
        0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule5_windows"] == arr_expected_result_rule5_windows).all()


##### RULE 6 #####################################################################

def test_rule6_nothing_conspicuous() -> None:
    """
    Test Rule 6: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule6 = np.array([
        4.92, 4.31, 4.60, 4.38, 4.48, 4.93, 4.60, 4.35, 5.02, 4.70,
        4.57, 4.97, 4.32, 4.90, 4.99, 4.24, 4.50, 4.69, 4.36, 4.65])
    tr = NelsonRules(arr_input_rule6)
    tr.rule6()
    arr_expected_result_rule6 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule6_points"] == arr_expected_result_rule6).all()

def test_rule6_nothing_conspicuous_windows() -> None:
    """
    Test Rule 6: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule6 = np.array([
        4.92, 4.31, 4.60, 4.38, 4.48, 4.93, 4.60, 4.35, 5.02, 4.70,
        4.57, 4.97, 4.32, 4.90, 4.99, 4.24, 4.50, 4.69, 4.36, 4.65])
    tr = NelsonRules(arr_input_rule6)
    tr.rule6()
    arr_expected_result_rule6_windows = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule6_windows"] == arr_expected_result_rule6_windows).all()


def test_rule6_out_of_control() -> None:
    """
    Test Rule 6: Out-Of-Control.
    :return: Not applicable
    """
    arr_input_rule6 = np.array([
        1.22, 3.54, 4.10, 4.25, 4.30, 4.20, 1.23, 1.30, 1.01, 3.60,
        2.90, 3.90, 3.37, 1.50, 2.90, 1.66, 2.23, 3.30, 1.22, 4.20])
    tr = NelsonRules(arr_input_rule6)
    tr.rule6()
    arr_expected_result_rule6 = np.array([
        0, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule6_points"] == arr_expected_result_rule6).all()


def test_rule6_out_of_control_windows() -> None:
    """
    Test Rule 6: Out-Of-Control.
    :return: Not applicable
    """
    arr_input_rule6 = np.array([
        1.22, 3.54, 4.10, 4.25, 4.30, 4.20, 1.23, 1.30, 1.01, 3.60,
        2.90, 3.90, 3.37, 1.50, 2.90, 1.66, 2.23, 3.30, 1.22, 4.20])
    tr = NelsonRules(arr_input_rule6)
    tr.rule6()
    arr_expected_result_rule6_windows = np.array([
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule6_windows"] == arr_expected_result_rule6_windows).all()


##### RULE 7 #####################################################################

def test_rule7_nothing_conspicuous() -> None:
    """
    Test Rule 7: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule7 = np.array([
        1.22, 3.54, 7.80, 1.10, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, 1.22, 5.00])
    tr = NelsonRules(arr_input_rule7)
    tr.rule7()
    arr_expected_result_rule7 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule7"] == arr_expected_result_rule7).all()


def test_rule7_out_of_control() -> None:
    """
    Test Rule 7: Out-Of-Control.
    :return: Not applicable
    """
    arr_input_rule7 = np.array([
        7.40, 6.90, 7.10, 2.40, 2.66, 2.50, 7.10, 2.60, 7.20, 2.60,
        7.10, 6.50, 6.90, 7.10, 7.20, 1.90, 2.88, 0.30, 1.90, 7.90])
    tr = NelsonRules(arr_input_rule7)
    tr.rule7()
    arr_expected_result_rule7 = np.array([
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule7"] == arr_expected_result_rule7).all()


##### RULE 8 #####################################################################

def test_rule8_nothing_conspicuous() -> None:
    """
    Test Rule 8: Nothing conspicuous recognizable.
    :return: Not applicable
    """
    arr_input_rule8 = np.array([
        1.22, 3.54, 7.80, 1.10, 0.32, 6.59, 1.23, 5.44, 5.50, 6.10,
        2.90, 6.00, 3.37, 1.50, 2.90, 1.66, 2.23, 9.80, 1.22, 5.00])
    tr = NelsonRules(arr_input_rule8)
    tr.rule8()
    arr_expected_result_rule8 = np.array([
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule8"] == arr_expected_result_rule8).all()


def test_rule8_out_of_control() -> None:
    """
    Test Rule 8: Out-Of-Control.
    :return: Not applicable
    """
    arr_input_rule8 = np.array([
        4.32, 5.21, 4.01, 5.03, 9.22, 10.21, 0.11, 0.02, 10.15, 0.30,
        8.30, 0.21, 4.32, 4.00, 4.87, 4.12, 5.01, 5.12, 4.96, 4.44])
    tr = NelsonRules(arr_input_rule8)
    tr.rule8()
    arr_expected_result_rule8 = np.array([
        0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
        1, 1, 0, 0, 0, 0, 0, 0, 0, 0
    ])
    assert (tr.d_results["rule8"] == arr_expected_result_rule8).all()


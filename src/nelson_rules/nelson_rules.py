
import numpy as np
import pandas as pd
from typing import Dict, Union


d_rules = {
    "rule1": {"f_std": 3.0},
    "rule2": {"i_points": 9},
    "rule3": {"i_points": 6},
    "rule4": {"i_points": 14},
    "rule5": {"i_points": 3, "i_points_window": 2, "f_std": 2.0},
    "rule6": {"i_points": 5, "i_points_window": 4, "f_std": 1.0},
    "rule7": {"i_points": 15, "f_std": 1.0},
    "rule8": {"i_points": 8, "f_std": 1.0},
}


class NelsonRules:

    def __init__(self, arr: np.ndarray, d_rule_settings: Dict[str, Dict[str, Union[float, int]]] = d_rules) -> None:

        if isinstance(arr, np.ndarray):
            self.arr: np.ndarray = arr

        elif isinstance(arr, list):
            if (all(isinstance(x, float) for x in arr)) or (all(isinstance(x, int) for x in arr)):
                self.arr: np.ndarray = np.array(arr)
            elif (isinstance(x, str) for x in arr):
                raise Exception("Please provide 1D numpy array as input data!")

        elif isinstance(arr, pd.Series):
            if (all(isinstance(x, float) for x in arr)) or (all(isinstance(x, int) for x in arr)):
                self.arr: np.ndarray = arr.to_numpy(arr)
            elif (isinstance(x, str) for x in arr):
                raise Exception("Please provide 1D numpy array as input data!")

        self.arr_length: int = self.arr.shape[0]
        self.f_mean = np.mean(self.arr)
        self.f_std = np.std(self.arr)
        self.d_results = {"input_data": self.arr}

        self.d_rules = d_rules
        if (self.d_rules != d_rule_settings) and (len(d_rule_settings) != 0):
            self.d_rules.update(d_rule_settings)


    def _check_if_point_outof_std(self, x, f_std_value: float) -> np.array:
        """
        Check if data point (x) is out of n standard deviations (f_std_value).
        :param x: value to be checked
        :param f_std_value: float, number of standard deviations, e.g. 3.0 for 3 std
        :return: array containing classification info.
        """
        if x < (self.f_mean - (f_std_value * self.f_std)):
            return 1
        elif x > (self.f_mean + (f_std_value * self.f_std)):
            return 1
        else:
            return 0


    def _evaluate_zscore(self, x):
        """
        Evaluate z-score: How far is a data point away from the mean?
        :param x: value to be checked
        :return: z-score
        """
        return (x - self.f_mean) / self.f_std


    def _check_direction_comparedTo_mean(self) -> np.array:
        """
        Check direction of points related to the mean value.
        :return: array containing classification info.
        """
        arr_directions = np.zeros(self.arr_length, dtype=int)
        for i in range(self.arr_length):
            if self.arr[i] < self.f_mean:
                arr_directions[i] = -1
            elif self.arr[i] > self.f_mean:
                arr_directions[i] = 1
        return arr_directions


    def _check_direction_comparedTo_previousValue(self) -> np.array:
        """
        Check direction of points related to the previous value.
        :return: array containing classification info.
        """
        arr_directions = np.zeros(self.arr_length, dtype=int)
        for i in range(1, self.arr_length):

                ## decreasing
                if self.arr[i] < self.arr[i - 1]:
                    arr_directions[i] = -1

                ## increasing
                elif self.arr[i] > self.arr[i - 1]:
                    arr_directions[i] = 1

        return arr_directions


    def _check_direction_and_if_outof_std(self, i_points_window: int, i_points_out: int, f_std_value: float) -> np.array:
        """
        This function relates to Rule 05 and Rule 06.
        e.g. Check if 2 out of 3 elements in a row are more than 2 std away from the mean in the same direction.
        :param i_points_window: int, number of points for window of interest, e.g. 3 in "2 out of 3 points in a row"
        :param i_points_out: int, number of points within this window that fulfill a certain condition,
                e.g. 2 in "2 out of 3 points in a row"
        :param f_std_value: float, number of standard deviations, e.g. 3.0 for 3 std
        :return: array containing classification info.
        """
        arr_directions = self._check_direction_comparedTo_mean()
        vfunc = np.vectorize(self._check_if_point_outof_std, excluded=["f_std_value"])
        arr_outof_std = vfunc(self.arr, f_std_value)
        arr_result_points = np.zeros(self.arr_length, dtype=int)
        arr_result_windows = np.zeros(self.arr_length, dtype=int)
        for i in range(i_points_window, self.arr_length):

            ##### CONDITION 1
            ## convert directions (-1, 0, 1) into True and False
            arr_window = arr_directions[i - i_points_window: i]
            if (arr_window == -1).sum() >= i_points_out:
                arr_cond1 = (arr_window == -1)
            elif (arr_window == 1).sum() >= i_points_out:
                arr_cond1 = (arr_window == 1)
            else:
                arr_cond1 = i_points_window * [False]

            ##### CONDITION 2
            arr_window = arr_outof_std[i - i_points_window: i]
            if (arr_window == 1).sum() >= i_points_out:
                arr_cond2 = (arr_window == 1)

                ## overwrite values
                res_window = arr_cond1 * arr_cond2
                if res_window.sum() >= i_points_out:
                    arr_result_points[i - i_points_window : i] = res_window
                    arr_result_windows[i - i_points_window : i] = i_points_window * [1]

        return arr_result_points, arr_result_windows


    def rule1(self, f_std_value: float = 3.0):
        """
        One point is more than x standard deviations from the mean.
        :param f_std_value: float, number of standard deviations, e.g. 3.0 for 3 std
        :return: array containing classification info.
        """
        vfunc = np.vectorize(self._check_if_point_outof_std, excluded=["f_std_value"])
        arr_result = vfunc(self.arr, f_std_value)
        self.d_results["rule1"] = arr_result


    def rule2(self, i_points: int = 9):
        """
        Number of points (or more) in a row are on the same side of the mean.
        :param i_points: int, minimum number of points to fulfill the condition
        :return: array containing classification info.
        """
        arr_result = np.zeros(self.arr_length, dtype=int)
        arr_directions = self._check_direction_comparedTo_mean()
        for i in range(i_points, self.arr_length + 1):
            arr_window = arr_directions[i - i_points: i]
            if ((arr_window == -1).sum() == i_points) or ((arr_window == 1).sum() == i_points):
                arr_result[i - i_points: i] = 1
        self.d_results["rule2"] = arr_result


    def rule3(self, i_points: int = 6):
        """
        Number of points (or more) in a row are continually increasing (or decreasing).
        :param i_points: int, minimum number of points to fulfill the condition
        :return: array containing classification info.
        """
        arr_result = np.zeros(self.arr_length, dtype=int)
        arr_directions = self._check_direction_comparedTo_previousValue()
        for i in range(i_points, self.arr_length + 1):

            ## first value of array is zero and needs to be updated according to the second value
            if (i == i_points):
                if self.arr[1] < self.arr[0]:
                    arr_directions[0] = -1
                else:
                    arr_directions[0] = 1

            ## result array is being updated
            arr_window = arr_directions[i - i_points: i]
            if (arr_window.sum() == i_points * (-1)) or (arr_window.sum() == i_points):
                arr_result[i - i_points: i] = i_points * [1]

        self.d_results["rule3"] = arr_result


    def rule4(self, i_points: int = 14):
        """
        Number of points in a row alternate in direction, increasing then decreasing.
        :param i_points: int, minimum number of points to fulfill the condition
        :return: array containing classification info.
        """
        res_a = ([-1, 1] * (int(i_points / 2) + 1))[ : i_points]
        res_b = ([1, -1] * (int(i_points / 2) + 1))[ : i_points]
        arr_result = np.zeros(self.arr_length, dtype=int)
        arr_directions = self._check_direction_comparedTo_previousValue()
        for i in range(i_points, self.arr_length + 1):

            ## first value of array is zero and needs to be updated according to the second value
            if (i == i_points):
                if self.arr[1] < self.arr[0]:
                    arr_directions[0] = 1
                else:
                    arr_directions[0] = -1

            ## result array is being updated
            arr_window = arr_directions[i - i_points: i]
            if np.array_equal(arr_window, res_a) or np.array_equal(arr_window, res_b):
                arr_result[i - i_points: i] = i_points * [1]

        self.d_results["rule4"] = arr_result


    def rule5(self, i_points_window: int = 3, i_points_out: int = 2, f_std_value: float = 2.0):
        """
        Check if 2 out of 3 elements in a row are more than 2 std away from the mean in the same direction.
        :param i_points_window: int, number of points for window of interest, e.g. 3 in "2 out of 3 points in a row"
        :param i_points_out: int, number of points within this window that fulfill a certain condition,
                e.g. 2 in "2 out of 3 points in a row"
        :param f_std_value: float, number of standard deviations, e.g. 2.0 for 2 std
        :return: array containing classification info.
        """
        arr_result_points, arr_result_windows = self._check_direction_and_if_outof_std(
            i_points_window=i_points_window, i_points_out=i_points_out, f_std_value=f_std_value)
        self.d_results["rule5_points"] = arr_result_points
        self.d_results["rule5_windows"] = arr_result_windows


    def rule6(self, i_points_window: int = 5, i_points_out: int = 4, f_std_value: float = 1.0):
        """
        check if 4 out of 5 elements in a row are more than 1 std away from the mean in the same direction.
        :param i_points_window: int, number of points for window of interest, e.g. 5 in "4 out of 5 points in a row"
        :param i_points_out: int, number of points within this window that fulfill a certain condition,
                e.g. 4 in "4 out of 5 points in a row"
        :param f_std_value: float, number of standard deviations, e.g. 2.0 for 2 std
        :return: array containing classification info.
        """
        arr_result_points, arr_result_windows = self._check_direction_and_if_outof_std(
            i_points_window=i_points_window, i_points_out=i_points_out, f_std_value=f_std_value)
        self.d_results["rule6_points"] = arr_result_points
        self.d_results["rule6_windows"] = arr_result_windows


    def rule7(self, i_points: int = 15, f_std_value: float = 1.0):
        """
        Number of points in a row (e.g. 15) are within 1 std of the mean on either side of the mean.
        :param i_points: int, minimum number of points to fulfill the condition
        :param f_std_value: float, number of standard deviations, e.g. 2 for 2 std
        :return: array containing classification info.
        """
        arr_directions = self._check_direction_comparedTo_mean()
        vfunc = np.vectorize(self._check_if_point_outof_std, excluded=["f_std_value"])
        arr_outof_std = vfunc(self.arr, f_std_value)
        arr_within_std = ~arr_outof_std + 2
        arr_result = np.zeros(self.arr_length, dtype=int)
        for i in range(i_points, self.arr_length + 1):
            condition_1 = (arr_directions[i - i_points: i] == -1).sum() >= 1 and \
                          (arr_directions[i - i_points: i] == 1).sum() >= 1
            condition_2 = (arr_within_std[i - i_points: i] == 1).sum() == i_points
            if condition_1 and condition_2:
                arr_result[i - i_points : i] = i_points * [1]
        self.d_results["rule7"] = arr_result


    def rule8(self, i_points: int = 8, f_std_value: float = 1):
        """
        Number of points in a row (e.g. 8) exist but none within x standard deviations of the mean,
        and the points are in both directions from the mean.
        :param i_points: int, minimum number of points to fulfill the condition
        :param f_std_value: float, number of standard deviations, e.g. 2.0 for 2 std
        :return: array containing classification info.
        """
        arr_directions = self._check_direction_comparedTo_mean()
        vfunc = np.vectorize(self._check_if_point_outof_std, excluded=["f_std_value"])
        arr_outof_std = vfunc(self.arr, f_std_value)
        arr_result = np.zeros(self.arr_length, dtype=int)
        for i in range(i_points, self.arr_length):
            condition_1 = np.count_nonzero(arr_directions[i - i_points : i] == 1) > 0
            condition_2 = np.count_nonzero(arr_directions[i - i_points : i] == -1) > 0
            condition_3 = arr_outof_std[i - i_points : i].sum() == i_points
            if condition_1 and condition_2 and condition_3:
                arr_result[i - i_points : i] = i_points * [1]
        self.d_results["rule8"] = arr_result


    def apply_rules(self) -> Dict[str, np.array]:
        """
        Apply all rules and load results to result dictionary.
        :return: result dictionary.
        """
        ## evaluate z score for each value
        vfunc = np.vectorize(self._evaluate_zscore)
        arr_result = vfunc(self.arr)
        self.d_results["zscore"] = arr_result

        ## apply rules
        self.rule1(f_std_value=self.d_rules["rule1"]["f_std"])
        self.rule2(i_points=self.d_rules["rule2"]["i_points"])
        self.rule3(i_points=self.d_rules["rule3"]["i_points"])
        self.rule4(i_points=self.d_rules["rule4"]["i_points"])
        self.rule5(i_points_out=self.d_rules["rule5"]["i_points"],
                   i_points_window=self.d_rules["rule5"]["i_points_window"],
                   f_std_value=self.d_rules["rule5"]["f_std"])
        self.rule6(i_points_out=self.d_rules["rule6"]["i_points"],
                   i_points_window=self.d_rules["rule6"]["i_points_window"],
                   f_std_value=self.d_rules["rule6"]["f_std"])
        self.rule7(i_points=self.d_rules["rule7"]["i_points"],
                   f_std_value=self.d_rules["rule7"]["f_std"])
        self.rule8(i_points=self.d_rules["rule8"]["i_points"],
                   f_std_value=self.d_rules["rule8"]["f_std"])

        return self.d_results

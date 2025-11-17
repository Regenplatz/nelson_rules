# nelson_rules

<a href=https://img.shields.io/badge/python-3.12-blue>
    <img src=https://img.shields.io/badge/python-3.12-blue?logo=python alt="Python 3.12">
</a>

<a href=https://img.shields.io/badge/NumPy-green>
    <img src=https://img.shields.io/badge/NumPy-blue?logo=NumPy alt="Python 3.12">
</a>




<br>
<br>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#background">Background</a></li>
    <li><a href="#about-the-package">About the package</a></li>   
    <li><a href="#how-to-install">How to install</a></li>
    <li><a href="#how-to-run-with-default-settings">How to run with default settings</a></li>
    <li><a href="#how-to-run-with-other-settings">How to run with other settings</a></li>    
    <li><a href="#how-to-access-results">How to access results</a></li>
  </ol>
</details>

<br>


<!-- ABOUT THE PROJECT -->
## Background

The 8 Nelson rules can be used in **process control** to detect **potential 
anomalies** during production. Those rules were defined by 
[Lloyd S. Nelson][L.S. Nelson, Journal of Quality Technology, 16, 4, 1984] 
in the 1980s. The rules and their exemplary visualizations are also available on 
[wikipedia][wikipedia-url].

<br>

## About the package

The package was built with [Numpy](https://numpy.org/) and tested with 
[pytest](https://docs.pytest.org/en/stable/).

By the use of this package, your data is checked for all 8 rules. 
As input data, a 1D NumPy Array is preferred, but a list of numeric values is
also possible. As result, a dictionary is provided, that contains numpy arrays
as values for each rule. It furthermore contains the *input data*, as
well as *zscores*.

Results on Nelson rules are available as binary (0, 1) 1D arrays. 
Zscores are available as float values.

<br>

## How to install
TODO

<br>

## How to run with default settings

*Default settings* refer to the values that are stated in the rules above.
E.g. for rule 1, we'd check if at least one point is more than 3 
standard deviations from the mean. The default values are encoded as follows: 
```
d_rule_settings = {
    "rule1": {"f_std": 3.0},
    "rule2": {"i_points": 9},
    "rule3": {"i_points": 6},
    "rule4": {"i_points": 14},
    "rule5": {"i_points": 3, "i_points_window": 2, "f_std": 2.0},
    "rule6": {"i_points": 5, "i_points_window": 4, "f_std": 1.0},
    "rule7": {"i_points": 15, "f_std": 1.0},
    "rule8": {"i_points": 8, "f_std": 1.0},
}
```

To check for data points following Nelson rules, the *rule setting 
dictionary* is not needed as a parameter, because it is already set as 
default. Therefore, simply run the following on your data: 
```
tr = NelsonRules(<your_data_in_1D_numpy_array>)
d_results = tr.apply_rules(d_rules)
```

The program is set up with [NumPy][NumPy-url]. However, if you'd 
like to get the results in a [pandas][pandas-url] DataFrame, run:
```
df = pd.DataFrame(data=d_results)
```

<br>

## How to run with other settings

In case you'd like to run the code with other settings, adapt 
*d_rule_settings* and run:
```
tr = NelsonRules(<your_data_in_1D_numpy_array>, d_rule_settings)
d_results = tr.apply_rules(d_rules)
```

<br>

## How to access results

The results are available in a dictionary with the following structure:
```
d_results = {
    "input_data":    [...],
    "zscore":        [...],
    "rule1":         [...],
    "rule2":         [...],
    "rule3":         [...],
    "rule4":         [...],
    "rule5_points":  [...],
    "rule5_windows": [...],
    "rule6_points":  [...],
    "rule6_windows": [...],
    "rule7":         [...],
    "rule8":         [...]
}
```
You could load the dictionary into a pandas DataFrame (as mentioned above).
<br> Or you could access the data of interest like this:
```
d_results["rule4"]
```
For rules 5 and 6, *points* and *windows* are available. By this, you could
visualize both: the n data points out of m points (window) that fulfill 
the rule.



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[L.S. Nelson, Journal of Quality Technology, 16, 4, 1984]: https://www.tandfonline.com/doi/abs/10.1080/00224065.1984.11978921
[wikipedia-url]: https://en.wikipedia.org/wiki/Nelson_rules
[NumPy-logo]: https://numpy.org/images/logo.svg
[NumPy-url]: https://numpy.org/
[pytest-logo]: https://docs.pytest.org/en/stable/_static/pytest1.png
[pytest-url]: https://docs.pytest.org/en
[pandas-url]: https://pandas.pydata.org/

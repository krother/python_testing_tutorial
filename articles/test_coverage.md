
# Test Coverage

For the next exercises, you need to install a small plugin:

    :::bash
    pip install pytest-cov


### Exercise 1: Calculate Test Coverage

Calculate the percentage of code covered by automatic tests:

    :::bash
    pytest --cov=.

Instead of the `.` you can insert the path you would like to see in the coverage report.

Check whether any hidden files have appeared.

### Exercise 2: Identify uncovered lines
Find out which lines are not covered by tests. Execute

    :::bash
    coverage html

Open the resulting file `htmlcov/index.html` in a web browser.

### Exercise 3: Increase test coverage

Write more tests to increase the test coverage of `word_counter.py` to 100%.

### Reflection Questions

* does 100% test coverage mean that the program is free of bugs?
* does 100% test coverage mean that all execution paths in the program have been tested?
* what types of errors is a high test coverage most likely to avoid?

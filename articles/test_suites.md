
# Test Suites

### Exercise 1: Test collection

Run all tests written so far by simply typing

    pytest


### Exercise 2: Options

Try some options of pytest:

    pytest -v  # verbose output

    pytest -lf # re-run failed tests

    pytest -x  # stop on first failing test


### Exercise 3: Fixing tests

Fix the tests in `test_suite.py`


### Exercise 4: Test selection

Run only one test class

    pytest test_suite.py::TestAverageWordLength

or a single test function:

    pytest test_suite.py::TestAverageWordLength::test_average_words

Your task is to run only the function **test_word_counter.test_simple** from the test suite in **tests/**.

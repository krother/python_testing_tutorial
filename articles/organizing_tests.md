
# Organizing Tests

### Exercise 1: Test Classes

Structure some of the tests you have written by placing them in a class.
Make sure the name of the class starts with the word `Test`.

Indent your test functions so that they belong to the class.
Add `self` as the first parameter of each function:

    :::python3
    class TestDummy:

        def test_dummy(self):
            assert ...

----

### Exercise 2: Test collection

Run all tests written so far by simply typing

    :::bash
    pytest

----

### Exercise 3: Test selection

Run only one test file:

    :::bash
    pytest FILE_NAME

Run only one test class:

    :::bash
    pytest FILE_NAME::CLASS_NAME

Finally, run a single test:

    :::bash
    pytest FILE_NAME::CLASS_NAME::TEST_NAME

----

### Exercise 4: Options

Find out which options of pytest do the following:

*more verbose output | re-run failing tests | stop on first test that fails*

    :::bash
    pytest -lf
    pytest -v
    pytest -x

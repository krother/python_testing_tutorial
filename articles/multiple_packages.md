### Exercise 5: Import test data in multiple test packages
In a big software project, your tests are distributed to two packages. Both **test_first.py** and **test_second.py** require the variable **MOBYDICK_SUMMARY** from the module **test data.py**. The package structure is like this:

    testss/
        test_a/
            __init__.py
            test_first.py
        test_b/
            __init__.py
            test_second.py
        __init__.py
        test_data.py
        test_all.py

Your task is to make sure that the variable **MOBYDICK_SUMMARY** is correctly imported to both test modules, so that the tests pass for all of:

    tests/test_a/test_first.py
    tests/test_b/test_second.py
    tests/test_all.py


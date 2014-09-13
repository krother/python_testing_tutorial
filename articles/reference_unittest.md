# Introduction to the unittest Framework in Python

unittest is a Python framework for writing Unit, Integration, Performance and Acceptance tests. It provides a class TestCase and a main() method.

It is typically imported with:

    from unittest import TestCase, main

### Writing a test class
Test classes should extend TestCase, and contain at least one method starting with test_ that contains assertions. TestCase offers many assertion methods (assertEqual, assertAlmostEqual, assertTrue etc.). Optionally, the methods setUp() and tearDown() can be used to prepare testing and clean up afterwards.

    class AdditionTests(TestCase):
        def test_add(self):
            self.assertEqual(add(3, 4), 7)

### Running the tests
The unittest.main method will look for all classes derived from TestCase that have been defined in imported modules. It runs all tests inside them and reports. Typically, you will find main() called in a separate code block:

    if __name__ == '__main__':
        main()

### Testing command-line scripts
To test a command-line script call it using a shell command and redirect the output for further evaluation:

    import os
    os.system('python myprog.py > out.txt')


You can run Python test files with unittest without calling main()

    python -m unittest test_file

without .py

## discovering tests

    python -m unittest discover

## test data
patch pythonpath in a local test_data that imports ../test_data.*

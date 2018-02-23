# Introduction to the unittest Framework in Python

**unittest** is a Python framework for writing Unit Tests, Integration Tests, and Acceptance Tests. It mainly provides a class **TestCase** and a **main()** method.

**unittest** is typically imported with:

    from unittest import TestCase, main

### Writing a test class
Test classes should extend TestCase, and contain at least one method starting with test_ . Test methods contain assertions.

TestCase offers many assertion methods (assertEqual, assertAlmostEqual, assertTrue etc.).

    class AdditionTests(TestCase):

        def test_add(self):
            self.assertEqual(add(3, 4), 7)

### Running the tests
The **unittest.main** method will look for all classes derived from TestCase that have been imported. It runs all tests inside them and reports.

Typically, you will find main() called in a separate code block:

    if __name__ == '__main__':
        main()

You can run Python test files with unittest without calling main()

    python -m unittest test_file

*Note: The name of the test module is spelled without .py*


### Testing command-line scripts
To test a command-line script call it using a shell command and redirect the output for further evaluation. The simplest way is to use **os.system**:

    import os
    os.system('python myprog.py > out.txt')


### Discovering tests

    python -m unittest discover

### Test data and fixtures
The methods setUp() and tearDown() can be used to prepare testing and clean up afterwards.

#### Importing test data in multiple packages
When you have many tests distributed to sub-packages, you may want to share test data among them. There are two ways to do so:

Either set the PYTHONPATH variable to the directory with your tests.

Alternatively, patch **sys.path** in a local module test_data.py in each of the sub-packages, so that they import ../test_data.*

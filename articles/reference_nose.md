# Testing Python Applications with nose
*"nose extends unittest to make testing easier"*

## Getting started

### Requirements
* Python 2.7

### Installing nose

    sudo easy_install nose

### Documentation
https://nose.readthedocs.org/en/latest/
https://nose.readthedocs.org/en/latest/writing_tests.html

## Assertions in nose

### Same syntax as in **unittest**
The TestCase class works in the same way as with the **unittest** module. You can run your existing tests with nose.

### Test functions without classes
You can write tests without subclassing **TestCase**. You can write tests as simple functions:

    from nose.tools import assert_equal

    def test_example():
        assert_equal(1 + 1, 2)

#### List available assert functions

    import nose.tools
    print dir(nose.tools)


## Running tests

#### Running a single test module

    nosetests only_test_this.py

In contrast to **unittest**, it is no longer neccessary to include a **__main__** block in your test file.

#### Selecting which tests to run

    nosetests test.module
    nosetests another.test:TestCase.test_method
    nosetests a.test:TestCase
    nosetests /path/to/test/file.py:test_function

### Test Detection

#### Running auto-detected tests with nose
    nosetests
    nosetests -v
    nosetests --with-doctest

## Running nose from Python
For instance as part of a setup script

    import nose
    nose.main()

## Which tests does nose detect automatically?
All tests identified by nose have **'test'** or **'Test'** at a word boundary or following a - or _) and lives in a module that also matches that expression will be run as a test.

The test finder examines Python files and directories that match this pattern. Packages in the current directory are always examined.

## Writing a nose configuration file
Create a **.noserc** file in your home directory containing:

    [nosetests]
    verbosity=3
    with-doctest=1

## Calculating test coverage
    sudo easy_install coverage
    nosetests --with-coverage
    nosetests --with-coverage --cover-html
    cd cover
    firefox index.html


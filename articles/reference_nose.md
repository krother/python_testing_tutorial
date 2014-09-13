# Testing Python Applications with nose
*"nose extends unittest to make testing easier"*

https://nose.readthedocs.org/en/latest/
https://nose.readthedocs.org/en/latest/writing_tests.html

## Requirements
* Python 2.7

## Brainstorming
* test collection


## Installing nose
    sudo easy_install nose

## Running tests with nose
    nosetests
    nosetests -v
    nosetests --with-doctest

## Which tests does nose detect automatically?
All tests identified by nose have 'test' or 'Test' at a word boundary or following a - or _) and lives in a module that also matches that expression will be run as a test.

The test finder examines Python files and directories that match this pattern. Packages in the current directory are always examined.

## Selecting which tests to run
    nosetests only_test_this.py
    nosetests test.module
    nosetests another.test:TestCase.test_method
    nosetests a.test:TestCase
    nosetests /path/to/test/file.py:test_function

## Running nose from Python
(e.g. in a setup script)

    import nose
    nose.main()

## Writing a nose configuration file
Create .noserc in your home directory containing:
    [nosetests]
    verbosity=3
    with-doctest=1

## Calculating Test Coverage
    sudo easy_install coverage
    nosetests --with-coverage
    nosetests --with-coverage --cover-html
    cd cover
    firefox index.html

## List all assert functions

    import nose.tools
    print dir(nose.tools)


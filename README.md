# Testing Python Applications with nose
*"nose extends unittest to make testing easier"*

https://nose.readthedocs.org/en/latest/

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

## Assertions in nose.tools
* assert_almost_equal
* assert_almost_equals
* assert_dict_contains_subset
* assert_dict_equal
* assert_equal
* assert_equals
* assert_false
* assert_greater
* assert_greater_equal
* assert_in
* assert_is
* assert_is_instance
* assert_is_none
* assert_is_not
* assert_is_not_none
* assert_items_equal
* assert_less
* assert_less_equal
* assert_list_equal
* assert_multi_line_equal
* assert_not_almost_equal
* assert_not_almost_equals
* assert_not_equal
* assert_not_equals
* assert_not_in
* assert_not_is_instance
* assert_not_regexp_matches
* assert_raises
* assert_raises_regexp
* assert_regexp_matches
* assert_sequence_equal
* assert_set_equal
* assert_true
* assert_tuple_equal

## Assertions in unittest.TestCase
* assertAlmostEqual
* assertAlmostEquals
* assertDictContainsSubset
* assertDictEqual
* assertEqual
* assertEquals
* assertFalse
* assertGreater
* assertGreaterEqual
* assertIn
* assertIs
* assertIsInstance
* assertIsNone
* assertIsNot
* assertIsNotNone
* assertItemsEqual
* assertLess
* assertLessEqual
* assertListEqual
* assertMultiLineEqual
* assertNotAlmostEqual
* assertNotAlmostEquals
* assertNotEqual
* assertNotEquals
* assertNotIn
* assertNotIsInstance
* assertNotRegexpMatches
* assertRaises
* assertRaisesRegexp
* assertRegexpMatches
* assertSequenceEqual
* assertSetEqual
* assertTrue
* assertTupleEqual




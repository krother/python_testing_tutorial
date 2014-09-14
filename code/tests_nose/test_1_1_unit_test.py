#!/usr/bin/env python
#
# Example of a test function with nose
#
# run with:
# nosetests test_1.1_unit_test.py
#

from mobydick import TextBody
from nose.tools import assert_equal

def test_word_number_two():
    """Count words in a short sentence"""
    text = TextBody("Call me Ishmael")
    assert_equal(text.word_number, 3)



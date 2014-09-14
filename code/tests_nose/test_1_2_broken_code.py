#!/usr/bin/env python
#
# Example of test that fails because of broken code.
#

from mobydick import TextBody
from nose.tools import assert_almost_equal

def test_average_word_length():
    """Calculate average word length in a short sentence"""
    text = TextBody("Call me Ishmael")
    assert_almost_equal(text.average_word_length, 4.333, 3)

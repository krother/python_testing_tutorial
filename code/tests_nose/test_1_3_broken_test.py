
#!/usr/bin/env python
#
# Example of test that fails because of a broken test.
#

from mobydick import TextBody
from nose.tools import assert_list_equal


def test_words():
    """The word attribute is a list"""
    words = ['my', 'name', 'is', 'ishmael']
    text = TextBody('Call me Ishmael')
    assert_list_equal(text.words, words)

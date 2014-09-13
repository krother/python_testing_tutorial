#!/usr/bin/env python
#
# Example of test functions with nose
#

from word_counter import TextBody
from nose.tools import assert_equal

MOBYDICK_SUMMARY = open('mobydick_summary.txt').read()

def test_word_number_one():
    """Count single word in a text"""
    text = TextBody("one_word")
    assert text.word_number == 1

def test_word_number_two():
    """Count two words in a text"""
    text = TextBody("two words")
    assert_equal(text.word_number, 2)

def test_word_number_text():
    """Count words in a text paragraph"""
    text = TextBody(MOBYDICK_SUMMARY)
    assert_equal(text.word_number, 54)



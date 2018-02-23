#!/usr/bin/env python
#
# example of an integration test
#

from word_counter import TextBody, WordCounter
from nose.tools import assert_equal

MOBYDICK_SUMMARY = open('mobydick_summary.txt').read()


def test_count_word_simple():
    """Count word in a short text"""
    text = TextBody("the white white whale")
    counter = WordCounter(text)
    assert_equal(counter.count_word("white"), 2)

def test_count_word_complex():
    """Count word in a longer text"""
    text = TextBody(MOBYDICK_SUMMARY)
    counter = WordCounter(text)
    assert_equal(counter.count_word("white"), 2)





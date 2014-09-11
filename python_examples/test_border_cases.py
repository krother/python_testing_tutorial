#!/usr/bin/env python
#
# example of border cases
#

from nose.tools import assert_equal, assert_raises, assert_greater, assert_list_equal
from word_counter import TextBody

def test_empty():
    """Empty input works"""
    text = TextBody('')
    assert_(text.word_number, 0)

def test_wrong_input():
    """Non-string doesn't work"""
    assert_(TypeError, TextBody, 777)
    
def test_smallest():
    """Minimal string works."""
    text = TextBody("whale")
    assert_(text.words, ['whale'])
    
def test_biggest():
    """An entire book works."""
    text = TextBody(open('moby_dick.txt').read())
    assert_(text.word_number, 200000)

def test_sanity():
    """Feed output of a class into itself"""
    text_a = TextBody(open('moby_dick.txt').read())
    words_before = text_a.words[:]
    copy = ' '.join(text_a.words)
    text_b = TextBody(copy)
    assert_(words_before, text_b.words)

def test_nasty():
    """Ugly data example works."""
    text = TextBody("That #~&%* program still doesn't work!\nI already de-bugged it 3 times, and still numpy.array keeps throwing AttributeErrors. What should I do?")
    assert_(text.word_number, 22)



#!/usr/bin/env python
#
# example of a test generator
#

from nose.tools import assert_equal
from word_counter import TextBody, WordCounter

MOBYDICK_SUMMARY = open('mobydick_summary.txt').read()
TEXT = TextBody(MOBYDICK_SUMMARY)
COUNTER = WordCounter(TEXT)

WORD_PAIRS = [
    ('months', 1),
    ('whale', 5),
    ('captain', 4),
    ('white', 2),
    ('harpoon', 1),
    ('Ahab', 1)
    ]

def check_word(word, number):
    assert_equal(COUNTER.count_word(word), number)

def test_word_pairs():
    # Tests a series of example words
    # creates one test for each word
    # --- no docstring so that parameters are visible ---
    for word, number in WORD_PAIRS:
        yield check_word, word, number

# nose does
for x, y, z in test_word_pairs:
    if x(y, z):
        ok()
    else:
        fail()





#!/usr/bin/env python
#
# example of a test with a mock object
#

from unittest import main, TestCase
from word_counter import WordCounter

MOBYDICK_SUMMARY = open('mobydick_summary.txt').read()

class MockText:
    words = ['the', 'white', 'white', 'whale']
    word_number = 4


class WordCounterTests(TestCase):

    def test_count_word_simple(self):
        """Count a single word"""
        counter = WordCounter(MockText)
        self.assertEqual(counter.count_word("white"), 2)






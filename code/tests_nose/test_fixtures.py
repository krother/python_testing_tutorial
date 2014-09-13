#!/usr/bin/env python
#
# example of tests with fixtures
#

from unittest import main, TestCase
from word_counter import TextBody, WordCounter


class WordCounterFixtureTests(TestCase):

    def setUp(self):
        """Prepare before each test"""
        MOBYDICK_SUMMARY = open('mobydick_summary.txt').read()
        self.text = TextBody(MOBYDICK_SUMMARY)
        self.counter = WordCounter(self.text)

    def test_count_months(self):
        self.assertEqual(self.counter.count_word("months"), 1)

    def test_count_the(self):
        """Count word in a longer text"""
        self.assertEqual(self.counter.count_word("the"), 6)

    def tearDown(self):
        """Clean up after a test has passed or failed."""
        pass





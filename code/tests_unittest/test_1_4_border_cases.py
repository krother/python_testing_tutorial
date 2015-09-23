#!/usr/bin/env python
"""
Example of border cases

TASK: insert the following assert_functions, so that each of them 
is used at least once:

    assertEqual, assertRaises, assertGreater, assertList_equal

"""

from mobydick import TextBody
from unittest import TestCase, main


class BorderCaseTests(TestCase):

    def test_empty(self):
        """Empty input works"""
        text = TextBody('')
        self.assert_x(text.word_number, 0)

    def test_smallest(self):
        """Minimal string works."""
        text = TextBody("whale")
        self.assert_x(text.words, ['whale'])
        
    def test_typical(self):
        """Representative small input works."""
        text = TextBody("whale eats captain")
        self.assert_x(text.words, ['whale', 'eats', 'captain'])

    def test_wrong_input(self):
        """Non-string doesn't work"""
        self.assert_x(TypeError, TextBody, 777)

    def test_biggest(self):
        """An entire book works."""
        text = TextBody(open('moby_dick.txt').read())
        self.assert_x(text.word_number, 200000)

    def test_sanity(self):
        """Feed output of a class into itself"""
        text_a = TextBody(open('moby_dick.txt').read())
        words_before = text_a.words[:]
        copy = ' '.join(text_a.words)
        text_b = TextBody(copy)
        self.assert_x(words_before, text_b.words)

    def test_nasty(self):
        """Ugly data example works."""
        text = TextBody("""That #~&%* program still doesn't work!
    I already de-bugged it 3 times, and still numpy.array keeps throwing AttributeErrors.
    What should I do?""")
        self.assert_x(text.word_number, 22)


if __name__ == '__main__':
    main()


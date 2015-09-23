#!/usr/bin/env python
"""
Example of a Unit Test
"""

from mobydick import TextBody
from unittest import TestCase, main

class MobyDickUnitTest(TestCase):

    def test_word_number_two(self):
        """Count words in a short sentence"""
        text = TextBody("Call me Ishmael")
        self.assertEqual(text.word_number, 3)


if __name__ == '__main__':
    main()


#!/usr/bin/env python
"""
Example of test that fails because of broken code.
"""

from mobydick import TextBody
from unittest import TestCase, main

class MobyDickBrokenCode(TestCase):

    def test_average_word_length(self):
        """Calculate average word length in a short sentence"""
        text = TextBody("Call me Ishmael")
        self.assertAlmostEqual(text.average_word_length, 4.333, 3)


if __name__ == '__main__':
    main()


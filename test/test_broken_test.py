
#!/usr/bin/env python
"""
Example of test that fails because of a broken test.
"""

from mobydick import TextBody
from unittest import TestCase, main

class MobyDickBrokenTest(TestCase):

    def test_words(self):
        """The word attribute is a list"""
        words = ['my', 'name', 'is', 'ishmael']
        text = TextBody('Call me Ishmael')
        self.assertListEqual(text.words, words)


if __name__ == '__main__':
    main()


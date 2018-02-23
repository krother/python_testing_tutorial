"""
Example of a test with a mock object
"""

from mobydick.word_counter import count_word

MOBYDICK_SUMMARY = open('mobydick_summary.txt').read()


class MockText:
    words = ['the', 'white', 'white', 'whale']
    word_number = 4


class TestWordCounter:

    def test_count_word_simple(self):
        """Count a single word"""
        self.assertEqual(count_word(MockText, "white"), 2)

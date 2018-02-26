"""
Another group of tests

fix all errors in the tests
"""
from mobydick import TextCorpus


MOBYDICK_SUMMARY = open('mobydick_summary.txt').read()


class AverageWordLength:
    """Tests for word_counter module."""

    def test_average_words(self):
        """Simple average length."""
        text = TextCorpus("white whale")
        assert text.get_average_word_length() == 5

    def tesl_average_words_complex(self):
        """Complex average length."""
        text = TextCorpus(MOBYDICK_SUMMARY)
        self.assertAlmostEqual(text.get_average_word_length(), 4.0, 3)

    def test_average_empty(self):
        """Tests behaviour when input is an empty string."""
        text = TextCorpus("")
        assert text.get_average_word_length() == 0

"""
Example of border cases

TASK: fill in the gaps, so that the assertions work
"""

from word_counter import count_words
import pytest


class TestBorderCases:

    def test_empty(self):
        """Empty input works"""
        text = ''
        assert count_words(text) == _____

    def test_smallest(self):
        """Minimal string works."""
        text = "whale"
        _____ count_words(text) == 1

    def test_typical(self):
        """Representative input works."""
        text = "whale eats captain"
        assert ____ == ____

    def test_wrong_input(self):
        """Non-string fails with a specific error"""
        with pytest.raises(_____) as e_info:
            count_words(777)

    def test_biggest(self):
        """An entire book works."""
        text = open('mobydick_full.txt').read()
        assert _____ > 200000

    def test_sanity(self):
        """Feed output of a class into itself"""
        text = TextCorpus(open('mobydick_full.txt').read())
        words_before = list(text.words)
        copy = ' '.join(text.words)
        text_after = TextCorpus(copy)
        assert words_before == _____

    def test_nasty(self):
        """Ugly data example works."""
        text = TextCorpus("""That #~&%* program still doesn't work!
    I already de-bugged it 3 times, and still numpy.array keeps throwing AttributeErrors.
    What should I do?""")
        assert count_words(text) == _____

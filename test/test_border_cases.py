"""
Example of border cases

TASK: fill in the gaps, so that the assertions work
"""

from mobydick import TextCorpus
import pytest


class TestBorderCases:

    def test_empty(self):
        """Empty input works"""
        text = TextCorpus('')
        assert text.n_words == _____

    def test_smallest(self):
        """Minimal string works."""
        text = TextCorpus("whale")
        _____ text.words == ['whale']
        
    def test_typical(self):
        """Representative small input works."""
        text = TextCorpus("whale eats captain")
        assert text.words == [_____, 'eats', 'captain']

    def test_wrong_input(self):
        """Non-string doesn't work"""
        with pytest.raises(_____) as e_info:
            TextCorpus(777)

    def test_biggest(self):
        """An entire book works."""
        text = TextCorpus(open('mobydick_full.txt').read())
        assert text._____ > 200000

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
        assert text.n_words == _____

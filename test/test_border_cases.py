"""
Examples of border cases

TASK: fill in the gaps, so that all tests pass
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
        assert ____ == ____

    def test_typical(self):
        """Representative input works."""
        text = "whale eats captain"
        assert ____

    def test_wrong_input(self):
        """Non-string fails with a specific error"""
        with pytest.raises(_____) as e_info:
            count_words(777)

    def test_biggest(self):
        """An entire book works."""
        text = open('____mobydick_full.txt').read()
        assert count_words(text) > 200000

    def test_nasty(self):
        text = """you haint no objections to sharing a harpooneer's blanket,
have ye? I s'pose you are goin' a-whalin',
so you'd better get used to that sort of thing."""
        assert count_words(text) == _____

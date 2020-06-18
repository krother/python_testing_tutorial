"""
Example of test that fails because of a broken test.
"""

from word_counter import TextCorpus


class TestMobyDickBrokenTest:

    def test_words(self):
        """The word attribute is a list"""
        words = ['my', 'name', 'is', 'ishmael']
        text = TextCorpus('Call me Ishmael')
        assert text.words == words

"""
Example of test that fails because of broken code.
"""

from mobydick import TextCorpus


class TestMobyDickBrokenCode:

    def test_average_word_length(self):
        """Calculate average word length in a short sentence"""
        text = TextCorpus("Call me Ishmael")
        assert round(text.average_word_length, 3) == 4.333

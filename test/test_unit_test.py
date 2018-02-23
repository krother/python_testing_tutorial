"""
Example of a Unit Test
"""

from mobydick import TextCorpus


class TestMobyDick:

    def test_word_number(self):
        """Count words in a short sentence"""
        text = TextCorpus("Call me Ishmael")
        assert text.n_words == 3

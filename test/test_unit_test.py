"""
Example of a Unit Test
"""

from mobydick.word_counter import count_words


class TestMobyDick:

    def test_count_words(self):
        """Count words in a short sentence"""
        n = count_words("Call me Ishmael")
        assert n == 3

"""
Example of test that fails because of broken code.
"""

from word_counter import count_words


def test_count_words_broken(self):
        """a test that fails because the code is broken"""
        text = "I s'pose you are goin' a-whalin'"
        assert round(text.average_word_length, 3) == 4.333

"""
Example of test that fails because of broken code.
"""

from mobydick.word_counter import count_words


def test_count_words_tabs():
    """words are separated by tabs as well"""
    n = count_words("the\twhite\thale")
    assert n == 3

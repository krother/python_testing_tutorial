"""
Example of test that fails because of broken code.
"""

from word_counter import count_words


def test_count_words_tabs():
    """words are separated by tabs as well"""
    text = "the\twhite\whale"
    assert count_words(text) == 3

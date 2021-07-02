"""
Example of a Unit Test
"""

from mobydick.word_counter import count_words


def test_count_words():
    """Count words in a short sentence"""
    text = "Call me Ishmael"
    assert count_words(text) == 3

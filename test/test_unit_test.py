"""
Example of a Unit Test
"""

from word_counter import count_words

def test_count_words():
    """Count words in a short sentence"""
    n = count_words("Call me Ishmael")
    assert n == 3

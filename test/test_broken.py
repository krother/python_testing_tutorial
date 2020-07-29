"""
Examples of tests that fail.

TASK:

- In one of the tests, the count_words() function is buggy
- In the other test, the test is buggy

Find out which is which and fix both.
"""

from word_counter import count_words


def test_count_words_tabs():
    """words are separated by tabs as well"""
    text = "the\twhite\twhale"
    assert count_words(text) == 3


def test_words():
    """example with lots of special characters works"""
    text = """you haint no objections to sharing a harpooneer's blanket,
have ye? I s'pose you are goin' a-whalin',so you'd better get used to that sort of thing."""
    assert count_words(text) == 32

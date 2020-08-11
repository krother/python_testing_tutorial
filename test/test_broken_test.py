"""
Example of test that fails because of a broken test.
"""

from mobydick.word_counter import count_words


def test_words():
    """example with lots of special characters works"""
    text = """you haint no objections to sharing a harpooneer's blanket,
have ye? I s'pose you are goin' a-whalin',so you'd better get used to that sort of thing."""
    assert count_words(text) == 32


from mobydick import TextCorpus, count_word

MOBYDICK_SUMMARY = open('mobydick_summary.txt').read()


PAIRS = [
    ('months', 1),
    ('whale', 5),
    ('captain', 4),
    ('white', 2),
    ('harpoon', 1),
    ('goldfish', 0)
    ]


def test_check_word():
    word, number = PAIRS[0]
    text = TextCorpus(MOBYDICK_SUMMARY)
    assert count_word(text, word) == number

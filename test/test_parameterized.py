from mobydick.word_counter import count_words_dict

MOBYDICK_SUMMARY = open('./data/mobydick_summary.txt').read()


PAIRS = [
    ('whale', 5),
    ('goldfish', 0),
    ('captain', 4),
    ('white', 2),
    ('jellyfish', 99),
    ('harpoon', 1),
    ]


def test_count_words_dict():
    counts = count_words_dict(MOBYDICK_SUMMARY)
    for word, number in PAIRS:
        assert counts[word] == number

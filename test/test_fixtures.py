#
# example of tests with fixtures
#

from word_counter import TextBody


def set_up(self):
    """Prepare before each test"""
    MOBYDICK_SUMMARY = open('../test_data/mobydick_summary.txt').read()
    self.text = TextBody(MOBYDICK_SUMMARY)

def test_count_months(self):
    self.assertEqual(self.counter.count_word("months"), 1)

def test_count_the(self):
    """Count word in a longer text"""
    self.assertEqual(self.counter.count_word("the"), 6)

def test_word_number_text():
    """Count words in a text paragraph"""
    text = TextBody(MOBYDICK_SUMMARY)
    assert_equal(text.word_number, 54)


def tearDown(self):
    """Clean up after a test has passed or failed."""
    pass

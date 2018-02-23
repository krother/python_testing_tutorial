#
# Example of a class derived from TestCase 
#

from word_counter import TextBody

MOBYDICK_SUMMARY = open('mobydick_summary.txt').read()

class TestAverageWordLengthTests:
    """Tests for word_counter module."""

    def test_average_words(self):
        """Simple average length."""
        text = TextBody("white whale")
        self.assertEqual(text.get_average_word_length(), 5)

    def test_average_words_complex(self):
        """Complex average length."""
        text = TextBody(MOBYDICK_SUMMARY)
        self.assertAlmostEqual(text.get_average_word_length(), 4.0, 3)

    def test_average_empty(self):
        """Tests behaviour when input is not a string."""
        text = TextBody("")
        self.assertRaises(TypeError, text.get_average_word_length)
        


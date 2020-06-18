"""
Code that is being tested
"""

def count_words(text):
    if type(text) != str:
        raise TypeError('TextAnalyzer accepts only string input.')
    words = text.split()
    return len(words)

def average_word_length(text):
    """Returns the average word length as a float."""
    lengths = map(len, text.split())
    return sum(lengths) / len(lengths)


def count_words_dict(text, n):
    '''Returns the n most frequent words.'''
    ...
    d = {}

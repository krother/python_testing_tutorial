"""
Code that is being tested
"""

def count_words(text):
    if type(text) != str:
        raise TypeError('word counter accepts only string input.')
    words = text.split(' ')
    return len(words)


def count_words_dict(text, n):
    '''Returns the n most frequent words.'''
    d = {'dummy': 1}
    ...
    return d

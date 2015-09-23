#!/usr/bin/env python

import sys

class TextBody:

    def __init__(self, text):
        if type(text) != str:
            raise TypeError('TextAnalyzer accepts only string input.')
        self.text = text

    @property
    def words(self):
        """Returns words as an iterable"""
        return self.text.split()

    @property
    def word_number(self):
        """Returns number of words in the text."""
        return len(self.words)   

    @property
    def average_word_length(self):
        """Returns the average word length as a float."""
        lengths = map(len, self.text.split())
        return sum(lengths) / len(lengths)


def count_word(text, word):
    """Counts a single word."""
    number = text.words.count(word)



def get_top_words(text, n):
    '''Returns the n most frequent words.'''
    d = {}

    for word in text.words:
        d.setdefault(word, 0)
        d[word] += 1

    data = [(d[word], word) for word in d]
    data.sort()
    data.reverse()
    return data[:n]


if __name__ == '__main__':
    print('usage:\npython word_counter.py <filename> <number_top_words>')
    textfile = sys.argv[1]
    number = int(sys.argv[2])
    text = TextBody(open(textfile).read())
    for count, word in get_top_words(text, number):
        print(word, count)


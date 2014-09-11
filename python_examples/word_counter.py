#!/usr/bin/env python

import sys

class TextBody:

    def __init__(self, text):
        if type(text) != str:
            raise TypeError('TextAnalyser accepts only string input.')
        self.text = text

    @property
    def words(self):
        """Returns words as an iterable"""
        return self.text.split()

    @property
    def word_number(self):
        """Returns number of words in the text."""
        return len(self.words)   

    def get_average_word_length(self):
        """Returns the average word length as a float."""
        lengths = map(len, self.text.split())
        return sum(lengths) / len(lengths)


class WordCounter:
    """Counts words in a TextBody object"""
    
    def __init__(self, text):
        self.text = text
        
    def count_word(self, word):
        """Counts a single word."""
        number = self.text.words.count(word)
        

if __name__ == '__main__':
    text = open(sys.argv[1]).read()
    text = TextBody(text)
    word = sys.argv[2]
    counter = WordCounter(text)
    count = counter.count_word(word)
    print("%s:\t%i" % (word, count))





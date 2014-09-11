#!/usr/bin/env python

from word_counter import TextBody
import sys

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
    print('usage:\npython word_report.py <filename> <number>')
    textfile = sys.argv[1]
    number = int(sys.argv[2])
    text = TextBody(open(textfile).read())
    for count, word in get_top_words(text, number):
        print(word, count)


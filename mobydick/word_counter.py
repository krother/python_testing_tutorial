#!/usr/bin/env python
"""
Code that is being tested
"""

def split_to_words(text):
    '''split a string into tokens'''
    if type(text) != str:
        raise TypeError('accepts only string input.')
    words = text.split(' ')
    return words

def count_words(text):
    '''count number of words in a text'''
    words = split_to_words(text)
    return len(words)

def count_word(text, word):
    '''count the frequency of a word in a text'''
    words = split_to_words(text)
    return words.count(word)

def count_words_dict(text):
    '''Returns a dictionary of word counts'''
    words = split_to_words(text)
    d = {}

    for word in words:
        d.setdefault(word, 0)
        d[word] += 1

    return d

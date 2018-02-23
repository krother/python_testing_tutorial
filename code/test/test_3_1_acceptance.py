#!/usr/bin/env python
#
# example of an acceptance test for a command-line app
#

from unittest import TestCase
import os

PROGRAM = '../mobydick/word_counter.py'
TEXT_FILE = '../test_data/mobydick_summary.txt'
OUTPUT = 'out.tmp'

class WordCounterAcceptanceTests(TestCase):

    def test_commandline(self):
        """Count words in a short text"""
        # remove output file if it is already there
        if os.path.exists(OUTPUT):
            os.remove(OUTPUT)

        # run the command line app
        cmd = 'python %s %s white > %s' % (PROGRAM, TEXT_FILE, OUTPUT)
        os.system(cmd)
        
        # check the output
        out = open(OUTPUT).read()
        self.assertTrue('white:\t2' in out)





"""
Example for testing a command-line app
"""

import os

PROGRAM = '../mobydick/word_counter.py'
TEXT_FILE = 'mobydick_summary.txt'
OUTPUT = 'out.tmp'


class TestCommandline:

    def test_commandline(self):
        """Count words in a short text"""
        # remove output file if it is already there
        if os.path.exists(OUTPUT):
            os.remove(OUTPUT)

        # run the command line app
        cmd = 'python %s %s 2 > %s' % (PROGRAM, TEXT_FILE, OUTPUT)
        os.system(cmd)
        
        # check the output
        out = open(OUTPUT).read()
        assert 'white:\t2' in out

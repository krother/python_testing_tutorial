
# Testing Command-Line Programs

### Exercise 1: Test a command-line application
The program **word_counter.py** can be used from the command line to calculate the most frequent words with:

    python word_counter.py mobydick_summary.txt

Command-line applications need to be tested as well. You find tests in **test_commandline.py**.

Your task is to make sure the command-line tests pass.

### Exercise 2: Test command-line options
The program **word_counter.py** calculates most frequent words in a test file. It can be used from the command line to calculate the top five words:

    python word_counter.py moby_dick_summary.txt 5

Your task is to develop a new test for the program.


### Exercise 3: User Acceptance

The ultimate test for any software is whether your users are able to do what they need to get done.

Your task is to *manually* use the program **word_counter.py** to find out whether Melville used *'whale'* or *'captain'* more frequently in the full text of the book *"Moby Dick"*.

**The User Acceptance test cannot be replaced by a machine.**

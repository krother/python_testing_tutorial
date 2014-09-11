# Challenges

Here, you find a collection of problems that can be solved by software testing.

### Test a Python function
The function **main()** in the module **word_counter.py** calculates the most frequent words in a text body. For instance:

    The program works perfectly.

Does the function calculate the number of words in the text correctly with **four**?

### Fix a failing test
The code in the test file **test_failing.py** is broken.

Prove that it is broken.

Then fix the code, so that the tests pass.


### Run multiple tests
In the file **test_group.py** you find multiple test functions.  Fill in the blanks in the file. Then run the code.

### Test a command line program
Run and fix the command-line test example in the file **test_commandline.py**.


### Write a new test
The module **word_report.py** contains a function to calculate the most frequent words in a text body. Check whether the most frequent words in the file **mobydick_summary.txt** calculated by the function are:

| word | count |
|------|-------|
| of   |  34 |
| the  |  23 |
| is   |  21 |
| sea  |  12 |
| ship |  3 |

### Write a command-line-test
Test whether ther program **word_report.py** calculates the five most frequent words correctly when used from the command line with the command:

    python word_report.py moby_dick_summary.txt 5


### Add a feature: special characters
Add a new feature to the **word_counter.py** program. The program should remove special characters from the text before counting words.

Prove that the new feature is working.

### Add a feature: ignore case
Add a new feature to the **word_counter.py** program. The program should ignore the case of words, e.g. *'captain'* and *'Captain'* should be counted as the same word.

### Test without dependencies
You need to test a function that usually requires another class, but you want to exclude the possibility that the other class is buggy.

Write a test for the function **word_report.get_top_words()** that does not use the class **TextBody**.

### Prepare test data
Create a new module **test_data.py** with a string variable that contains a sentence with lots of special characters:

    "That #§&%$* program still doesn't work!\nI already de-bugged it 3 times, and still numpy.array keeps raising AttributeErrors. What should I do?"

Add three smaller strings to the module that cover different issues with special characters, e.g. no special characters, only special characters, many special characters in a row etc.

Test the word count for each of the strings by importing them from the **test_data** module.


### Test border cases
Fill the gaps in **test_border_cases.py**. Use all alternatives that are given in the file.

### Test Coverage
What is the percentage of code covered by automatic tests for the modules **word_counter.py** and **word_report.py**.


### Preparations before tests
Sometimes you need to prepare multiple tests in a similar way. For instance, a number of tests for **word_report.py** require loading the contents of the text file **mobydick_summary.txt**.

Make sure the code for loading the text file appears only once.

### Import test data in multiple test packages
In a bigger software package, you have a lot of tests distributed to two packages. Both of them require the variable **MOBYDICK_SUMMARY** in **test data.py**:

    tests/
        test_a/
            test_first.py
        test_b/
            test_second.py
        test_data.py

Make sure the variable **MOBYDICK_SUMMARY** is correctly imported to both test modules.

### Sets of example data
You have a list of pairs (data sample, expected result). Test all data samples in a way that makes it easy to add many more pairs (in particular, *don't* copy-paste a new test function for each data sample).

The following samples apply to the text **mobydick_summary.txt**:

| word | count |
|------|-------|
| months | 1 |
| whale  | 5 |
| captain | 4 |
| white | 2 |
| harpoon | 1 |
| Ahab | 1 |

When the test is running, add two more examples.

### Test selection
Run a single test function from a larger test suite.

### Test collection
Run all tests you have written so far with one command from the console.

### Integrate a test suite in a Python package
Run all tests from **setup.py** by typing:

    python setup.py test


### User Acceptance
Use the program **word_counter.py** to find out whether Melville used *'whale'* or *'captain'* more frequently in the full text of the book *"Moby Dick"*.


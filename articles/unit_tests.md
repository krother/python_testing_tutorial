
# Unit Tests

### Exercise 1: Test a Python function

The function **main()** in the module **word_counter.py** calculates the number of words in a text body.

For instance, the following sentence contains **three** words:

    Call me Ishmael

Your task is to prove that the **TextCorpus** class calculates the number of words in the sentence correctly with **three**.

Run the example test in **test_unit_test.py** with

    pytest test_unit_test.py


### Exercise 2: Test proves if code is broken

The test in the module **test_broken_code.py** fails, because there is a bug in the function **word_counter.average_word_length()**. In the sentence

    Call me Ishmael

The words are **four, two,** and **seven** characters long. This gives an average of:

    >>> (4 + 2 + 7) / 3.0
    4.333333333333333

Fix the code in `test_broken_code.py`, so that the test passes.


### Exercise 3: Code proves if tests are broken

The test in the module **test_broken_test.py** fails, because there is a bug in the test file.

Your task is to fix the test, so that the test passes. Use the example in **test_broken_test.py**.


### Exercise 4: Test border cases

High quality tests cover many different situations. The most common situations for the program **word_counter.py** include:

| test case | description | example input | expected output
|-----------|-------------|---------------|-----------------
| empty | input is valid, but empty | "" | 0
| minimal | smallest reasonable input | "whale" | 1
| typical | representative input | "whale eats captain" | 3
| invalid | input is supposed to fail | 777 | *Exception raised*
| maximum | largest reasonable input | *Melville's entire book* | *more than 200000*
| sanity | program recycles its own output | *TextBody A created from another TextBody B* | *A equals B*
| nasty | difficult example | "That #~&%* program still doesn't work!" | 6

Your task is to make all tests in **test_border_cases.py** pass.

## New Features!

### Exercise 5: Word separators

The program **word_counter.py** separates words at spaces, but not tabulators. You need to change that.

The following sentence should also contain **four** words:

    The\tprogram\tworks\tperfectly.

Your task is to add a test for this new situation and make it work.

### Exercise 6: Special characters
Add a new feature to the **word_counter.py** program. The program should remove special characters from the text before counting words.

Your task is to prove that the new feature is working.

### Exercise 7: Ignore case
Add a new feature to the **word_counter.py** program. The program should ignore the case of words, e.g. *'captain'* and *'Captain'* should be counted as the same word.

Your task is to prove that the new feature is working.

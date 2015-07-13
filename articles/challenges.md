# Challenges

Here, you find a collection of problems that can be solved by software testing. Pick the ones that fit the needs of your trainees.

### Contents

1. Unit Tests
2. Integration Tests
3. Acceptance Tests
4. Test Data
5. Test Suites
6. Test Coverage
7. Testing New Features

----

## 1. Unit Tests

### 1.1 Test a Python function
The function **main()** in the module **word_counter.py** calculates the number of words in a text body.

For instance, the following sentence contains **three** words:

    Call me Ishmael

Your task is to prove that the **main()** function calculates the number of words in the sentence correctly with **three**.

Use the example test in **test_1_1_unit_test.py**.

### 1.2 Test proves if code is broken
The test in the module **test_failing_code.py** fails, because there is a bug in the function **word_counter.average_word_length()**. In the sentence

    Call me Ishmael

The words are **four, two,** and **seven** characters long. This gives an average of:

    >>> (4 + 2 + 7) / 3.0
    4.333333333333333

Your task is to fix the code, so that the test passes.

Use the example in **test_1_2_broken_code.py**.

### 1.3 Code proves if tests are broken
The test in the module **test_failing_test.py** fails, because there is a bug in the test file.

Your task is to fix the test, so that the test passes. Use the example in **test_1_3_broken_test.py**.


### 1.4 Test border cases
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

Your task is to make all tests in **test_1_4_border_cases.py** pass.

### 1.5 Run multiple tests
Software tests can be grouped and executed together.

Your task is to execute all of the above tests with one command and make them pass.

----

## 2. Integration Tests

### 2.1 Integrating two modules
pass

### 2.2 Mock Objects
The function **word_report.get_top_words()** requires an instance of the class **TextBody**. You need to test the function, excluding the possibility that the **TextBody** class is buggy. To do so, you need to replace the class by a **Mock Object**, a simple placeholder.

Your task is to write a test for the function **word_counter.get_top_words()** that does not use the class **TextBody**.

----

## 3. Acceptance Tests

### 3.1 Test a command-line application
The program **word_counter.py** can be used from the command line to calculate the most frequent words with:

    python word_counter.py mobydick_summary.txt

Command-line applications need to be tested as well. You find tests in **test_3_1_commandline.py**.

Your task is to make sure the command-line tests pass.

### 3.2 Test command-line options
The program **word_counter.py** calculates most frequent words in a test file. It can be used from the command line to calculate the top five words:

    python word_counter.py moby_dick_summary.txt 5

Your task is to develop a new test for the program.

### 3.3 User Acceptance
The ultimate test for any software is whether your users are able to do what they need to get done.

Your task is to *manually* use the program **word_counter.py** to find out whether Melville used *'whale'* or *'captain'* more frequently in the full text of the book *"Moby Dick"*.

**The User Acceptance test cannot be replaced by a machine.**

----

## 4. Test Data

### 4.1 A module with test data
Create a new module **test_data.py** with a string variable that contains a sentence with lots of special characters:

    "That #§&%$* program still doesn't work!\nI already de-bugged it 3 times, and still numpy.array keeps raising AttributeErrors. What should I do?"

Your task is to write a test for the module **word_count.py** using the string imported from the **test_data** module.


### 4.2 Preparing tests with fixtures
Sometimes multiple tests need similar preparations. For instance, the tests in **test_word_report.py** require loading the contents of the text file **mobydick_summary.txt**.

Your task is to make sure the code for loading the text file appears only once.


### 4.3 Sets of example data
You have a list of pairs (data sample, expected result) for the program **count_words.py** that apply to the text **mobydick_summary.txt**:

| word | count |
|------|-------|
| months | 1 |
| whale  | 5 |
| captain | 4 |
| white | 2 |
| harpoon | 1 |
| Ahab | 1 |

Your task is to create six tests from these samples. Figure out how more pairs can be added easily. In particular, *don't* copy-paste a new test function for each data sample.

### 4.4 Write a test with sample data
The module **word_report.py** contains a function to calculate the most frequent words in a text body. It should produce the following top five results for the book in **mobydick.txt**:

| position | word |
|----------|------|
| 1. | of   |
| 2. | the  |
| 3. | is   |
| 4. | sea  |
| 5. | ship |

Your task is to write tests for these five positions.

### 4.5 Import test data in multiple test packages
In a big software project, your tests are distributed to two packages. Both **test_first.py** and **test_second.py** require the variable **MOBYDICK_SUMMARY** from the module **test data.py**. The package structure is like this:

    testss/
        test_a/
            __init__.py
            test_first.py
        test_b/
            __init__.py
            test_second.py
        __init__.py
        test_data.py
        test_all.py

Your task is to make sure that the variable **MOBYDICK_SUMMARY** is correctly imported to both test modules, so that the tests pass for all of:

    tests/test_a/test_first.py
    tests/test_b/test_second.py
    tests/test_all.py


----

## 5. Test Suites

### 5.1 Test selection
Your task is to run only the function **test_word_counter.test_simple** from the test suite in **tests/**.

### 5.2 Test collection
Your task is to run all tests in the directory **tests/** with one command.

### 5.3 Integrate a test suite in a Python package
Your task is to make it possible to run all tests for a package by typing:

    python setup.py test


----

## 6. Test Coverage

### 6.1 Calculate Test Coverage
Your task is to calculate the percentage of code covered by automatic tests for the modules **word_counter.py** and **word_report.py**.

### 6.2 Identify uncovered lines
Your task is to find out which lines of **word_counter.py** are not covered by tests.

### 6.3 Increase test coverage
Your task is to bring test coverage of **word_counter.py** to 100%.


----

## 7. Testing New Features

### 7.1 Add new feature: special characters
Add a new feature to the **word_counter.py** program. The program should remove special characters from the text before counting words.

Your task is to prove that the new feature is working.

### 7.2 Add new feature: ignore case
Add a new feature to the **word_counter.py** program. The program should ignore the case of words, e.g. *'captain'* and *'Captain'* should be counted as the same word.

Your task is to prove that the new feature is working.

### 7.3 Add new feature: word separators
The program **word_counter.py** does separate words at spaces, but not tabulators. You need to change that.

The following sentence should also contain **four** words:

    The\tprogram\tworks\tperfectly.

Your task is to add a test for this new situation and make it work.


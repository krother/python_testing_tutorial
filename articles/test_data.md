
# Test Data

### Exercise 1: A module with test data
Create a new module **test_data.py** with a string variable that contains a sentence with lots of special characters:

    "That #§&%$* program still doesn't work!\nI already de-bugged it 3 times, and still numpy.array keeps raising AttributeErrors. What should I do?"

Your task is to write a test for the module **word_count.py** using the string imported from the **test_data** module.


### Exercise 2: Preparing tests with fixtures
Sometimes multiple tests need similar preparations. For instance, the tests in **test_word_report.py** require loading the contents of the text file **mobydick_summary.txt**.

Your task is to make sure the code for loading the text file appears only once.


### Exercise 3: Sets of example data
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

### Exercise 4: Write a test with sample data
The module **word_report.py** contains a function to calculate the most frequent words in a text body. It should produce the following top five results for the book in **mobydick.txt**:

| position | word |
|----------|------|
| 1. | of   |
| 2. | the  |
| 3. | is   |
| 4. | sea  |
| 5. | ship |

Your task is to write tests for these five positions.

### Exercise 5: Import test data in multiple test packages
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


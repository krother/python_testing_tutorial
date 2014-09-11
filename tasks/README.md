# Tasks

## Part 1: Automatic Tests

### Task 1.1: Run a test
The module most_frequent.py calculates the most frequent words in a text body.

* Run the test.

### Task 1.2: TestCase subclasses
Fill in the blanks in the file

    test_unit.py

Run the code

    nosetests test_unit.py


### Task 1.3: Integration Tests
Fix the code so that the tests pass

    nosetests test_integration.py


### Task 1.4: Testing a command line app
Run the acceptance test example

    nosetests test_acceptance.py


### Task 1.5: Write your own tests
Test the module

    word_report.py

Write an Integration Test and an Acceptance Test.

#### Bonus question:
How would you write a Unit Test for

    get_top_words()

that does not use **TextBody**?

## Part 2: Test-Driven-Development
Add a feature to the word_counter program that removes special characters from the text before counting words.

### Task 2.1: Prepare test data
Create a new module. As test data, create a string variable that contains a sentence with lots of special characters.

### Task 2.2: Apply TDD
Make TextBody remove special characters automatically.

Write code that evaluates your test data by strictly applying the following procedure:

1. Write a test function.
2. Run the test and make sure it fails.
3. Write code.
4. Run the test and make sure it passes.

### Task 2.3: Add border cases
Repeat the procedure above 2-3 times to cover a couple of different situations with special characters (no special characters, only special characters, many special characters in a row etc.).

Fill in the assert functions

    nosetests test_border_cases.py

Use all functions that are imported.

### Task 2.4: Add a fixture

**Fixture: load the text file in setUp()**
**Fixture: example for tearDown(): remove temp files.**

** how to import test data in multiple test packages**
patch pythonpath in a local test_data that imports ../test_data.*

Add a method setUp(self) that defines variables common to a few of your tests.


Run the code example

    nosetests test_fixtures.py

### Task 2.5: Test Generators
Run the code example

    nosetests test_generator.py

### Task 3.1: Test Coverage
Calculate test coverage

    nosetests test_generator.py

### Test collection

### Test selection
*



### Task 3.2: Test suites
Run all tests

    nosetests -­v

### Task 3.3: Integrating tests in your package
Write a script that runs all tests when you type:

    python setup.py test

* pyscaffold adds a py.test mode by default.

### Task 3.4: User Acceptance
Use the program

    word_counter.py

to find out whether Melville
used *'whale'* or *'captain'*
more frequently in his book.

### Task 4: kinds of tests

pairs: name - description

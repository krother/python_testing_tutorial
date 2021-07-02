
# Unit Tests

## Warming Up

#### How many words are in the following sentence?

```bash
Call me Ishmael.
```

----

#### How many words are in the next sentence?

```bash
"you haint no objections to sharing a harpooneer's blanket,
have ye? I s'pose you are goin' a-whalin',
so you'd better get used to that sort of thing."
```


----

### Exercise 1: Test a Python function

The function `count_words()` in the module **word_counter.py** calculates the number of words in a text body.

For instance, we would expect the following input to result in a word count of `3`:

```bash
Call me Ishmael
```

Your task is to prove that the `count_words()` function in fact returns `3`.

Run the example test in `test_unit_test.py` with

```bash
python -m pytest test/test_unit_test.py
```

----

### Exercise 2: A test fails if code is broken

Run the tests in `test_broken.py` and inspect the output.

One of the tests fails, because there is a bug in the function `count_words()`.

The other test fails because there is a bug in the test.

Find out what is broken in which test.

----

### Exercise 3: Fixing tests

Fix the code and test in `test_broken.py`.

Run the tests again, so that both of them pass.

----

### Exercise 4: Test border cases

High quality tests cover many different situations.
Common situations for the program **word_counter.py** include:

| test case | description | example input | expected output
|-----------|-------------|---------------|-----------------
| empty | input is valid, but empty | "" | 0
| minimal | smallest reasonable input | "whale" | 1
| typical | representative input | "whale eats captain" | 3
| invalid | input is supposed to fail | 777 | `TypeError`
| maximum | largest reasonable input | *Melville's entire book* | *> 200000*
| nasty | difficult example | "That #~&%* program still doesn't work!" | 6

Your task is to make all tests in **test_border_cases.py** pass.

----

### Exercise 5: Special characters

Add a new feature to the **word_counter.py** program. The program should remove special characters from the text before counting words.

Your task is to write a test for this new feature.

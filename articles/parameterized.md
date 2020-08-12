
# Parameterized Tests

### Exercise 1: Sets of example data

The tests in `test_parameterized.py` check a list of pairs (word, count) that apply to the text file `mobydick_summary.txt`:

    ```python
    PAIRS = [
        ('whale', 5),
        ('goldfish', 0),
        ('captain', 4),
        ('white', 2),
        ('jellyfish', 99),
       ('harpoon', 1),
    ]
    ```

Run the tests and see what happens.

----

### Exercise 2: Fixing the test

Fix the test by using the `count.get(word)` method instead of `[word]`.
Run the test again. What happens?

----

### Exercise 3: Parameterize

There is a deeper issue here. We want all test examples to be *independent*.
We will create six tests from the example data.

Use the **test parametrization in pytest**.
Change the test function by adding the following decorator:

```python
import pytest

@pytest.mark.parametrize('word, number', PAIRS)
def test_count_words_dict(word, number):
    ...
```

The two arguments will be filled in automatically.
Now remove the `for` loop.

Run the test.
You should see six tests instead of one.
Make sure all six pass.

----

### Exercise 2: Write another parameterized test

Use test parametrization to test the `count_words()` function on the following test cases.

| text | expected result |
|----------|------|
| Call me Ishmael | 3 |
| . | 0  |
| 1234 | 1 |
| x | 1 |
| We are the Borg - Resistance is futile | 7  |

Write one parameterized test that checks these five examples.

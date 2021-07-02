
# Fixtures

Sometimes you need to prepare test data (load files, create objects etc.).
If you want to prepare the same data for multiple tests, you can use a **fixture**.

----

### Exercise 1: A module for test data

Create a new module `conftest.py` in the same directory as your tests.
There, add a function that loads the file `data/mobydick_summary.txt`:

Place the decorator `@pytest.fixture` on top of it:

```python
import pytest

@pytest.fixture
def text_summary():
    return open(...).read()
```

----

### Exercise 2: Using the fixture

Now create a module `test_corpus.py` with a function that uses the fixture:

```python
def test_short_sample(text_summary):
    assert count_words(text_summary) == 77
```

Execute the module with `pytest`. Note that you **do not** need to import `conftest`. Pytest does that automatically.

----

### Exercise 3: Create more fixtures

Create a fixture for the full text of the book `mobydick_full.txt` as well.

----

### Exercise 4: Fixtures from fixtures

Create a fixture in `conftest.py` that prepares a dictionary with word counts using the `word_counter.count_words_dict()` function.

```python
from word_counter import count_words_dict

@pytest.fixture
def count_dict(text_summary):
    return ...
```

Write a simple test that makes sure the dictionary is not empty.

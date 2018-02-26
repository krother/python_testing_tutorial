
# Parameterized Tests

### Exercise 1: Sets of example data

You have a list of pairs (word, count) that apply to the text file `mobydick_summary.txt`:

    PAIRS = [
             ('months', 1),
             ('whale', 5),
             ('captain', 4),
             ('white', 2),
             ('harpoon', 1),
             ('goldfish', 0)
    ]

We will create six tests from these samples.

Instead of creating six tests manually, we will use the **test parametrization in pytest**. Edit the file `test_parameterized.py` and add the following decorator to the test function:

    @pytest.mark.parametrize('word, number', PAIRS)

Add two arguments `word` and `number` to the function header and remove the assignment below.

Run the test and make sure all six tests pass.


### Exercise 2: Write another parameterized test

The function **get_top_words()** calculates the most frequent words in a text corpus. It should produce the following top five results for the book **mobydick_full.txt**:

| position | word |
|----------|------|
| 1. | of   |
| 2. | the  |
| 3. | is   |
| 4. | sea  |
| 5. | ship |

Write one parameterized test that checks these five positions.

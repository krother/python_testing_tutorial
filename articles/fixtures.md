
# Fixtures

### Exercise 1: A module for test data

Create a new module `conftest.py` with a string variable that contains a sentence with lots of special characters:

    sample = """That #§&%$* program still doesn't work!
    I already de-bugged it 3 times, and still numpy.array keeps raising AttributeErrors. What should I do?"""

Create a function that returns a `mobydick.TextCorpus` object with the sample text above. Use the following as a header:

    @pytest.fixture
    def sample_corpus():
        ...


### Exercise 2: Using the fixture

Now create a module `test_sample.py` with a function that uses the fixture:

    def test_sample_text(sample_corpus):
        assert sample_corpus.n_words == 77

Execute the module with `pytest`. Note that you **do not** need to import `conftest`. Pytest does that automatically.


### Exercise 3: Create more fixtures

Create fixtures for the two text corpora in the files `mobydick_full.txt` and `mobydick_summary.txt` as well.


### Exercise 4: Fixtures from fixtures

Create a fixture in `conftest.py` that uses another fixture:

    from mobydick import WordCounter

    @pytest.fixture
    def counter(mobydick_summary):
    	return WordCounter(mobydick_summary)

Write a simple test that makes sure the fixture is not `None`

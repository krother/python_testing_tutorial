# Python Testing for Trainers
**A Course building Toolkit**

## Contributors
Kristian Rother, Magdalena Rother, Daniel Szoska

## Overview
This toolkit helps you to prepare training courses on automated testing in Python. It allows you to create courses with interchangeable

* testing frameworks
* background of participants
* course duration

Our aim is to save you preparation time while leaving room for your own ideas.

Most of all, we hope you have fun in your next course.

## How to make a course
Build a course using the following formula:

    course = theme + challenges + tools

### Theme
The content of the course is wrapped into a *Moby Dick* theme: trainees will count frequent words in Melville's book about the white whale. The theme is the driving force that will motivate trainees to keep going.

### The Challenges
Challenges are problem descriptions relevant to the topic of the course. They are related to real-world problems. Challenges are more general than e.g. tasks for trainees. You can adjust challenges to fit to a given difficulty or time frame. They are the raw material to create both *tasks* and *learning objectives*.

### The Tools
Tools are what your trainees will use to solve the challenges. They include: Python programs, code examples, example data etc. Tools are interchangeable. The material given here works with different Python testing frameworks.

### Learning Objective
During the tutorial participants will implement automatic test functions that pass for the Moby Dick example. using the unittest module within 20'.

### Duration
one hour for a group of experienced developers. For beginners, you may double or triple that time.

### Material
* Handout “Introduction to the unittest Framework in Python”
* Slide: Challenge
* Slide: Task description
* TextAnalyser.py
* TestTextAnalyzer.py

## Task Description
What are the 5 words that Melville used the most in Moby Dick?
Extend the TextAnalyser class with a function that returns the five most frequent words from Melvilles “Moby Dick”.
Add a corresponding test function to the TextAnalyserTests module.

Ensure that the test passes.

Testing adds precision to your work.


#### TASK: run minimal test example
> nosetests

EXPLAIN OUTPUT

## Structure

### Purposes of Testing
* Write code
* debug
* refactor
* maintain software
* teamwork

### Testing Strategies

#### Types of tests
* Unit Tests
* Acceptance Tests
* Integration Tests
* Regression Tests

#### Test tools
* Coverate
* Mock Objects
* test suite
* TDD
* test data
* 1 assert per test
* border cases

### 7 Features of nose
* test functions
* TestCase subclasses
* asserts from nose.tools
* fixtures setUp() tearDown()
* test generators
* test detection
* test selection


## Structure

### Types of Tests
* Unit Tests
* Integration Tests
* Acceptance Tests
* Regression tests

### Quality Tests
* Write tests first
* 1 assert per test
* Border cases
* Test data
* Mock objects

### Development
* Test coverage
* Test suite
* Setup script
* User Acceptance
* Functional testing
--------------------------
I. Writing automatic tests in Python

Warm-up exercise: run example test

1.1 nosetests
- nosetests
- -v
- explain output
- test functions (EXAMPLE)
- assert, nose.tools (EXAMPLE)

1.2 Unit Testing
- testing in isolation
- TestCase subclasses (EXAMPLE)
- self.assert statements

1.3 Integration Tests
- two together (EXAMPLE)

1.4 Acceptance Tests
- disambiguation: vs. Web tests, User acceptance tests, manual tests
- command line tests (EXAMPLE)

TASKS:
- TASK: write a Unit Test
- TASK: write a Integration Test
- TASK: write an Acceptance Test

----------------------------
II. Test-Driven Development

2.1 TDD
- What is TDD
- 1 assert per test
- when all tests pass, stop coding
- have test data
- what kind of tests to write?

2.2 Border cases
- empty, fail, smallest, biggest, nasty, sanity (EXAMPLE)

2.3 Fixtures
- in modules
- in classes (EXAMPLE)

2.4 Test generators
- generators (EXAMPLE)

TASK: Write test first
----------------------------
III. Tests during refactoring

Warm-up: Puzzle: calculating coverage

3.1 Refactoring
- example strategy
- tests need structure, too
- mock objects (EXAMPLE)

3.2 Test detection
- test detection
- test selection

3.3 Building a Test Suite
- test suite
- setup script

3.4 Coverage
- run coverage

TASK: refactor
TASK: run coverage


## Copyright

Feedback and comments are welcome at: krother@academis.eu

© 2013 Magdalena & Kristian Rother

Released under the conditions of a Creative Commons
Attribution License 4.0.

# Instructions for Trainers

This chapter aims to help you to run a tutorial on automated testing in Python.
Our aim is to save you preparation time while leaving room for your own ideas.
Most of all, we hope you have fun in your next course.

## How to run a course using this toolkit

1. Introduce the Moby Dick Theme to your trainees
2. Clone the repository
3. Share the exercises with your trainees
5. Start coding your way through the chapters

## Lesson plan for a 180' tutorial

| module | topic | time |
|--------|-------|------|
| warm-up | introduce the Moby Dick theme | 5' |
| warm-up | announce training objectives | 5' |
| |
| **part 1**  | **Writing automatic tests in Python** | 45’ |
| warm-up | warmup question | 5' |
| new content | presentation: Unit Tests in pytest | 10’ |
| application | exercises: Unit Tests | 25’ |
| wrap-up | Q & A | 5’ |
| |
| **part 2**  | **Test Strategies (45')** | |
| warm-up | quiz on test strategies | 10' |
| new content | presentation on Test-Driven-Development | 10’ |
| application | exercises: fixtures and parameterized tests | 20' |
| wrap-up | Q & A | 5’ |
| |
| **break** | | 10’ |
| |
| **part 3**  | **Tests data and test suites (45')** | |
| warm-up | multiple choice questions | 10' |
| new content | presentation on Integration and Acceptance Tests | 10’ |
| application | exercises: test collection and test coverage | 20' |
| wrap-up | Q & A | 5’ |
| |
| **summary**  | **Benefits of testing (25')** | |
| transfer | group discussion on benefits of testing | 15’ |
| wrap-up | recap puzzle | 5’ |
| finishing | summary | 4’ |
| finishing | goodbye | 1' |

I used a similar lesson plan to conduct a training at EuroPython 2014.
The audience consisted of about 60 Python programmers, including beginners and seasoned developers.

## Why the Moby Dick example?

Three main reasons:

* The implementation is simple enough for beginners
* Counting words yields different border cases (because of upper/lower case, special characters etc), making a sufficient use case for testing
* You can easily change the theme to another book from [Project Gutenberg](http://www.gutenberg.org/).

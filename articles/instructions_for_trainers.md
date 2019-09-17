# Instructions for Trainers

## Overview
This toolkit helps you to prepare training courses on automated testing in Python. It allows you to create courses with interchangeable

* testing frameworks
* background of participants
* course duration

Our aim is to save you preparation time while leaving room for your own ideas. Most of all, we hope you have fun in your next course.

## How to run a course using this toolkit

1. Introduce the Moby Dick Theme to your trainees
2. Clone the repository
3. Set the PYTHONPATH environment variable, so that you can do

    import mobydick

4. Share the exercises with your trainees.
5. Start coding!

## Lesson plan for a 180' tutorial

| module | topic | time |
|--------|-------|------|
| warm-up | introduce the Moby Dick theme | 5' |
| warm-up | icebreaker activity | 5' |
| warm-up | announce training objectives | 5' |
| |
| **part 1**  | **Writing automatic tests in Python** | 45’ |
| warm-up | methods in the unittest module | 5’ |
| new content | presentation: Unit Tests, Integration Tests, and Acceptance Tests | 15’ |
| application | challenges 1.1 - 1.5 | 20’ |
| wrap-up | Q & A | 5’ |
| |
| **part 2**  | **Integration and Acceptance Tests (45')** | |
| warm-up | quiz on test strategies | 10' |
| new content | presentation on Test-Driven-Development | 10’ |
| application | challenges 2.1 - 3.3 | 20' |
| wrap-up | Q & A | 5’ |
| |
| **break** | | 10’ |
| |
| **part 3**  | **Tests data and test suites (45')** | |
| warm-up | multiple choice questions | 10' |
| new content | presentation on test suites | 10’ |
| application | exercises 4, 5, 6 | 20' |
| wrap-up | Q & A | 5’ |
| |
| **summary**  | **Benefits of testing (25')** | |
| transfer | group discussion on benefits of testing | 20’ |
| finishing | summary | 4’ |
| finishing | goodbye | 1' |

I used a very similar lesson plan to conduct a training at EuroPython 2014. The audience consisted of about 60 Python programmers, including beginners and seasoned developers.

## Why was this example selected?

Three main reasons:

* The implementation is simple enough for beginners.
* Counting words easily yields different results (because of upper/lower case, special characters etc). Therefore the program needs to be thoroughly tested.
* You can easily change the theme to another book from [Project Gutenberg](http://www.gutenberg.org/).

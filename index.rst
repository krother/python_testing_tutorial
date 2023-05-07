Python Testing Tutorial
=======================

This tutorial helps you to learn automated testing in Python using the
``pytest`` framework.

.. figure:: images/mobydick.png
   :alt: Moby Dick


.. topic:: Goal: Count Words in Moby Dick

   *Captain Ahab was vicious because Moby Dick, the white whale, had bitten
   off his leg. So the captain set sail for a hunt. For months he was
   searching the sea for the white whale. The captain finally attacked the
   whale with a harpoon. Unimpressed, the whale devoured captain, crew and
   ship. The whale won.*

   .. figure:: images/counting470.png
      :alt: tick marks while counting words
   
   Herman Melville’s book *“Moby Dick”* describes the epic fight between
   the captain of a whaling ship and a whale. In the book, the whale wins
   by eating most of the other characters. 
   **But does he also win by being mentioned more often?**
   
   **In this course, you will test a program that is counting words in
   Melvilles book.**

Preparations
------------

clone the repository:

::

   git clone https://github.com/krother/python_testing_tutorial.git

install **pytest**:

::

   pip install pytest

Chapters
--------

.. toctree::
   :maxdepth: 1

   articles/unit_tests.md
   articles/fixtures.md
   articles/parameterized.md
   articles/organizing_tests.md
   articles/test_coverage.md

Appendix
--------

.. toctree::
   :maxdepth: 1

   articles/quotes.md
   articles/find_pairs.md
   articles/instructions_for_trainers.md

Links
-----

-  `Python Testing Tutorial <https://katyhuff.github.io/python-testing/>`__ - by Kathryn Huff
-  `Introduction to pytest <https://www.youtube.com/watch?v=UPanUFVFfzY>`__ - by Michael Tom-Wing and Christie Wilson
-  `Test & Code Podcast <http://testandcode.com/>`__ - by Brian Okken
-  `The Clean Code Talks – Unit Testing <http://www.youtube.com/watch?v=wEhu57pih5w&feature=channel>`__
-  `Test-Driven-Development <https://www.youtube.com/watch?v=L4hOiGOKSxQ>`__ - by H.Percival


.. topic:: License

   this tutorial was contributed to by Kristian Rother, Magdalena Rother, Daniel Szoska

   Usable under the conditions of the Creative Commons Attribution License 4.0 (CC-BY 4.0).
   See `creativecommons.org <https://creativecommons.org/licenses/by/4.0/>`__ for details

Feedback and comments are welcome at: `kristian.rother@posteo.de`

Sources for this tutorial:
`github.com/krother/python_testing_tutorial <https://github.com/krother/python_testing_tutorial>`__.

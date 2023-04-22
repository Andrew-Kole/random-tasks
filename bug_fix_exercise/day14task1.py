"""
Bug-Fixing Exercise 1
The program depicted below consists of two Python files. The program tries to count and print out the number of periods in the "Trees are good. Grass is green." . However, running the cli.py file returns an error. Please fix the error.

cli.py:

import functions

nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)


functions.py:

def count(phrase):
    return phrase.count('.')
"""
from modules import bfday14task1func

nr_of_periods = bfday14task1func.count("Trees are good. Grass is green.")
print(nr_of_periods)


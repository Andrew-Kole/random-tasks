"""
The same program as in exercise 1 now is throwing yet another error. Hunt the error down and fix it.

main.py:

import functions.py

nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)


functions.py:

def count(phrase):
    return phrase.count('.')
"""

from modules import bf_day14task2

nr_of_periods = bf_day14task2.count("Trees are good. Grass is green.")
print(nr_of_periods)

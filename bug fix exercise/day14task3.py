"""
There is another error in the same program. Please fix the error.

main.py:

from functions import count

nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)


functions.py:

def count(phrase):
    return phrase.count('.')
"""

from modules.bf_day14task3 import count

nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)
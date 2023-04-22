"""
Define a function that has two parameters, year_of_birth and current_year . The current_year parameter should be a default parameter with the current year as a default value.

The function should calculate and return the age of the user given the year of birth and the current year.

Note: It is enough to define the function for this exercise -no need to call it.
"""


def calculate_age(year_of_birth, current_year=2023):
    return current_year - year_of_birth

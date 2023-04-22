"""
Extend the program you wrote in exercise 2 by printing a message to the user instead of their age if their age is greater than 120. Feel free to print any message that you like.
"""

def calculate_age(year_of_birth, current_year=2023):
    return current_year - year_of_birth


year = int(input("What is your year of birth? "))

if calculate_age(year) > 120:
    print("Are you human at all?")
else:
    print(calculate_age(year))
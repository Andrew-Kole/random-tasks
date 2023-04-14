"""
Your task for this exercise is to use the function you created in exercise 1. Then, below the function definition, get the year of birth from the user using an input function and then call and print the defined function to get the user's age as output. Here is how the program should behave:
"""

def calculate_age(year_of_birth, current_year=2023):
    return current_year - year_of_birth


year = int(input("What is your year of birth? "))

print(calculate_age(year))
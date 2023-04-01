"""
We have the same list:

ranking = ['John', 'Sen', 'Lisa']

This time you need to create a program that:

1. Contains the above list.

2 Prompts the user to input the person's name.

3. Returns the rank that person has.

For example:
"""

ranking = ['John', 'Sen', 'Lisa']

user_promt = input("Enter a name: ")
rank = ranking.index(user_promt) + 1
print(rank)
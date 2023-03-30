"""
Create a program that prompts the user to input their name repeatedly. Then, the program repeatedly prints out the name with the first letter capitalized.

In other words, the program should behave as in the screenshot below:

(in folder with same name)
"""
#name = ""  no reason to declare it

while True:
    name = input("What is your name?")
    print(name.capitalize())

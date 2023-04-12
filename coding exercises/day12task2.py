"""
Create a script that asks the user to enter a password. Then create a function that checks the strength of the user password. The function should return Strong Password if all of the following conditions are true:

Eight or more characters

At least one uppercase letter.

At least one digit.

Here is what happens when the user provides a password that satisfies all three conditions:


And if the user enters a password that breaks one of the three conditions, the program returns Weak Password:


Note:  You can use the code we developed in the Bonus Example on Day 9.  For your convenience, you can find the code we developed in that video attached to the lecture resources of this article.
"""

password = input("Enter new password: ")

def check_pass(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["upper-case"] = uppercase
    return result


if all(check_pass(password).values()):
    print("Strong Password")
else:
    print("Weak Password")
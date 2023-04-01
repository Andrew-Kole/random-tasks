"""
Create a program that:

1. Prompts the user to input a (dollar) amount.

2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.

3. Prints out the amount in euros, as shown in the screenshot below.
"""

user_prompt = float(input("How many dollars have you got?"))
print("The amount of euros is: \n" , user_prompt * 0.95)
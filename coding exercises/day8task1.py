"""
Note: This is a very challenging exercise. Do not worry if you can't get it right. Just try to code until you get bored. The sole experience of trying to code helps your learning a ton.

A client wants to buy a coin-flip probability program from you.

The programs should work like this:

1. The user runs the program. The program asks the user to enter "head" or "tail".  The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail". The user does the same over and over again.




In each cycle, the program should return the current percentage of heads in the program, similar to what you see in the screenshot above. Also, you should write each user entry (i.e., head or tail) in a text file using a with-context manager, one entry per line.
"""

while True:
    with open("../files/coin.txt", "r") as file:
        coins = file.readlines()

    coin = input("head or tail?")+"\n"
    coins.append(coin)

    with open("../files/coin.txt", "w") as file:
        file.writelines(coins)

    number = coins.count("head\n")
    percents = number / len(coins) * 100

    print(f"Heads: {percents}%")
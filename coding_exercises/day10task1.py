"""
Build a percentage calculator that gets from the user the "total value" and the "value" and returns the percentage as shown below:


The program should also print a message if the user doesn't enter a number for the "total value or for the "value":


"""
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = value / total_value * 100


    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
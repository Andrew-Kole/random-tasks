"""
Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter.
"""

def convert(liters):
    cubic = float(liters) / 1000
    return cubic

liters = input("Enter number of liters: ")

print(f"{liters} liters is equal to {convert(liters)} cubic")
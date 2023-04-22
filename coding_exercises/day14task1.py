"""
Create a function that finds out the state of water (i.e., gas, liquid, solid) given the temperature. In other words, the function has a temperature parameter and returns either "Gas", "Liquid" or "Solid" as a string depending on the temperature. The function should be written in a separate file from the command line interface file. The output should look like in the screenshot below:


Let's run it one more time. Here is another example:


Note: To check if a value is between two values, you can use elif 0 < x < 100:
"""
from modules.func_for_day14task1 import water_statement

water_temperature = input("Enter water temperature: ")
result = water_statement(int(water_temperature))
print(result)
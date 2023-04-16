"""
In coding exercise 1, we hardcoded the values 0 and 100. It is better to change them to constants in the script where the function is defined. Therefore, your task is to modify the script from exercise 1 by creating two global variables/constants in that file, one variable associated with 0 and another associated with 100. Then, use those variables in the function instead of the values.
"""

from modules.func_for_day14task1 import water_statement_with_parametrs

water_temperature = input("Enter water temperature: ")
result = water_statement_with_parametrs(int(water_temperature))
print(result)
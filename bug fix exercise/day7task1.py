"""
The code below tries to write the items of temperatures each in one line in the file.txt list. However, the code has an error. Try to fix the error.

temperatures = [10, 12, 14]

file = open("file.txt", 'w')

file.writelines(temperatures)
"""

temperatures = [10, 12, 14]

file = open("../files/day7task1.txt", 'w')

for temperature in temperatures:
    file.writelines(str(temperature)+"\n")
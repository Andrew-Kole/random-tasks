"""
Write a program that reads the essay.txt file and returns the number of characters contained in the file.
"""

file = open("../files/essay.txt", "r")
print(len(file.readline()))
file.close()
"""
Write a program that gets a list of names from the user and returns the number of names given. You are encouraged to use a function. Here is how the program would work:
"""
names = input("Type names separated by comas: ")


def get_names(arg_names):
    names_list = arg_names.split(",")
    return names_list


def count_names(arg_names_list):
    return len(arg_names_list)


print(count_names(get_names(names)))

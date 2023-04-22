"""
Please download the members.txt file from the resources of this article.

Then, create a program that, whenever executed, asks the user to enter a new member in the command line:


Then, the member is added to members.txt. In this case, the text file content would be:

John Smith

Sen Lakmi

Sono Octonot

Solomon Right
"""
name = input("Add a new member: ")
file = open("../files/members.txt", "r")
existing_names = file.readlines()
file.close()

existing_names.append(name + "\n")
file = open("../files/members.txt", "w")
existing_names = file.writelines(existing_names)
file.close()



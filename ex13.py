# imports the arguments module from sys
from sys import argv
# read the WYSS section for how to run this
# this gives the first argument of the script name, followed by the vars first, second, and third from the command line
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
party = input("Do you like to party? ")
print(party)
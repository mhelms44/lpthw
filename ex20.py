# import argv from sys
from sys import argv
# sets the arguments as the script name and an input file, in this example I'm passing ex20.txt
script, input_file = argv
# creates first function, which reads the file and prints it. 
def print_all(f):
    print(f.read())
# creates second function, which "rewinds" the file back to the start
def rewind(f):
    f.seek(0)
# creates the last function that reads the file one line at a time using the line_count and incrementing it by one
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = '\n')
# Opens the "input_file" into the buffer, first set by the argument passed at runtime.
current_file = open(input_file)
# Prints the entire file using the print_all function
print("First let's print the whole file:\n")
print_all(current_file)
#Runs the rewind function to go back to the start of the file
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
#Runs the print_a_line function, which prints one line at a time.
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
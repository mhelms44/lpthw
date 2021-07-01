#imports the argument module from sys
from sys import argv
#arguments that we need for this python script, the script name and the filename we want to read
script, filename = argv
#creates a variable called txt that gets the output from the open(filename) function
txt = open(filename)
#prints out the name of the file we passed as an argument
print(f"Here's your file {filename}:")
#uses read() to read the output stored in txt.
print(txt.read())
#Prints a string for us to type the filename again
print("Type the filename again:")
#gets input with a > prompt and stores in in file_again
file_again = input("> ")
#sets a var called txt_again with the open() function on the file name
txt_again = open(file_again)
#prints the file name again by using the read() function
print(txt_again.read())
txt.close()
txt_again.close()
input("Files closed \nPress any key to exit...")
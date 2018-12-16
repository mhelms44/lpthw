from sys import argv
#sets arguments for argv, which we imported from sys. This gives us the script name and we supply a filename. 
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
#loads the file into a buffer and the 'w' opens it for writing, creates the file if it doesnt exist and truncates it. 
# We could leave out the 'w' option if we wanted to but since we plan to empty the file and overwrite it anyway, 'w' gives us some sanity there. 
target = open(filename, 'w')
#print("Truncating the file. Goodbye!")
#empties the file
#target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#uses the write() function to write the variables we got through keyboard input earlier to the file
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
#closes the file at the end of the writes. 
target.close()
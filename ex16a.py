from sys import argv
script, filename = argv

print("We are now going to print the file you just provided")
print(f"The file name is {filename}")
input("Press enter to continue....")

target = open(filename, 'r')
print(target.read())
target.close()
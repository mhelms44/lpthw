# imports argument support from sys
from sys import argv
# sets the arguments to be passed when the script is run
script, user_name, status = argv 
# sets up a var named prompt that we use with input() later on
prompt = 'How would you like to respond? '
#uses .format() to add variables to the first string from the arguments
print("Hi {0}, I'm the {1} script, and it looks like your status is...{2}".format(user_name, script, status))
#just a string
print("I'd like to ask you a few questions.")
#uses f-string to ask the user_name supplied as an argument a question
print(f"Do you like me {user_name}?")
#sets variable likes to the input which is prefaced with the prompt var
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {0} about liking me.
You live in {1}. Not sure where that is.
And you have a {2} computer. Nice.""".format(likes, lives, computer))
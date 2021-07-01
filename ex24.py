list# prints out a string
print("Let's practice everything.")
# prints string with an escape character for the ' marks and the \
print('You\'d need to know \'bout escapes with \\ that do:')
# uses \n and \t for a new line and a tab
print('\n newlines and \t tabs.')
# using """ in a block allows us to put whatever we want in between. We use this to create a string of text formated the way we want.
poem = """
\t The lovely world
with logic so firmly planeted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none
"""
# prints out a - 50 times
print("-" * 50)
# prints our poem var we set earlier
print (poem)
# prints out a - 50 times
print("-" * 50)
# creates a var named five and sets it to the value of 5 using an equation
five = 10 - 2 + 3 - 6
# prints the value of five using an f string
print(f"This should be five: {five}")
# creates a function named secret_formula that takes started as its argument
# by the end of the function we return the value of jelly_beans, jars, and crates.
def secret_formula(started):
    beans = started * 500
    jars = beans / 1000
    crates = jars / 100
    return beans, jars, crates

# sets the value of start_point, which we then pass to secret_formula by calling it on the next line
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
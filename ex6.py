#sets the value of types_of_people
types_of_people = 10
#creates variable x that is a formated string with the types_of_people variable
x = f"There are {types_of_people} types of people."
#creates a variable called binary that is a string binary
binary = "binary"
#creates a variable called do_not that contains the string don't
do_not = "don't"
#creates a variable y with a formated string containing the two variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."

#prints variable x
print(x)
#prints variable y
print(y)

#prints a formated string for variable x which contains formatted strings
print(f"I said: {x}")
#same thing with printing variable y
print(f"I also said: '{y}'")
#creates a variable called hilarious and sets it to false
hilarious = False
#creates a joke_evaluation variable with a formatted string and an empty variable
joke_evaluation = "Isn't that joke so funny?! {}"
#prints the joke evaluation with the format syntax using the hilarious boolen variable
print(joke_evaluation.format(hilarious))

#creates a string in variable w
w = "This is the left side of..."
#creates a string in variable e
e = "a string with a right side."
#prints the two variables each containing a string
print(w + e)

# sets value of people to 30
people = 30
# sets value of cars to 40
cars = 40
# sets value of trucks to 15
trucks = 15
# first if statement elvauates if cars is greater than people, if true it prints out a string.
if cars > people:
    print("We should take the cars.")
# elif is python's version of "else if". If the first if statement isn't true and we keep going through the program it will evaluate this statement next
elif cars < people:
    print("We should not take the cars.")
# if we get through all the conditional statements and none of them are true, else is our catch all that will always work if nothing else does. 
else:
    print("We can't decide!")

if trucks > cars:
    print("That is too many tucks.")
elif trucks < cars and cars < people:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, lets just take the trucks")
else: print("Fine, lets stay home then")
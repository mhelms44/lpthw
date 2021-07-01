# creates a list called the count with 5 ints in it
the_count = [1, 2, 3, 4, 5]
# creates a list called fruits with 4 strings in it
fruits = ['apples', 'oranges', 'pears', 'apricots']
# creates a list called change with a mix of strings and ints
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# "for number" could be "for foo" or whatever else we want. 
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we dont know whats in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# no need to use a for loop to add a range to a list. Just set the list to the range. 
test = range(0, 6)

for i in test:
    print(f"Here is my test: {i}")


# now we can print them out too
for i in elements:
    print(f"Elements was: {i}")
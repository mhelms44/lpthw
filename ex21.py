# Creates a function named add that takes two arguments when called, prints a strong, and then returns the value of a + b
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b 

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a}  {b}")
    return a / b

print("Lets do some math with just functions!")
# We can set variables to have values from functions. In this case we are calling functions and then setting whatever they return as the variable value. 
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide (200, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit
print("Here is a puzzle")
# Sets the variable what using our functions and variables previously created
# 35 + 74 - 180 * (100 / 2)
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

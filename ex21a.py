# Testing out getting input from user and passing that to a function
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

print("Enter two numbers.")
a = float(input("Number 1: "))
b = float(input("Number 2: "))

value = add(a, b)
print (value)
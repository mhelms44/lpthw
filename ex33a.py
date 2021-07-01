# Creating ex33 using a function
# Also lets user supply the starting, stopping, and loop increment values at start

def list_fill(starter, stopnumber, increment):
    i = starter
    x = stopnumber
    y = increment
    numbers = []
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

starter = int(input("What number do you want to start with? "))
stopnumber = int(input("What number do you want the loop to stop with? "))
increment = int(input("How much should the loop increment by every time it runs? "))
list_fill(starter, stopnumber, increment)
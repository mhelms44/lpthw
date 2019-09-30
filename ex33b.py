# Rewriting ex33a as a for loop

def list_fill(starter, stopnumber):
    i = starter
    x = stopnumber

    numbers = range(i, x)

    for num in numbers:
        print(num)

starter = int(input("What number do you want to start with? "))
stopnumber = int(input("What number do you want the loop to stop with? "))
list_fill(starter, stopnumber)
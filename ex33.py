# creates variable i and sets it to 0
i = 0
# creates a list called numbers that is currently empty
numbers = []
# while loop that runs as long as i is less than 6
while i < 6:
    print(f"At the top i is {i}")
    # uses the append function on the list to add in whatever number we currently have in the loop
    numbers.append(i)
    # increments the value of i by 1 ever loop
    i = i + 1
    print("Numbers now: ", numbers)

    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
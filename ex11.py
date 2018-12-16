#Sets a var of age and uses the input function to print out a string and then take input
age = input("How old are you? ")
height = input("How tall are you in inches? ")
weight = input("What is your weight? ")

#prints out the variables using the format() function for age, height, and weight. 
#print("So, you are {0}, you are {1} tall, and weigh {2} pounds.".format(age, height, weight))
print(f"So, you are {age}, you are {height} inches tall, and weigh {weight} pounds.")
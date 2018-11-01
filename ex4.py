#total cars we have
cars = 100
#how many people fit in the car, as a float
space_in_a_car = 4
#how many drivers we have
drivers = 31
#how many passengers we have
passengers = 90
#how many cars we have not being driven
cars_not_driven = cars - drivers
#we get the number of cars driven from the number of drivers
cars_driven = drivers
#how many people we can transport in the total number of cars we have
carpool_capacity = cars_driven * space_in_a_car
#what the average number of people per car will be
average_passengers_per_car = passengers / cars_driven

#prints the number of cars avaliable
print("There are", cars, "cars available.")
#prints the number of drivers avaliable
print("There are only", drivers, "drivers available.")
#prints how many empty cars not being driven we have
print("There will be", cars_not_driven, "empty cars today.")
#prints the total carpool capacity we have
print("We can transport", carpool_capacity, "people today.")
#prints the number of passengers we have
print("We have", passengers, "to carpool today.")
#prints the average passenger count per car
print("We need to put about", average_passengers_per_car, "in each car.")
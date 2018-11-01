#creates a var named forammter that has four brackets for holding a variable/string
formatter = "{} {} {} {}"

#uses the format function with formatter to hold 4 ints.
print(formatter.format(1, 2, 3, 4))
#same as before but this time with strings
print(formatter.format("one", "two", "three", "four"))
#prints out True/False keywords held in formatter used with the format function
print(formatter.format(True, False, False, True))
#this prints out formatter four times, so 12 brackets in total all empty.
print(formatter.format(formatter, formatter, formatter, formatter))
#four strings held by formatter we print out using the format function
print(formatter.format(
    "We can put literally anything we want to put here, it doesn't matter.",
    "At least you would think.",
    "High level programming languages have their problems",
    "But at least this isn't Java!"
))
name = 'Michael Helms'
age = 25 # not a lie
height = 74 # inches
height_cm = height * 2.54 # height in CM
weight = 200 # lbs
weight_kg = (1 / 2.2) * weight # roughly the weight in KG
rounded_weight_kg = round(weight_kg)
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"Or, {height_cm} centimeters tall in the EU.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"Sounds a little better in kilograms at {rounded_weight_kg}")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
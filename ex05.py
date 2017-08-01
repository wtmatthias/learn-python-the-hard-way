# ex05.py

name = 'Zed A. Shaw'
age = 35
height = 74  # in inches
weight = 180  # in lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_cm = round((height * 2.54), 2)  # rounds 'height_cm' to 2 digits
weight_kg = round((weight * 0.453592), 2)  # rounds 'weight_kg' to 2 digits

print(f"Let's talk about {name}.")
print(f"He's {height} inches or {height_cm} centimeters tall")
print(f"He's {weight} pounds or {weight_kg} heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
total_met = age + height_cm + weight_kg  # added total w/ metric conversions
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total_met}.")

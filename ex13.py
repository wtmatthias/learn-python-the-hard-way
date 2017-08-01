# ex13.py

from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
first_def = input(f"What does {first} mean?") # passing the variable name to the input string
print("Your second variable is:", second)
second_def = input(f"What does {second} mean?")
print("Your third variable is:", third)
third_def = input(f"What does '{third}' mean?")

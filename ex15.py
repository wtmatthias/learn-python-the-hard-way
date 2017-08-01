# ex15.py

# import argv module from sys package
from sys import argv

# call the script name and the txt file name
script, filename = argv

# open 'filename' and store in 'txt' variable
txt = open(filename)

# reads text from the file directly into terminal
print(f"Here's your file {filename}:\n") # put \n for easier reading of .txt file
print(txt.read()) # call the .read function to 'txt'

# ex17-1.py
# version 1 of ex17 (i.e. verbatim from manual)
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file).read()

print(f"The input file is {len(in_file)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print("Alright, all done.")

out_file.close()
# in_file.close()
# don't need to write above line b/c line11 uses open().read(), which closes after reading

# NOTE: you can create a new .py script for ex17 to write a shorter version. and you can use this script to copy the 1st version over to a new version. like this...
# > python ex17-1.py ex17-1.py ex17-2.py

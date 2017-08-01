# ex17-2.py
# version 2 of ex17 - much shorter recreation
from sys import argv
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}...")

# writes/copies file if doesn't exist & interupts (w/ error) if it already exists
out_file = open(to_file, 'x').write(open(from_file).read())

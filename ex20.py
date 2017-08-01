from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

# `.seek()` changes the starting point ('N' - in bytes) for next operation
# `rewind(f)` moves 'f' to the 0 byte position
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end ='')

current_file = open(input_file)


print("First let's print the whole file: \n")

# "end=''" is a call to avoid printing an extra "\n" at the end of each line
# .readline() default is to return the \n (new line)
print_all(current_file)


print("Now let's rewind, kind of like a tape. \n")

rewind(current_file)


print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

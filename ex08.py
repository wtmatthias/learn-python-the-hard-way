#ex8.py

formatter = "{} {} {} {}"

print(formatter .format(1, 2, 3, 4))
print(formatter .format("one", "two", "three", "four"))
print(formatter .format(True, False, False, True))
print(formatter .format(formatter, formatter, formatter, formatter))
print(formatter .format(
    "I'm trying my own",
    "text right here",
    "in an attempt to learn",
    "the '.format' function."
))

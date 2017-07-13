# ex5.py

name = 'Zed A. Shaw'
age = 35
height = 74.0  # in inches
weight = 180.0  # in lbs
eyes = "Blue"
teeth = 'white'
hair = 'Brown'

height_cm = height * 2.54
weight_kg = weight * 0.4536

print "Let's talk about %s" % name
print "He's %d centimeters tall." % height_cm
print "He's %d kilograms heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_cm, weight_kg, age + height_cm + weight_kg)

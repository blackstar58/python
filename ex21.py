import math
	

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b * 10

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

def pencil(a):
	print "The SQRT of %d" % (a)
	return math.sqrt( a )

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
cat = pencil(9)

print "Age: %d, Height: %d, Weight: %d, IQ: %d SQRT: %d" % (age, height, weight, iq, cat)

#A puzzle for the extra credit , type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
how = age + (height - (weight * (iq/2)))
when = multiply(age, add(height,iq))

print "That becomes: ", what, "Can you do it by hand?"
print "What is when: %d" % when
print "This is the result of how: %d" %how
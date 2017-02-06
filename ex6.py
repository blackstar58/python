# assign a value to x  
x = "There are %d types of people." % 10
# assign a value to binary
binary = "binary"
#assign a value to do_not
do_not = "don't"
# assign a value to y - 1
y = "Those who know %s and those who %s." %(binary, do_not)
#print the value of x
print x
#print the value of y
print y

#print value of x including a string to the start
print "I said: %r." %x
#print valur of y including a string to the start
print "I also said: '%s'." %y

#assign a value of false to hilarious
hilarious = False
#assign a string to variable joke evaluation - 2
joke_evaluation = "Isn't that joke so funny?! %r"

#print the combination of joke_evaluation and hilarious
print joke_evaluation % hilarious

#assign a value to variable 
w = "This is the left side of..."
#assign a value of variable to e
e = "a string with a right side."

#print the values of w plus e
print w + e
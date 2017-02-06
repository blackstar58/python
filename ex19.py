# This defines a function called cheese_and_crackers, which takes two variables , cheese_count and boxes_of_cracker
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#print the variable passed in with cheese_count
	print "You have %d cheeses!" % cheese_count
	#print the variable passed in with boxes_of_crackers 
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#print blow statment
	print "Man that's enough for a party!"
	#print statement get a blanket for by a new line
	print "Get a blanket.\n"
	
#print this statement first in the script	
print "We can just give the function numbers directly:"
#call function defined above
cheese_and_crackers(20, 30)

#print this statement second in the script
print "OR, we can use variables from our script:"
# assign values to new variable amount_of_cheese
amount_of_cheese = 10
# assign values to new variable amount_of_crackers
amount_of_crackers = 50

#call function with new variables names, this will force the values of the variables to be passed to cheese_count and boxes_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
	
#print this statement third in the script	
print "We can even do math inside too:"
#call function with enbedded math assigned
cheese_and_crackers(10 + 20, 5 + 6)

#print this statement fourth in the script
print "And we can combine the two, variables and math"
#This takes the values assigned above and add numerical values to them 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
	
	
	
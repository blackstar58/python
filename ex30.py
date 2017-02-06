people = 30
cars = 40
buses = 15

if cars > people:
#if the value of cars is greater than the value of people	
	print "We should take the cars."
#print above statement	
elif cars < people:
#if the if statement is not valid then compare it to the next statement
#if the value of cars is less than people 
	print "We should not take the cars."
#print the value above	
else:
#if the above two statement are not met then the else statement will be the default	
	print "We can't decide"
#print the value above	
	

if buses > cars:
#This is the first if statement , if this is true then print value below 
	print "That's too many buses."
#print the value above	
elif buses < cars:
#If the above statement is not met then do the comparison above
	print "Maybe we could take the buses."
#print the above statement	
else:
#if all the other comparisions are not met , the is the default	
	print "We still can't decide."

if people > buses:
	print "Alright, lets just take the buses."
else:
	print "Fine, let's stay home then."
	
	
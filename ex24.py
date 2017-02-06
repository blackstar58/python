print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

#assign value to poem
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none. 
"""

print "--------------"
#print dashes
print poem
#print value assigned to poem
print "--------------"
#print dashes

five = 10 - 2 + 3 - 6
#do aritmatic and assign value to five
print "This should be five: %s" % five
#print value of five
def secret_formula(started):
#create function secret_formula
#takes value started

	jelly_beans = started * 500
#multiple started by 500 assign to jelly bean
	jars = jelly_beans / 1000
#divide jelly_beans by 1000 and assign to value jars
	crates = jars / 100
#divide jars by 100 assign to crates
	return jelly_beans, jars, crates
#return all functions back to user

start_point = 10000
#assign 10k to start_point
beans , jars, crates = secret_formula(start_point)
#assign result of function secret_formula to beans, jars, crates
print "With a starting point of: %d" %start_point
#print the vaue of start_point
print "We'd have %d beans, %d jars, and %d crates. " % (beans, jars, crates)
#prints the value of beans , jars, crates this is before the divison by 10 

start_point = start_point / 10
# This takes the value of start point and divides by 10

print "We can also do that this way:"
#This prints the statement above
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
#This send the value of start_point into the function secret_formula then prints the return value









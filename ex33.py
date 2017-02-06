i = 0
numbers = []
x = 10
test(x,3)

def test(r,y):
	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)
		print (y)
		i = i + y
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	
	
print "The numbers: "

for num in numbers:
	print num
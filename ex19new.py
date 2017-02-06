def max_weight(items, weight):
	print "There are %d items." %items
	print "Each weight exactly %d amount." %weight
	print "The total weight is %d amount.\n" %(items*weight)


print "First version of this input:"
max_weight(22, 33)

print "Second version of this input:"
newitems = 40
newweight = 100
max_weight(newitems, newweight)

print "Third version of the input:"
max_weight(14+10, 40+22)

print "Fourth version of the input:"
max_weight(newitems+20, newweight+33)

print "Fifth version of the input:"
seconditem = 10
max_weight(seconditem, newweight+seconditem)

print "Sixth version of the input:"
max_weight(5*29,33*18)

print "Seventh version of the input:"
fine = 100
ok = 300
max_weight(fine, ok)

print "Eigth version of the input:"
max_weight(fine+2, newweight)

print "ninth version of the input:"
max_weight(33, 22.30)

print "Tenth version of the input:"
max_weight(seconditem, newweight)
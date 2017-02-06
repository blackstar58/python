name = 'Ahmed Ismail Syed'
age = 35 # not a lie
height = 76 #inches
weight = 190 #lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'
kg_weight = weight / 2.2
m_height = (height * 2.2) / 100 

print "Let's talk about %r. " % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth
print "His weight in KG is %f." % kg_weight
print "His height in meters is %f" % m_height

#this line is tricky, try to get it exactly right 
print "If I add %d, %d, and %d I get %f." %(
    age, height, weight, age + height + round(weight))
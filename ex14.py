from sys import argv

script,user_name,age = argv
prompt = 'Zork is god: '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer you have?"
computer = raw_input(prompt)

print """
Allright, so you said %r about liking me. 
You live in %r. Not sure where that is. 
And you have a %r computer. Nice.
What is your %r ?
""" % (likes, lives, computer,age)
#This import from the system the argv tool set
from sys import argv

#This takes the script name provided in command line and assigns it to filename
#script, first = argv

#This is a raw_input
print "Type the file name:"
filename = raw_input("> ")


#This is a special function , it take txt function and assigni it to the content of the file name
#Open is a action that you can do to the file name 


txt = open(filename)

#prints the file name to the command line
print "Here's your file %r:" % filename
# This is a special function , this print the content of the file assigned to the txt function
# read allows you to parse this file , so it can be read , (read file ), from file assigned to text 
# Then print it out 
print txt.read()
txt.close()

#This is a command promopt for the user to retype the file name 
print "Type the filename again:"
#This presents a chevron to the use and takes their input and assigns to a file 
file_again = raw_input("> ")




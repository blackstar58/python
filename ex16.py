#import argv function from syste
from sys import argv

#provide script name , filename that is provided by the user
script, filename = argv

#print following messages (filename included in this message)
print "We're going to erase %r." % filename
# print the above message , ctrl c will exit python
print "If you don't want that, hit CTRL-C (^C)."
#print message return will contiune 
print "If you do want that , hit RETURN."

#print question mark , since user input is an action and not a file nothing is needed
raw_input("?")

#orint open file
print "Opening the file..."
#open target file, provided by user in filename , w is to write to the file ,and truncate at the sametime
#assign value to target , this is the filename 
target = open(filename, 'w')

#print statement , truncating filename
print "Truncating the file. Goodbye!"
#trucate file 
target.truncate()

#print statment , please provide three lines
print "Now I'm going to ask you for three lines"

#assign values to object from raw input , each is printed seprately
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

newline = "%s\n%s\n%s" %(line1,line2,line3)
#print "This is a new line %r", newline


#print statment , print line
print "I'm going to write these to the file."

#write content of line1 to file
#target.write(line1)
#print nextline content
#target.write("\n")
#print content of line2 to file
#target.write(line2)
#print nextline value
#target.write("\n")
#print content of line3 to file
#target.write(line3)
#print next line indecation
#target.write("\n")

#target.write(newline)
target.write("%s\n%s\n%s" %(line1,line2,line3))

#print below statment to file
print "And finally, we close it."
#close filename 
target.close()
# Import Argument function for sys stack
from sys import argv
# The file requires the script name and the input fie , the input file is treated and loaded into argument
script, input_file = argv

# create function print all that accepts a variable called "f"
def print_all(f):
	# Read content of f with read function and print to console
	print f.read()

# create function rewind that takes variable "f"
def rewind(f):
	# find the position '0' in the variable 
	# what is seek?
	f.seek(0)

# create functiont that prints out the entire content of the file , get the starting position and the file name 
def print_a_line(line_count, f):
	# print the value of line count and print value of line being read
	print line_count, f.readline()
	
# assign the value of current_file , this should be the input file that was submited within the arguments
current_file = open(input_file)

# print the below statment and the input and then skip a line 
print "First let's print the whole file:\n"

# print the entire value of current_file , this should the file specified by the input_file argument
print_all(current_file)

# print the below statement
print "Now let's rewind, kind of like a tape."

# run rewind function on current file , this should find the position 0 of the file
rewind(current_file)

#print below statement 
print "Let's print three lines:"

# assign value of current line to 1
current_line = 1 # current line value is 1
# pass the value of current line and the value of current file which is the file from the argument
print_a_line(current_line, current_file)

# assign value of current line to 2 , add 1 to value of current line
current_line += 1 # current line value is 2
# pass the value of current line and value of current file which is the file from the argument
print_a_line(current_line, current_file)

# assign vaue of current line to 3 , add 1 to value of current line
current_line += 1 #current line value is 3, value is converted into variable line_count when print_a_line is called
# pass the value of current line and value of current fule which is the file from the argument
print_a_line(current_line, current_file)

def break_words(stuff):
	"""This function will break up words for us."""
	#split the value of stuff into an array looking at spaces
	words = stuff.split(' ')
	#returns arrary called words
	return words

	#alphebeically sorts the array words
def sort_words(words):
	"""Sorts the words."""
	#return an alpaabeically sorted array of words array
	return sorted(words)


	#This function print the first value of the words feature
def print_first_word(words):
	"""Prints the first word after popping it off."""
	#take the first value of the array and assign to word
	word = words.pop(0)
	#prints value of variable words
	print word

	#This function will print the last word from the array words
def print_last_word(words):
	"""Prints the last word after popping it off."""
	#remove the last element of words list using -1 and assign to variable word
	word = words.pop(-1)
	#print the value value of word 
	print word

	#This function will sort the value of sentence and return a list
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	#after running the value of sentence through the break_words function assign it to words
	words = break_words(sentence)
	#take the value of words and pass to the sort_words function
	return sort_words(words)

	#same as function below but without the sorting 
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence. """
	words = break_words(sentence)
	#take the value of words and pass it to the print_first_word function
	#within in print_first_word function remove the first word and print to screen
	print_first_word(words)
	#take the value of words and pass it to the print_last_word function 
	#within the print_last_word function remove the last word and print to screen
	print_last_word(words)
	
	#sort a sentence and print the first and last word , this calls other function within the module 
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one. """
	#take the value of sentence and run it through sort_sentence function and then assign to words element
	#within the sort_sentence function break the sentence into a list by identifying spaces
	words = sort_sentence(sentence)
	#take the value of words and pass it to the print_first_word function
	#within in print_first_word function remove the first word and print to screen
	print_first_word(words)
	#take the value of words and pass it to the print_last_word function 
	#within the print_last_word function remove the last word and print to screen
	print_last_word(words)
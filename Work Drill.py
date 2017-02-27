Word Drill - 

Class - Tell Python to make a new kind of thing
Object - Two meanings: the most basic kind of thing, and any instance of some thing. 
Instance - What you get when you tell python to create a class
def - How you define a function inside a class
self - Inside the functions in a class, self is a variable for the instance/object being accessed
inheritance - The concept that one class can inherit traits from another class, much like you and your parents
composition - The concept that a class can be composed of other classes as parts , much like how a car has wheels
attribute - A property classes have that are from composition and are usually variables
is-a - A phrase to say that something inherits from another , as in a "salmon: is-a "fish"
has-a - A phrase to say that something is composed of other things or has a trait , as in "a salmon has-a mouth"


Phrase Drill - 

class X(Y) - make a class named X that is-a Y
	class Song(object):
		
class X(object): def __init__(self,J) - class X has-a __init__ that takes self and J parameters
	def __init__(self, lyrics):	
		
class X(object): def M(self,J) - class X has-a function named M that takes self and J parameters
	def sing_me_a_song(self):
		
foo = X() - Set foo to an instance of class X
happy_bday = Song(["Happy birthday to you",
				  "I don't want to get sued",
				  "So I'll stop right there"])

foo.M(J) - From foo get the M function , and call it with parameters self, J
happy_bday.sing_me_a_song(queen)

foo.K = Q - From foo get the K attribute , and set it to Q



Substitution Drill - 

Make a class named ??? that is-a Y
class ??? has-a __init__ that takes self and ??? parameters
class ??? has-a function named ??? that takes self and ??? parameters
Set foo to an instance of class ???
From foo get the ??? function, and call it with self=??? and parameters ???
From foo get the ??? attribute and set it to ???


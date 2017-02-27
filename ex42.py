## Animal is-a object (yes, sort of confusing) look at the extra credit 

class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## def has a __init__ with attribute of self and name
		## self has a name which is equal to name
		self.name = name

##Cat is-a Animal 
class Cat(Animal):
	
	def __init__(self, name):
		##def has a __init__ with attributes of self and name
		## self has a name which is equal to variable name
		self.name = name

##Person is-a object
class Person(object):
	
	def __init__(self, name):
		##self has-a name which is equal to variable name
		self.name = name
		
		##Person has-a pet of some kind
		self.pet = None

##employee is a person
class Employee(Person):
	
	def __init__(self, name, salary):
		## Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class.
		
		super(Employee, self).__init__(name)
		##self has a salary and is equal to variable salary
		self.salary = salary

##Fish is a object
class Fish(object):
	pass

#Halibut is a Fish
class Halibut(Fish):
	(pass)

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

##pet attribute of mary set ot satan
mary.pet = satan

## frank is a employee instance with attributes of Frank and 120000
frank = Employee("Frank", 120000)

## pet attribute of frank is-a rover
frank.pet = rover

## flipper is a instance of Fish
flipper = Fish()

## crouse is a instance of Salmon
crouse = Salmon()

## harry is a instance of Halibut
harry = Halibut()

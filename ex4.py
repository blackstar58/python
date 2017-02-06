# variable cars are assigned to 100
cars = 100

#The number of spaces in a car
space_in_a_car = 4

#The total number of drivers
drivers = 30

#This is the passangers variable
passengers = 90

#variable the takes drivers and substracts from the number of cars
cars_not_driven = cars - drivers

#number of cars that are being driven 
cars_driven = drivers

#How many people can fit into the number of cars that are being driven
carpool_capacity = cars_driven * space_in_a_car

#Total number of passangers that can fit in all the cars
average_passengers_per_car = passengers / cars_driven

#print statement and the value of cars
print "There are", cars, "cars avalible."

#print the number of drivers avalible 
print "There are only", drivers, "drivers avalible."

#print the number of cars not driven
print "There will be", cars_not_driven, "empty cars today."

#print the carpool capacity
print "We can transport", carpool_capacity, "people today."

#print the number of passengers avalible
print "We have", passengers, "to carpool today."

#print the average number of passangers per car
print "We need to put about", average_passengers_per_car, "in each car."

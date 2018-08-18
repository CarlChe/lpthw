# cars we have
cars = 100

#volumn capacity per car
space_in_car = 4.0

#drivers we have
drivers = 30

#all passengers
passengers = 90

#cars not in use
cars_not_driven = cars - drivers

#cars in use
cars_driven = drivers

#cargo capacity
carpool_capacity = cars_driven * space_in_car

#average passengers in running car
average_passengers_per_car = passengers / cars_driven



print("There are", cars, "cars available.")

print("there are only", drivers, "drivers available.")

print("There will be", cars_not_driven, "empty cars today.")

print("We can transport", carpool_capacity, "goods today.")

print("We have", passengers, "to carpool today.")

print("We need to put about", average_passengers_per_car, "in each car.")

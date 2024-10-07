#example creating objects from a class - define function - set parameters
class Point:   #define new class / blueprint

    def __init__(self, x, y):  # define function / self method. set parameters - attributes
        self.x = x              #X and Y are instance variables
        self.y = y              #self is object and can be any name. self typically used.

    def falls_in_rectangle(self, lowerleft, upperright):  # define function and self method and set parameter
        if lowerleft[0] < self.x < upperright[0] and lowerleft[1] < self.y < upperright[1]:
            return True
        else:
            return False

    def distance_from_point(self, x, y):
        return ((self.x - x) **2 + (self.y - y)**2) ** 0.5

point1 = Point(1,1)     # create object instance with arguments
print(point1.x, point1.y)     #print arguement values

point2 = Point(6,7)
print(point2.x, point2.y)
results = point2.falls_in_rectangle((4,5), (8,9))
print(results)

print(point1.distance_from_point(1,10))

##########################################################################
#Create a program that calculates
# the number of paint buckets a customer needs to paint their wall area.
# To make this program, we will need to create a Paint class and a House class.
#
# We decided to have a House class and a Paint class for our house painting cost
# calculator program. In our program, the responsibility of the House class
# will be the calculation of the number of paint buckets needed
# to paint the entire house and the responsibility of the
# Paint class will be the calculation of the total price of the paint.
#
# 1. Add a paint_needed method to House
# 2. Let us suppose that 2.5 buckets of paint are needed to paint one square unit of a wall.
# Therefore, inside the paint_needed method you should multiply 2.5 with the self.wall_area and return the value.
# That value is the paint needed to paint the house.
# Specifically, your task is to:
# 1. Create a total_price method inside Paint. The method should only have a self parameter.
# 2. The total_price method should calculate and return the total price given the number of buckets for
# two scenarios - when color is 'white' and when it is not.
# The price of white paint is 1.99 and the price for color paint is 2.19.
#
class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return self.wall_area * 2.5

class Paint:

    def __init__(self, buckets, color):
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19
amount = House(10)
print(amount.paint_needed())
totalColor = Paint(amount.paint_needed(), "white")
print(totalColor.total_price())

#######################################################

cj = "john john. john john".capitalize()         #methods are what make objects useful
print(cj)
cj = "john john john".count("j")                #methods are what make objects useful
print(cj)

#######################################################



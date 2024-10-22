#Write a function that takes in one integer parameter, the
#side length of a square, and returns the area. The function
#should be named find_area, and have one parameter:
#side_length.
#Write your function here!
def find_area(side_length):
    return side_length ** 2

#If your function works correctly, this will originally
#print: "A square with side length 4 has an area of 16".
test_side_length = 4
print("A square with side length", test_side_length, "has an area of", find_area(test_side_length))


def introduction(name, age):
    return "My name is " + str(name) + " and I am " + str(age) + " years old."
print(introduction(6, "Wilbert"))
# My name is 6 and I am Wilbert years old.


# Write a function called my_TAs. The function should take as
# input three strings: first_TA, second_TA, and third_TA.
# It should return as output the string, "[first_TA], [second_TA],
#and [third_TA] are awesome!", with the values replacing the
#variable names.
#
#For example, my_TAs("Sridevi", "Lucy", "Xu") would return
#the string "Sridevi, Lucy, and Xu are awesome!"
#
#Hint: Notice that because you're returning a string instead
#of printing a string, you can't use the print() statement
# -- you'll have to create the string yourself, then return
#it!
#Write your function here!
def my_TAs(first_TA, second_TA, third_TA):
    return f"{first_TA}, {second_TA}, and {third_TA} are awesome!"

#If your function works correctly, this will originally
#print: "Joshua, Jackie, and Marguerite are awesome!".
test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))


#Write a function called get_todays_date that returns
#today's date as a string, in the form year/month/day.
#For example, if today is January 15th, 2017, then it
#would return 2017/1/15.
#Remember, you took care of the string formatting part of
#this exercise in 2.2.9 Coding Exercise 1! Now, you're
#converting it to a function that returns the string.
#Note that the line below will let you access today's date
#using date.today() anywhere in your code.
from datetime import date
#Write your function here!
def get_todays_date():
    today = date.today()
    return f"{today.year}/{today.month}/{today.day}"

#If you want to test your code, you can do so by calling
#your function below. However, this is no longer required
#for grading.
print(get_todays_date())



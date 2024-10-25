#function set 3.4
#3.4.5
def say_good_night():
  name = "Jack"
  return "Good Night, " + name + " and "
say_good_night()
print("Jill")
#outputs Jill

print(say_good_night(), end = "")
print("Jill")
#outputs Good Night, Jack and Jill

def yay_TAs(ta1, ta2, ta3):
  result = ta3 + ", " + ta2 + ", and " + ta1 + " are awesome!"
  return result
my_string = yay_TAs("Jackie", "Joshua", "Marguerite")
print(my_string)
#outputs Marguerite, Joshua, and Jackie are awesome!

print(1, 2, 3, sep = "")
print(4, 5, 6, end = "$")
print()
print(7, 8, 9, sep = "!", end = "!")
print(0)
#outputs 
#123
#4 5 6$
#7!8!9!0

#HideAndSeek 3.4.1 10 of 25
#Write a function called hide_and_seek. The function should
#have no parameters and return no value; instead, when
#called, it should just print the numbers from 1 through 10,
#follow by the text "Ready or not, here I come!". Each
#number and the message at the end should be on its own
#line.
#Then, call the function.
#There should be no print statements outside the function.
#Write your function here!
def hide_and_seek():
    for i in range(1,11):
        print(i)
    print("Ready or not, here I come!")

hide_and_seek()

#ShowSelector 3.4.2 11 of 25
#Write a function called select_a_show. select_a_show
#should have one parameter, an integer representing
#how many minutes until you have to leave.
#select_a_show should return the following:
def select_a_show(n):
    if n <= 0:
        return "You're late!"
    elif n <= 10:
        return "Leave now, be early!"
    elif n <= 45:
        return "Watch a comedy!"
    elif n <= 100:
        return "Watch a drama!"
    else:
        return "Watch a movie!"
            
print(select_a_show(-5))
print(select_a_show(5))
print(select_a_show(34))
print(select_a_show(68))
print(select_a_show(124))

#semihemisphere.py Coding 3.4.3 12 of 25
def semihemisphere(x, y):
#latitude is between -90 and 90 South and Nouth poles - 0 equator
#longitude is between -180 and 180 -180 West and 180 East - 0 to 180 Eastern
    if x < 0 and y < 0: #SW
        return "Southwest"
    if x > 0 and y < 0: #NW
        return "Northwest"
    if x < 0 and y > 0: #SE
        return "Southeast"
    if x > 0 and y > 0: #NE
        return "Northeast"

#If your function works correctly, this will originally
#print Northwest, Southeast, Northeast, Southwest
print(semihemisphere(33.7, -84.4))
print(semihemisphere(-71.1, 86.3))
print(semihemisphere(67.1, 12.1))
print(semihemisphere(-11.6, -62.3))

#HideAndSeek2.py Coding 3.4.4 13 of 25
#Write your function here!
def hide_and_seek(count):
    for number in range(1, count + 1):
        print(number)
    print("Ready or not, here I come!")

#The function call below will test your function. We'll delete
#and overwrite this with other calls to hide_and_seek with
#different numbers during grading:
hide_and_seek(36)

#########################################
#LeapYear.py
def is_leap_year(year):
    # Check if the year is a leap year
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Test cases to verify the code
print("1993 is a leap year:", is_leap_year(1993))  # Expected output: False
print("1996 is a leap year:", is_leap_year(1996))  # Expected output: True
print("1900 is a leap year:", is_leap_year(1900))  # Expected output: False
print("2000 is a leap year:", is_leap_year(2000))  # Expected output: True








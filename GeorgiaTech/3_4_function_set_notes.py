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
#There should be no print statements outside the function.
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

################################
# sevens.py
#Write a function called lucky_sevens that takes in one
#parameter, a string variable named a_string. Your function
#should return True if there are exactly three '7's in
#a_string. If there are less than three or more than three
#'7's, the function should return False.
def lucky_sevens(string):
    # Count the number of '7's in the string
    count = string.count('7')

    # Return True if there are exactly three '7's, otherwise return False
    return count == 3

#Below are some lines of code that will test your function.
print(lucky_sevens("happy777bday"))
print(lucky_sevens("h7app7ybd7ay"))
print(lucky_sevens("happy77bday"))
print(lucky_sevens("h777appy777bday"))

#################################################
#idealGasLaw.py 3.4.7
# P = (nRT) / V
#
#Write a function called find_pressure that takes as input
#three variables: number of moles, temperature, and volume.
#You can call these variables in the function whatever you
#want, but they must be specified in that order: moles, then
#temperature, then volume. You should assume all three are
#floats. Then, return as output your calculation for
#pressure. For the gas constant, you should use the value
#0.082057.
def find_pressure(moles, temperature, volume):
    # gas constant
    R = 0.082057
    # Calculate pressure
    pressure = (moles * R * temperature) / volume
    return pressure

#If your function works correctly, this will originally
#print: "Result: 48.905972000000006". The extra zeroes and
#the 6 are rounding errors by Python.
test_n = 10
test_T = 298
test_V = 5
print("Result:", find_pressure(test_n, test_T, test_V))

##########################################################
# idealGasLaw2.py 3.4.8
#So, we want to *assume* that pressure is in atm (and thus,
#that R should be 0.082057), but we want to let the person
#calling our function change that if need be. So, revise
#your find_pressure function so that R is a keyword parameter.
#Its default value should be 0.082057, but the person calling
#the function can override that. The name of the parameter for
#the gas constant must be R for this to work.

# P = (nRT) / V
#
def find_pressure(n, T, V, R=0.082057):
    return (n * R * T) / V


test_n = 10
test_T = 298
test_V = 5
test_R = 62.364 #Torr!
print("Result:", find_pressure(test_n, test_T, test_V, R = test_R))

#####################################################################
# SumOfPrimes.py 3.4.9
#Write a function called sum_of_primes. sum_of_primes should
#take as input a single integer, and then it should sum all
#the prime numbers up to and including that integer.
#For example, sum_of_primes(6) would return 10: 2 + 3 + 5 = 10.
#1, 4 and 6 are not prime; 2, 3, and 5 are.
# sum_of_primes(7)  -> 17 (2 + 3 + 5 + 7 = 17)
# sum_of_primes(8)  -> 17 (2 + 3 + 5 + 7 = 17)
# sum_of_primes(11) -> 28 (2 + 3 + 5 + 7 + 11 = 28)

def is_prime(n):
    from itertools import count, islice
    return n > 1 and all(n % i for i in islice(count(2), int(n**0.5)-1))

#Add your function here!
def sum_of_primes(n):
    return sum(i for i in range(2, n + 1) if is_prime(i))

#If your function works correctly, this will originally
#print 10, 17, 17, and 28.
print(sum_of_primes(6))
print(sum_of_primes(7))
print(sum_of_primes(8))
print(sum_of_primes(11))

############################################
# seasonPicker.py 3.4.10

#Write a function called what_season. what_season should
#have two parameters: the first a string representing
#a month, and the second an integer representing a day.
#
#what_season should return "Spring" if the date is in
#Spring, "Summer" if it's in Summer, "Fall" if it's in
#Fall, and "Winter" if it's in Winter.
# - Spring starts March 20.
# - Summer starts June 21.
# - Fall starts September 22.
# - Winter starts December 21.
def what_season(month, day):
    # Manually convert the month to its numerical representation
    if month == "January":
        month_num = 1
    elif month == "February":
        month_num = 2
    elif month == "March":
        month_num = 3
    elif month == "April":
        month_num = 4
    elif month == "May":
        month_num = 5
    elif month == "June":
        month_num = 6
    elif month == "July":
        month_num = 7
    elif month == "August":
        month_num = 8
    elif month == "September":
        month_num = 9
    elif month == "October":
        month_num = 10
    elif month == "November":
        month_num = 11
    elif month == "December":
        month_num = 12

    # Determine the season based on month and day
    if (month_num == 3 and day >= 20) or (month_num == 4) or (month_num == 5) or (month_num == 6 and day <= 20):
        return "Spring"
    elif (month_num == 6 and day >= 21) or (month_num == 7) or (month_num == 8) or (month_num == 9 and day <= 21):
        return "Summer"
    elif (month_num == 9 and day >= 22) or (month_num == 10) or (month_num == 11) or (month_num == 12 and day <= 20):
        return "Fall"
    else:
        return "Winter"

print(what_season("December", 25))  # Winter
print(what_season("June", 15))  # Spring
print(what_season("June", 23))  # Summer
print(what_season("September", 27))  # Fall

########################################################
# philJackson.py 3.4.11
#Write a function called is_a_contender that will take three
#parameters: a team name (a string), a number of wins (an
#integer), and a number of losses (an integer).
#
#Based on these parameters, the function should return one
#of three strings:
# - If the team is a contender (at least 40 wins and fewer
#   than 20 losses), return "The [team name] are a contender!"
# - If the team is not a contender (less than 40 wins and at least
#   20 losses), return "The [team name] are not a contender!"
# - If it cannot be determined (both values are higher or both
#   values are lower), return "The [team name] might be a contender!"
def is_a_contender(team_name, wins, losses):
    if wins >= 40 and losses < 20:
        return f"The {team_name} are a contender!"
    elif wins < 40 and losses >= 20:
        return f"The {team_name} are not a contender!"
    else:
        return f"The {team_name} might be a contender!"

# If your function works correctly, this will originally
# print: "The Hawks are not a contender!".
test_team_name = "Hawks"
test_wins = 18
test_losses = 40

print(is_a_contender(test_team_name, test_wins, test_losses))

#############################################################
# BloodPressure.py 3.4.12
#Write a function called check_blood_pressure that takes two
#parameters: a systolic blood pressure and a diastolic blood
#pressure, in that order. Your function should return "Low",
#"Ideal", "Pre-high", or "High" -- whichever corresponds to
#the given systolic and diastolic blood pressure.
#
#You should assume that if a combined blood pressure is on the
#line between two categories (e.g. 80 and 60, or 120 and 70),
#the result should be the higher category (e.g. Ideal and
#Pre-high for those two combinations).
def check_blood_pressure(systolic, diastolic):
    if systolic >= 140 or diastolic >= 90:
        return "High"
    elif systolic >= 120 or diastolic >= 80:
        return "Pre-high"
    elif systolic >= 90 or diastolic >= 60:
        return "Ideal"
    else:
        return "Low"

#If your function works correctly, this will originally
#print: Ideal
test_systolic = 110
test_diastolic = 70
print(check_blood_pressure(test_systolic, test_diastolic))

##################################################################
# PokemonDamage.py 3.4.13
#Recall Coding Problem 2.4.8. In that problem, you calculated
#the damage done by an attack based on several parameters.
#
#Convert your code from there into two functions, one called
#calculate_damage and one called calculate_modifier.
#
#Your function for calculate_damage must call calculate_modifier;
#it may not calculate the modifier separately. As such,
#calculate_damage should accept all ten parameters: STAB,
#Type, Critical, Other, Random, Level, Attack, Defense, and
#Base. You'll need to pass STAB, Type, Critical, Other, and
#Random to calculate_modifier.

def calculate_modifier(STAB, Type, Critical, Other, Random):
    return STAB * Type * Critical * Other * Random


def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):
    modifier = calculate_modifier(STAB, Type, Critical, Other, Random)
    damage = ((2 * Level / 5 + 2) * Attack * Base / Defense / 50 + 2) * modifier
    return damage


#print: 16.0
STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

print(calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base))

###################################################################
# AverageWordLength.py 3.4.14
# -----------------------------------------------------------
# In this problem, you should write three functions:
# word_count, letter_count, and average_word_length.
#
# word_count should take as input a string. It should return
# the number of words in the string. You may assume that the
# number of words in the string will be one more than the
# number of spaces in the string.
#
# letter_count should take as input a string. It should return
# the number of letters in the string. You may assume that
# the string is only letters and spaces: no punctuation or
# numbers.
#
# average_word_length should take as input a string. It should
# return the average length of the words in the string. You
# can find the average length by dividing the number of letters
# by the number of words.
#
# Your implementation for average_word_length *must* call
# word_count and letter_count.
def word_count(a_string):
    return len(a_string.split())

def letter_count(a_string):
    return sum(1 for char in a_string if char.isalpha())

def average_word_length(a_string):
    words = word_count(a_string)
    letters = letter_count(a_string)
    return letters / words

# If your function works correctly, this will originally
# print: 3.5
a_string = "Up with the white and gold"
print(average_word_length(a_string))

####################################################
# SOLUTION TWO FOR ABOVE
# First, we create the function:
def letter_count(a_string):
    letters = 0
    for character in a_string:
        # If it's not a space, then it must be a letter!
        if not character == " ":
            letters += 1
    # Finally, we return how many letters we found.
    return letters

# word_count is the exact opposite. Instead of counting the
# characters that are not spaces, we only want to count the
# spaces:

def word_count(a_string):
    # Here, we'll initialize our initial count to 1 because
    # each space starts a new word -- that means we have one
    # word to begin with.
    words = 1
    for character in a_string:
        if character == " ":
            words += 1

    return words

# We divide the results of letter_count by the results of
# word_count.

def average_word_length(a_string):
    return letter_count(a_string) / word_count(a_string)

a_string = "Up with the white and gold"
print(average_word_length(a_string))

#####################################################
# validCharacters.py 3.4.15
#Write a function called is_valid. is_valid should take two
#parameters: a string to check, and a string of all valid
#characters.
#is_valid should return the boolean True if all the
#characters in the string to check are present in the string
#of valid characters. It should return False if any character
#in the checked string does not appear.
def is_valid(check_string, valid_characters):
    for char in check_string:
        if char not in valid_characters:
            return False
    return True

#print True, then False
sample_valid_string = "1234-5678-9011-1111"
sample_invalid_string = "1234!5678.9011?1111"
valid_characters = "0123456789-"

print(is_valid(sample_valid_string, valid_characters))
print(is_valid(sample_invalid_string, valid_characters))

#############################################################
# VowelsAndConsonants.py 3.4.16
#Call this function count_letters. It should have two
#parameters: the string in which to search, and a boolean
#called find_consonants. If find_consonants is True, then the
#function should count consonants. If it's False, then it
#should instead count vowels.
#
#Return the number of vowels or consonants in the string
#depending on the value of find_consonants. Do not count
#any characters that are neither vowels nor consonants (e.g.
#punctuation, spaces, numbers).
#
#You may assume the string will be all lower-case letters
#(no capital letters).

def count_letters(input_string, find_consonants):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in input_string:
        if find_consonants and char in consonants:
            count += 1
        elif not find_consonants and char in vowels:
            count += 1
    return count
# test the function with the given example:
a_string = "up with the white and gold"
print(count_letters(a_string, True))  # Should print 14 (counting consonants)
print(count_letters(a_string, False))  # Should print 7 (counting vowels)




# Write a function called has_a_vowel. has_a_vowel should have
# one parameter, a string. It should return True if the string
# has any vowels in it, False if it does not.
#the function below ONLY looks at first letter in strings
#and returns incorrect RETURN. Program needs to return all vowels

def has_a_vowel(a_str):
    for letter in a_str:
        if letter in "aeiou":
            return True
    return False

print(has_a_vowel("abba"))
print(has_a_vowel("beeswax"))
print(has_a_vowel("syzygy"))
print(has_a_vowel(""))
#####################################

def file_text(filename):
    try:
        file = open(filename)
    except:
        return "Error opening file!"
    file_text = file.read()
    return file_text

file_text("test.txt")
file_contents = file_text("test.txt")
print(file_contents)

###############################################
# Write a function called get_integer that takes as input one
# variable, my_var. If my_var can be converted to an integer,
# do so and return that integer. If my_var cannot be converted
# to an integer, return a message that says, "Cannot convert!"
#
# For example, for "5" as the value of my_var, get_integer would
# return the integer 5. If the value of my_var is the string
# "Boggle.", then get_integer would return a string with the
# value "Cannot convert!"
#
# Do not use any conditionals or the type() function.
def get_integer(my_var):
    try:
        return int(my_var)
    except (ValueError, TypeError):
        return "Cannot convert!"

# If your function works correctly, this will originally
# print: 5, Cannot convert!, and 5.

print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))

#############################################
#Instead of printing "Cannot convert!" when my_var
#cannot be converted to an integer, you should instead return
#the error message that results.
#Write a function called get_integer that takes as input one
#variable, my_var. If my_var can be converted to an integer,
#do so and return that integer. If my_var cannot be converted
#to an integer, return the error message that results from
#attempting to do so.
#Do not use any conditionals or the type() function.
def get_integer(my_var):
    try:
        return int(my_var)
    except Exception as error:
        return error

print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))



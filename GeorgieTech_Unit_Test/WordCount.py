#Write a function called word_count. word_count takes as
#input a string called my_string, and returns as output the
#number of words in the string.

#For the purposes of this problem, you can assume that every space indicates a new
#word; so, the number of words should be one more than the number of spaces.

#You may also assume that any strings are
#not empty, so there should always be at least one word if
#my_string is a string.

# Note, though, that it could be the case that a non-string
# is accidentally passed in as the argument for my_string. If
# that happens, an error will arise.
# If such an error arises, you should instead return "Not a string". Otherwise,
# return an integer representing the number of words in the string.
def word_count(my_string):
    try:
        # Attempt to perform string operations, which will fail if my_string is not a string
        word_list = my_string.split(' ')
        return len(word_list)
    except AttributeError:
        # If my_string is not a string, it will cause an AttributeError
        return "Not a string"

#If your function works correctly, this will originally
#print:
#Word Count: 4
#Word Count: 1
#Word Count: 7
#Word Count: Not a string
#Word Count: Not a string
#Word Count: Not a string
print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("One."))
print("Word Count:", word_count("There are seven words in this sentence."))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))
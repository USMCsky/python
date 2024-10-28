#Revise your word_count method so that if it encounters
#multiple consecutive spaces, it does *not* count an
#additional word. For example, these three strings should
#all be counted as having two words:
# "Hi   David"
# "Hi                 David"
#Other than ignoring consecutive spaces, the directions are
#the same: write a function called word_count that returns an
#integer representing the number of words in the string, or
#return "Not a string" if the input isn't a string. You may
#assume that if the input is a string, it starts with a
#letter word instead of a space.
def word_count(s):
    if type(s) != str:
        return "Not a string"

    # Split the string by spaces and filter out empty strings resulting from multiple spaces
    words = [word for word in s.split(" ") if word]
    return len(words)

print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("Hi   David"))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))

# SOLUTION #2
# Our function definition hasn't changed:

def word_count(my_string):
    # And we still want to anticipate errors, so we wrap our
    # body in a try block:

    try:
        word_count = 1
        previous_was_space = False
        # Then, we run the same loop we ran before:
        for letter in my_string:

            # But instead of counting if the current letter
            # is a space, we count if it's a space *and* the
            # previous letter wasn't a space. Effectively,
            # this means we're only counting the first space
            # when several appear in a row:
            if letter == " " and not previous_was_space:
                word_count += 1
            # Then, we have to update previous_was_space so
            # that it has the right value on the next
            # iteration of the loop:
            if letter == " ":
                previous_was_space = True
            else:
                previous_was_space = False
        # Then we can return the word count:
        return word_count
    # And as before, we return "Not a string" if we found a
    # TypeError:
    except TypeError:
        return "Not a string"

print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("Hi   David"))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))
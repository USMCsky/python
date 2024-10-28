# Write a function called average_word_length that takes as
# input a string called my_string, and returns as output the
# average length of the words in the string.

# - You should not count punctuation marks toward the
#   length of a word. A string like "Hi, Lucy" has two
#   words with an average length of 3.0 characters: the ,
#   after "Hi" does not count as a character in the word.
#   The only punctuation marks you need to handle are
#   these: . , ! ?

# - You may assume the only characters in the string are
#   letters, the punctuation marks listed above, and spaces.
# - If my_string is not a string, you should instead return
#   the string, "Not a string".

# - If there are no words in my_string, you should instead
#   return the string, "No words". This could happen for
#   strings like "" (an empty string) and ".,!?" (a string
#   of only punctuation marks). You may assume that any
#   of these punctuation marks will always be followed by
#   at least one space.
#
#Here are a few hints that might help you:
#
# - You can peak at the first character in my_string with
#   my_string[0]. If my_string is "Hi, Lucy", then the value
#   of my_string[0] is "H". You don't have to do this, but
#   you can if you want.

# - There are lots of ways you can do this. If you're
#   stuck, try taking a step back and thinking about the
#   problem from a fresh perspective.

# - If you're still stuck, try counting words and letters
#   separately, and worrying about average length only
#   after both have been counted.
# The average word length should be character count divided by word count.
def average_word_length(my_string):
    # Check if the input is a string
    if not isinstance(my_string, str):
        return "Not a string"

    words = my_string.split()
    if len(words) == 0:       # Case when the string is empty or contains only punctuation marks
        return "No words"

    # Removing the special punctuation marks
    cleaned_words = [''.join(char for char in word if char.isalpha()) for word in words]

    # Filtering out any empty words resulted from cleaning punctuation marks
    cleaned_words = [word for word in cleaned_words if word]
    if len(cleaned_words) == 0:
        return "No words"

    total_length = sum(len(word) for word in cleaned_words) # Calculate the total length of all words
    average_length = total_length / len(cleaned_words)  # Calculate the average length
    return average_length

#4.0
#Not a string
#No words
print(average_word_length("Hi"))
print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))

#######################################
# ALTERNATIVE SOLUTION
# As before, there are lots of ways to do this. We'll cover
# one that can be done using only what we've covered so far,
# but there are other ways to do this.
#
# First, we start with the function header:

def average_word_length(my_string):
    # And as before, we wrap everything in a try block so
    # that we can react to errors that arise:
    try:

        # Average word length is the number of characters
        # divided by the number of words. So, we know we're
        # going to need to count both of those things:

        word_count = 0
        letter_count = 0

        # And we're going to need to reuse the method we used
        # before to avoid consecutive spaces. Notice, though,
        # that this problem says not to assume the string
        # starts with a letter. How can we take care of that?
        # Here, we're going to redefine how we identify words:
        # a new word starts when a letter occurs after a
        # space. So, let's pretend like a space occurred right
        # before the string started:

        previous_was_space = True

        # This way, if the first character in the string is a
        # letter, it's counted as a new word because it
        # "follows" the space. If it's not, it won't count
        # anyway.
        #
        # Now we iterate through each character in the string:

        for letter in my_string:

            # For each one, we want to check if it's actually
            # a character we should count. We should count it
            # as a letter if it's a letter. Remember, we only
            # have to worry about not counting spaces and four
            # punctuation marks: .,?!

            if not letter == " " and not letter == "." and not letter == "," and not letter == "!" and not letter == "?":

                # If this current character isn't any of those
                # characters, we count it as a letter:
                letter_count += 1

                # And if it's a letter that occurred after a
                # space, we also note that we found a new
                # word!
                if previous_was_space:
                    word_count += 1

            # Then last, we update previous_was_space based on
            # whether or not this character was a space.
            previous_was_space = letter == " "

        # Then, we return the number of letters divided by the
        # number of words.
        return letter_count / word_count

    # There are two problems that could arise. One, word_count
    # could have been 0. That means there were no words in the
    # string. So, we catch the ZeroDivisionError and return the
    # string "No words".

    except ZeroDivisionError:
        return "No words"

    # Or, my_string might not have been a string in the first
    # place. So, we catch a TypeError and return the string
    # "Not a string".

    except TypeError:
        return "Not a string"

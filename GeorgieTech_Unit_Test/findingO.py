words = ["dog", "sparrow", "cat", "frog"]

# This program is supposed to print the location of the 'o'
# in each word in the list. However, line 22 causes an
# error if 'o' is not in the word. Add try/except blocks
# to print "Not found" when the word does not have an 'o'.
# However, when the current word does not have an 'o', the
# program should continue to behave as it does now.
#
# Hint: don't worry that you don't know how line 18 works.
# All you need to know is that it may cause an error.
#
# You may not use any conditionals.
for word in words:
    try:
        print(word.index("o"))
    except ValueError:
        print("Not found")


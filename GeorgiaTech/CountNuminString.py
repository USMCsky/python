a_string = "F12dav^f%$25d"

#a_string is a string of random characters. Write some code
#that adds all the digits that appear in the string and prints
#their sum.
#
#For example, the digits in the string above are 1, 2, 2, and 5,
#so your code would print 10.
#
#Remember, you can iterate over each character in a string with
#this syntax:
#
#for a_character in a_string:
#
#Remember also, you can check if a character is in a list of other
#characters within this syntax:
#
#if a_character in "ABCDEFG":
#If there are no digits in the string, print 0.
# Initialize sum to 0
sum = 0
for item in a_string:
    if item in "0123456789":
        sum += int(item)
print(sum)

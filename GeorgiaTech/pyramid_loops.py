# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# Which of the following code segments would have the output shown above?

for i in range(0, 5):
    for j in range(0, i):
        print(j, end=" ")
    print(" ")

for i in range(5, 0):
    for j in range(5, i):
        print(j, end=" ")
    print(" ")

for i in range(5, 0, -1):
    for j in range(5, i, -1):
        print(j, end=" ")
    print(" ")

print("")

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print(" ")

for i in range(0, 5):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print(" ")
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# Which of the following code segments would have the output shown above?

i = 0
while i < 5:
    j = i
    while j > 0:
        print(j, end=" ")
        j -= 1
    i += 1
    print("")

print(" ")

i = 5
while i > 0:
    j = i
    while j > 0:
        print(j, end=" ")
        j -= 1
    i -= 1
    print("")

i = 0
while i < 5:
    j = 0
    while j < i:
        print(j, end=" ")
        j += 1
    i += 1
    print("")


mystery_string = "Lucy"


#For example, if the string was "Lucy", then the output would
#be:
#
#L
#Lu
#Luc
#Lucy
#
#Hint: to print without automatically starting a new line,
#include the text end="" inside the print statement's
#parentheses. For example, print("Hello", end="") will print
#the word "Hello" without starting a new line afterward. So,
#calling it twice would print "HelloHello" on one line
#instead of two lines.
mystery_string = "Lucy"
for i in range(len(mystery_string)):
    print(mystery_string[:i + 1])

########### alternative solution #####
mystery_string = "Lucy"
current_row = ""
for letter in mystery_string:
    current_row += letter
    print(current_row)

#####################################
mystery_string = "Lucy"

#This method uses information you'll learn in Chapter 4.2.
#Here's a preview in the meantime, though:

for i in range(1, len(mystery_string) + 1):
    print(mystery_string[0:i])


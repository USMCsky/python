mystery_value = 82
#Write a while loop that continues to add 9 to mystery_value
#until mystery_value is greater than 100. Each time 9 is
#added, print the *new* value of mystery_value. For example,
#with mystery_value = 87, your code should print 96 and 105.
#Add your code here!
while mystery_value <= 100:
    mystery_value += 9
    print(mystery_value)
##########################

mystery_int_1 = 3
mystery_int_2 = 4
mystery_int_3 = 5

#Above are three values. Run a while loop until all three
#values are less than or equal to 0. Every time you change
#the value of the three variables, print out their new values
#all on the same line, separated by single spaces.

while mystery_int_1 > 0 or mystery_int_2 > 0 or mystery_int_3 > 0:
    mystery_int_1 -= 1
    mystery_int_2 -= 1
    mystery_int_3 -= 1
    print(mystery_int_1, mystery_int_2, mystery_int_3)

############################
#debug factorial of 5
num = 5
result = 1
for i in range(1, num + 1):
    result *= i
    print(result)
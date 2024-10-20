mystery_int = 50

#Do not use sum function - add with loops
#Add some code below that will find and print the sum of
#every odd number between 0 and mystery_int. This time,
#exclude the bounds (e.g. if mystery_int was 51, add the odds
#from 1 to 49, but not 51).
sum = 0

# Iterate through the range and add the odd numbers
for num in range(1, mystery_int):
    if num % 2 != 0:
        sum += num

print(sum)
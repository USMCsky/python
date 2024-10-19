#Creates listOfStrings and assigns it a list of strings each with
#multiple words
listOfStrings = ["This is the first string", "This is the second string",
                 "This is the third string", "This is the fourth string",
                 "This is the fifth string"]
numSpaces = 0
#Loops over each string in listOfStrings
for currentString in listOfStrings:
    #Loops over each character in currentString
    for currentCharacter in currentString:
        #Checks if the current character is a space
        if currentCharacter == " ":
            numSpaces += 1

numWords = numSpaces + len(listOfStrings)
print("There are", numWords, "words in these strings.")

############################################################
## multiplication table to 100
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "times", j, "equals", i * j)

####################################################
## loop values - values of count
count = 0
for x in range(3):
    for y in range(3):
        count = count + y
print(count)

count = 0
for x in range(3):
    for y in range(3):
        count = count + x
print(count)

count = 0
for x in range(3):
    for x in range(3):
        count = count + x
print(count)

#############compare two list###############
list1 = ["Alison", "Mina", "Leticia", "Elaine", "Sonny", "Benito"]
list2 = ["Yuri", "Andrew", "Mina", "Elaine", "Charles", "Alison"]
for name1 in list1:
    for name2 in list2:
        if name1 == name2:
            print(name1)

num = 5
result = 1
for i in range(1, num + 1):
    result *= i
print(result)

###########################
## All the following loops have the same result
for i in range(1, 6):
    j = 0
    while j < i:
        print(j, end=" ")
        j += 1
    print("")

for i in range(1, 6):
    for j in range(0, i):
        print(j, end=" ")
    print("")

i = 0
while i < 6:
    j = 0
    while j < i:
        print(j, end=" ")
        j += 1
    i += 1
    print("")

#### EARWORM SOLUTION THAT PASSED ####
lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 3

count = 0
index = 0

while count < lines_of_sanity:
    print(lyrics[index])
    count += 1
    index = (index + 1) % len(lyrics)

while index != 0:
    print(lyrics[index])
    index = (index + 1) % len(lyrics)

print("MAKE IT STOP")


##### SUGGESTED SOLUTION - THE GIVEN SAMPLE SOLUTION BELOW WOULD FAIL  #####

lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 3

# As the hint suggested, we're going to need a counter to count how
# many lines have been played already. This is how we'll know if we've
# lost sanity yet. We'll start this at 0:

lines_heard = 0

# Now, we need two loops: a while loop while lines_heard is less than
# lines_of_sanity, and a for loop to iterate through each line of the
# song. Which one goes first?
#
# Well, we want to repeat the song while lines_heard is less than
# lines_of_sanity. Since the while loop is governing the for loop, we
# put the while loop on the outside:

while lines_heard < lines_of_sanity:

    # Then we run a for loop for each line of the lyrics:
    for line in lyrics:
        # For each line, we want to increment out counter so we can
        # keep track of our sanity:
        lines_heard += 1

        # Then we want to print the current line:
        print(line)

# Then, after we're done printing the lyrics, we print MAKE IT STOP.
# Note that this is outside any of the loops because it only prints
# once, and only after the other lines are done.
print("MAKE IT STOP")




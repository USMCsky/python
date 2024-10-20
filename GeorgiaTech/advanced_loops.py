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

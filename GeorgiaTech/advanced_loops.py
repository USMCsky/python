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




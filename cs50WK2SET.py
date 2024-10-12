# In a file called camel.py, implement a program that prompts the user for the name of a
# variable in camel case and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.
#
# Much like a list, a str is “iterable,” which means you can iterate over each of its
# characters in a loop. For instance, if s is a str, you could print each of its characters,
# one at a time, with code like:
# for c in s:
#     print(c, end="")

cC = input("camelCase: ").strip()

for letter in cC:
    if letter.islower():
        print(letter, end="")
    else:
        print("_" + letter.lower(), end="")

# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins
# in these denominations: 25 cents, 10 cents, and 5 cents.
#
# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time,
# each time informing the user of the amount due. Once the user has inputted at least 50 cents,
# output how many cents in change the user is owed. Assume that the user will only input integers,
# and ignore any integer that isn’t an accepted denomination.

coins = [5, 10, 25,]
owe = 50

print("Amount Due: 50")
while True:
    inserted_coin = int(input("Insert coin in nickels, dimes, and quarters: "))
    if inserted_coin in coins:
        owe -= inserted_coin
        if owe < 0:
            print(f"Change Owed: {owe * -1}")
            break
        elif owe == 0:
            print("Here is your coke")
            break
        else:
            print(f"Amount Due: {owe}")
    else:
        print("Must use a correct coin!")

# When texting or tweeting, it’s not uncommon to shorten words to save time or space,
# as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py,
# implement a program that prompts the user for a str of text and then outputs that same text but with
# all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

twttr_post = input("Input: ")
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
print("Posts: ",end="")
for vowel in twttr_post:
    if vowel in vowels:
        continue
    print(vowel, end="")


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


# Structure is_valid returns True if s meets all requirements and False if it does not.
#implement additional functions for is_valid to call (e.g., one function per requirement).
# Much like a list, a str is a “sequence” (of characters), which means it can be “sliced” into shorter
# strings with syntax like s[i:j]. For instance, if s is "CS50", then s[0:2] would be "CS".
# plates.py
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) <= 2 or len(s) > 6:  # Must be longer than two or no greater than 6
        return False

    for punct in s:             # “No periods, spaces, or punctuation marks are allowed.”
        if punct in [".", " ", "!", "?", ","]:
            return False

# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
    for i in range(len(s)):
        if s[i].isdigit():
            if i == len(s) - 2 and s[i] == '0':
                return False
            elif not(i == len(s) - 1 or i == len(s) - 2):
                return False
    return True

main()
#
# In a file called nutrition.py, implement a program that prompts consumers users
# to input a fruit (case-insensitively) and then outputs the number of calories in one portion
# of that fruit, per the FDA’s poster for fruits, which is also available as text.
# Capitalization aside, assume that users will input fruits exactly as written in the
# poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
#
# Rather than use a conditional with 20 Boolean expressions,
# one for each fruit, better to use a dict to associate a fruit with its calories!
# If k is a str and d is a dict, you can check whether k is a key in d with code like:
# if k in d:
# Take care to output the fruit’s calories, not calories from fat!
# nutrition.py

fruits = {
    "Apple": 130, "Avocado": 50, "Banana": 110, "Cantaloupe": 50, "Grapefruit": 60, "Grapes": 90, "Honeydew Melon": 50, "Kiwifruit": 90,
    "Lemon": 15, "Lime": 20, "Nectarine": 60, "Orange": 80, "Peach": 60, "Pear": 100, "Pineapple": 50, "Plums": 70, "Strawberries": 50,
    "Sweet Cherries": 100, "Tangerine": 50, "Watermelon": 80, }
choice = input("Choice: ").strip().title()

for fruit in fruits:
    if choice in fruit:
        print("Calories:" + str(fruits[fruit]))

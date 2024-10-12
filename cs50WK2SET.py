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


mystery_string = "CS1301"

#Write a for-each loop that lists each character in
#mystery_string with its index. For example, if the string
#Add your code here!
index = 0
for character in mystery_string:
    print(f"{index} {character}")
    index += 1

# also enumerate
for index, character in enumerate(mystery_string):
    print(f"{index} {character}")

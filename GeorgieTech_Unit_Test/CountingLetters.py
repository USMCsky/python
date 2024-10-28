mystery_string = "Hello! What a fine day it is today."
mystery_character = "a"

#Write some code below that will count and print how many
#times mystery_character appears in mystery_string. You may
#not use the string class's .count method.
#With the original values for mystery_string and
#mystery_character, your code should initially print 4. Only
#count characters with the same case as mystery_character
#(in other words, here you would ignore capital A).

count = 0
for char in mystery_string:
    if char == mystery_character:
        count += 1

print(count)

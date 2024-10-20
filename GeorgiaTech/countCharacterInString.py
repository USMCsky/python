mystery_string = "Hello! What a fine day it is today."
mystery_character = "a"

# Initialize a counter
count = 0

# Iterate through each character in the string
for character in mystery_string:
    # Check if the current character matches the mystery_character
    if character == mystery_character:
        count += 1

# Print the result
print(count)



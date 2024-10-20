mystery_list = ["Taylor Swift", "Twenty Two", "Georgia Tech"]

# Initialize a counter to 0
count = 0

# Loop through each string in the list
for string in mystery_list:
    # Loop through each character in the current string
    for char in string:
        # Check if the character is 't' or 'T'
        if char == 't' or char == 'T':
            # Increment the counter
            count += 1

# Print the final tally
print(count)


# When you run this code, it will print each letter from A to Z on a new line.
# Here's a breakdown of what's happening:
# ord(start_character) converts the start character ("A") to its ASCII value (65).
# ord(end_character) converts the end character ("Z") to its ASCII value (90).
# The range(start_ord, end_ord + 1) generates a sequence of numbers from 65 to 90 inclusive.
# The for loop iterates over this sequence, converting each ASCII value back to its corresponding
# character using chr(i) and then printing it.
#
start_character = "f"
end_character = "l"

start_ord = ord(start_character)
end_ord = ord(end_character)

for i in range(start_ord, end_ord + 1):
    print(chr(i))




#### EARWORM SOLUTION ####
lyrics = ["I can't do this all on my own, no I know", "I'm no superman"]
lines_of_sanity = 10

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


##### SUGGESTED SOLUTION #####

lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 6

# As the hint suggested, we're going to need a counter to count how
# many lines have been played already. This is how we'll know if we've
# lost sanity yet. We'll start this at 0:

lines_heard = 0

# Now, we need two loops: a while loop while lines_heard is less than
# lines_of_sanity, and a for loop to iterate through each line of the
# song. Which one goes first?
#
# Well, we want to repeat the song while lines_heard is less than
# lines_of_sanity. Since the while loop is governing the for loop, we
# put the while loop on the outside:

while lines_heard < lines_of_sanity:

    # Then we run a for loop for each line of the lyrics:
    for line in lyrics:
        # For each line, we want to increment out counter so we can
        # keep track of our sanity:
        lines_heard += 1

        # Then we want to print the current line:
        print(line)

# Then, after we're done printing the lyrics, we print MAKE IT STOP.
# Note that this is outside any of the loops because it only prints
# once, and only after the other lines are done.
print("MAKE IT STOP")



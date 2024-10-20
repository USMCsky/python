#### EARWORM SOLUTION THAT PASSED - FINISH VERSES ####
lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 3

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


### EARWORM STOP ON PARTICULAR COUNT#######
# Given values
lyrics = ["I wanna be your endgame", "I wanna be your first string",
          "I wanna be your A-Team", "I wanna be your endgame, endgame"]
lines_of_sanity = 9

count = 0
# Print the lyrics up to 6 times or the limit of lines_of_sanity
for index in range(lines_of_sanity):
    if count >= 6:
        break
    print(lyrics[index % len(lyrics)])
    count += 1

################################
### Print lyrics length of sanity

for i in range(0, lines_of_sanity):
    # Next, we want to print a line from lyrics. Which line? Well, for
    # the first four lines, we want to print the line at the index of
    # i.
    #
    # After that, though, i might exceed the length of the list. What
    # do we do then? Well, instead of just printing the item at
    # index i, we want to print the item at index i % length. That way,
    # if i is greater than the length, it 'wraps around' to the start
    # again.
    #
    # So, that would look like this:

    print(lyrics[i % len(lyrics)])

    # The brackets after parentheses let us specify which item in lyrics
    # we're printing. i % len(lyrics) finds which lyric to print right
    # now. If i is 4 and there are 4 lyrics, then it will print the first
    # one again. if i is 6 and there are 4 lyrics, it will print the
    # third one again.

print("MAKE IT STOP")

############### ANOTHER SOLUTION
# We're still going to need to count the number of lines heard so far:
lines_heard = 0

# And we're still going to want to repeat until lines_heard exceeds
# lines_of_sanity:
while lines_heard < lines_of_sanity:

    # And we still want to iterate over each line in the lyrics:
    for line in lyrics:

        # The difference here is: we only want to print if lines_head
        # still doesn't exceed lines_of_sanity. It's possible that it
        # exceeded it since the last time the while loop condition was
        # checked since it could be incremented several times inside
        # this for loop.
        #
        # So, we only want to print if it's still less:

        if lines_heard < lines_of_sanity:
            lines_heard += 1
            print(line)

        # Technically, we could break here: it would stop the for loop,
        # send us back to check the while loop, and that would
        # terminate. We don't really need to, though. Without that, the
        # for loop will run a few more times, but they still won't print
        # anything.

print("MAKE IT STOP")

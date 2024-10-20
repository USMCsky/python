flips = "HHTTHTHHTTHHTHTHTHHTTHHTTTTH"

#The string above gives the results of a series of coin flips,
#H for heads and T for tails.
#
#Count the number of heads and number of tails. Then, print
#a message like this one based on the results:
#
#13 heads, 10 tails. Heads wins.
#
#Replace 13 and 10 with the actual numbers of heads and tails.
#Replace 'Heads wins.' with 'Tails wins.' ift there are more
#tails, or with 'It's a tie.' if there are the same number of
#heads and tails.
#
#For example:
#
# "HHTTHH" -> 4 heads, 2 tails. Heads wins.
# "THTHTT" -> 2 heads, 4 tails. Tails wins.
# "TTHHHT" -> 3 heads, 3 tails. It's a tie.


#Add your code here!
sumH = 0
sumT = 0

for letter in flips:
    if letter == "H":
        sumH += 1
    if letter == "T":
        sumT += 1

if sumH > sumT:
    print(str(sumH) +" heads, " + str(sumT) + " tails. Heads wins.")
elif sumT > sumH:
        print(str(sumH) +" heads, " + str(sumT) + " tails. Tails wins.")
else:
    print(str(sumH) +" heads, " + str(sumT) + " tails. It's a tie.")

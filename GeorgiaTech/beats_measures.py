beats_per_measure = 4
measures = 5

#In music, a song's time signature is given in terms of beats
#per measure. A common time signature is 4 beats per measure:
#for every measure of music, a conductor might count from 1
#to 4 with the tempo of the music.

#Write a nested for loop that will print out the beats of the
#piece of music. For example, if the song had 4 beats per
#measure and only 2 measures, this would print out:

#We print from 1 to 4 before starting over because there are
#4 beats per measure, and we print them all twice because there
#are two measures.
# Nested loop to print beats of music
for _ in range(measures):
    for beat in range(1, beats_per_measure + 1):
        print(beat)

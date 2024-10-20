beats_per_measure = 4
measures = 5

#BY LINE
for measure in range(1, measures + 1):
    for beat in range(1, beats_per_measure + 1):
        if beat == 1:
            print(measure, end=' ')
        else:
            print(beat, end=' ')
    print()

# Loop through each measure vertically
for measure in range(1, measures + 1):
    # Loop through each beat in the current measure
    for beat in range(1, beats_per_measure + 1):
        # If it's the first beat, print the measure number
        if beat == 1:
            print(measure)
        else:
            print(beat)

########## BEST SOLUTION ##############
for i in range(1,measures+1):
    print(i)
    for j in range(2 ,beats_per_measure +1):
        print(j)

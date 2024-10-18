# Variables
phase = "Full"
distance = 248000
date = 29
eclipse = False

if phase == "Full":
    special_moons = []
    if distance < 230000:
        special_moons.append("Super")
    if date in [29, 30, 31]:
        special_moons.append("Blue")
    if eclipse:
        special_moons.append("Blood")

    if special_moons:
        print(" ".join(special_moons) + " Moon")
    else:
        print("Full Moon")
else:
    print("Moon")
##############################
# alternate sample solutions
phase = "Full"
distance = 228000
date = 31
eclipse = True

# There are a few ways we could do this. Here's mine. First,
# I'm going to start by creating a result string with the
# value "Moon". I know that no matter what, the last word of
# my output should be "Moon":
result = "Moon"

# Next, I only care about any of these values if the phase is
# "Full". So, I'll go ahead and check that:
if phase == "Full":

    # Next, I want to check whether to add "Super", "Blue",
    # and "Blood". If I want to add "Blood", though, I want it
    # to be closest to the word "Moon", so I'm going to check
    # that first:
    if eclipse:
        result = "Blood " + result

    # Next, I''ll check if the moon is "Blue":
    if date >= 29:
        # Note that by doing this second, I'm adding "Blue"
        # to whatever happened after checking if this was a
        # Blood Moon. If line 22 ran, result is now "Blood
        # Moon", and I'm adding "Blue" to the front to get
        # "Blue Blood Moon":
        result = "Blue " + result

    # Then, I'll check if the moon qualifies as a Super Moon:
    if distance < 230000:
        # Again, because I'm adding "Super" to the beginning,
        # it doesn't matter if "Blood" and/or "Blue" were
        # added:
        result = "Super " + result

    # The last part is a little tricky: I need to add "Full"
    # to the front if I didn't add Blue, Blood, or Super.
    # There are ways to check the value of 'result' to see if
    # those things were added, but since we haven't learned
    # those yet, we'll go with this way.
    #
    # Here, we re-check the conditions that would have
    # caused us to add "Super", "Blue", or "Blood" to our
    # result. If none are true, then we change result to
    # "Full Moon".
    if not (eclipse or date >= 29 or distance < 230000):
        result = "Full Moon"

# Finally, we present the result. If the phase wasn't "Full",
# then we skip right from line 15 to here. That's why we gave
# result the initial value of "Moon" in the first place.
print(result)


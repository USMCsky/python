### indoor voice
shout = input("TYPE SOMETHING IN ALL CAPS ")
quiet = print(shout.lower())

### playback
playback = input(" Type in something ")
slow = playback.replace(" ", "...")
print(slow)

# faces.py
def main():
    convert(input(str("Emoticons are the best :) :( PICK ONE! ")))

def convert(input):
    print(input.replace(":(", "🙁").replace(":)", "🙂"))

main()

# In a file called einstein.py, implement a program in Python that prompts the user for
# mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an
# integer. Assume that the user will input an integer.
# einstein.py

kg = input("Enter Mass(kg): ")
e = (int(kg) * (300000000 * 300000000))
print("E = " + str(e))

# dollars_to_float, which should accept a str as input (formatted as $##.##
# # wherein each # is a decimal digit), remove the leading $, and return the amount as a float. Given $50.00 as input, it should return 50.0.
# percent_to_float, which should accept a str as input (formatted as ##%
# # wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. Given 15% as input, it should return 0.15.
# tip.py

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    meal = d.lstrip('$')
    return float(meal)

def percent_to_float(p):
    svc = p.strip('%')
    svcConvert = float(svc) / 100
    return svcConvert

main()


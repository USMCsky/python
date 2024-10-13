#Monty what is the meaning of life. DeepThought responses.
# deep.py

gqol = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = str(gqol)
if answer.strip() == "42":
    print("Yes")
elif answer.lower() == "forty-two":
    print("Yes")
elif answer.lower() == "forty two":
    print("Yes")
else:
    print("No")

# In a file called bank.py, implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and
# treat the user’s greeting case-insensitively.
# bank.py

greet = input("Enter Greeting: ").strip().lower()
if "hello" in greet:
    print("$0")
elif "h" in greet[0]:
    print("$20")
else:
    print("$100")

# In a file called extensions.py, implement a program that prompts the user for the name of a file
# and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# .gif # .jpg # .jpeg # .png # .pdf # .txt # .zip
# If the file’s name ends with some other suffix or has no suffix at all,
# output application/octet-stream
# extensions.py
ext = input("Filename: ").strip().lower()

if ext.endswith("gif"):
    print("image/gif")
elif ext.endswith("jpg"):
    print("image/jpeg")
elif ext.endswith("jpeg"):
    print("image/jpeg")
elif ext.endswith("png"):
    print("image/png")
elif ext.endswith("pdf"):
    print("application/pdf")
elif ext.endswith("txt"):
    print("text/plain")
elif ext.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")

# In a file called interpreter.py,
# implement a program that prompts the user for an arithmetic expression
# and then calculates and outputs the result as a
# floating-point value formatted to one decimal place.
# Assume that the user’s input will be formatted as x y z, with one space
# between x and y and one space between y and z, wherein:
# x, y, z = expression.split(" ")
# x is an integer
# y is +, -, *, or /
# z is an integer
#  user inputs 1 + 1, your program should
#  output 2.0. Assume that, if y is /, then z will not be 0.
#       interpreter.py

x, y, z = input("Expression: ").split(" ")
xF = float(x)
zF = float(z)
if y == "+":
    result = xF + zF
    print(round(result,1))
elif y == "-":
    result = xF - zF
    print(round(result,1))
if y == "*":
    result = xF * zF
    print(round(result,1))
if y == "/":
    result = xF/zF
    print(round(result,1))

# In meal.py, implement a program that prompts the user for a time and outputs
# whether it’s breakfast time, lunch time, or dinner time.
# If it’s not time for a meal, don’t output anything at all.
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
# And assume that each meal’s time range is inclusive.
# For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
#
# Structure your program per the below, wherein convert is a function (that can be called by main)
# that converts time, a str in 24-hour format, to the corresponding number of hours as a float.
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes),
# convert should return 7.5 (i.e., 7.5 hours).
# hours, minutes = time.split(":")
# meal.py

def main():
    time = input("What time is it? ").strip()
    hours = convert(time)

    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")

def convert(time):
    hr, min = time.split(":")
    minF = float(min) / 60
    return float(hr) + minF

if __name__ == "__main__":
    main()

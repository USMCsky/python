#wallet variable with money. Half it.
wallet = 335
print(wallet/2)

#simple strings
name = "Eric"
print(name)

name = input("what is your name? ")
age = input("How old are you? ")

if age > str(40):
    print(f"{name} you are a dino at {age}")
else:
    print(f"{name}, that is an awesome {age}")

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



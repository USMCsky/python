# In deep.py, implement a program that prompts the user for the answer to
# the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42
# or (case-insensitively) forty-two or forty two. Otherwise output No.
#deep.py

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



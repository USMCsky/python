#LECTURE loops loops and more loops

i = 3
while i != 0:
    print("meow")
    i = i - 1
####
i = 0
while i < 3:
    print("meow")
    i = i + 1
###
for i in [0,1,2]:
    print("dog")
###
for i in range(5):
    print("dog")
###
print("\nCat and Dog" * 3, end="")
###
while True:
    x = int(input("\nWhat is n?"))
    if x > 0:
        break
for x in range(x):
    print("WHOOPIE")
######
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is n?"))
        if n > 0:
            break
    return n

def meow(n):
    for n in range(n):
        print(str.lower("MEOW!"))
main()

####### LISTS
students = ["Hermione", "Harry", "Ron"]
for student in students:
    print(str.upper(student))

####### LISTS
students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(students)
    print(i + 1, students[i])

##### DICT
stds = {"Hermione": "Gryffindor",
           "Harry": "Gryffindor",
           "Draco": "Slytherin",
           "Ron": "Griffindor"
           }
for s in stds:
    print(s)

for s in stds:
    print(s +"- House: " + stds[s], sep = ", ")
##############

stdDict = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]
for person in stdDict:
    print(person["name"], person["house"], sep = ", ")

##########
for _ in range(3):
    print("#")
#########
def main():
    print_column(3)
    print_row(4)

def print_column(height):
    #for _ in range(height):
        print("#\n" * height, end="")

def print_row(width):
    print("?" * width)

main()
########

def main():
    print_square(5)

def print_square(size):
    for i in range(size):
        for j in range(size):     # print("#" * size)
            print("#", end = "")  ########
        print()
main()

# FOR LOOP
# letters.py

def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in range(len(names)):     # for name in names:
        print(write_letter(names[i], "Princess Peach"))    #name

def write_letter(receiver, sender):
    return f"""
+```````````````````````````````````````````````````+
        Dear {receiver},
        
        You are cordially invite to a ball at
        Peach's Castle this evening, 7:00 PM.
        
        Sincerely,
        {sender}

+```````````````````````````````````````````````````+
"""
main()


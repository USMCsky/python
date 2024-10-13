x = int(input("What's x? "))
print(f"x is {x}")

# Catches a ValueError
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# Demonstrates else
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

# Adds a loop
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")

# Adds functions, uses break and return
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

main()

# Removes break
def main():
    x = gett_int()
    print(f"x is {x}")

def gett_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
main()

# Removes else
def main():
    x = gettt_int()
    print(f"x is {x}")

def gettt_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

main()

# Adds pass
def main():
    x = geet_int()
    print(f"x is {x}")

def geet_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

main()

# Adds prompt
def main():
    x = geeet_int("What's x? ")
    print(f"x is {x}")

def geeet_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()

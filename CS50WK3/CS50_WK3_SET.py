### fuel.py

def main():
    # 1/4 25% full, 1/2 50% full 3/4 75% full
    # 1% pr less output E. 99% or more output F.

def fuel(x,y):
    # prompt user for fraction formatted as x/y (integers)
    # output as a percentage rounded to nearest integer - amount of fuel in tank

def debug():
    # if X or Y is not int, X > Y, or Y is 0 prompt again
    # Be sure to catch ValueError and ZeroDivisionError

### TESTING LECTURES ###

    def main():
        x = get_int("What's x? ")
        print(f"x is {x}")

    def get_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                pass

    main()


    distances = {
        "Voyager 1": "163",
        "Voyager 2": "136",
        "Pioneer 10": "80 AU",
        "New Horizons": "58",
        "Pioneer 11": "44 AU",
    }

    def main():
        spacecraft = input("Enter a spacecraft: ")

        try:
            au = float(distances[spacecraft])
        except KeyError:
            print(f"'{spacecraft}' is not in dictionary")
            return
        except ValueError:
            print(f"Can't convert '{distances[spacecraft]}' to a float")
            return

        m = convert(au)
        print(f"{m} m")

    def convert(au):
        return au * 149597870700

    main()

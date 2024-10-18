### fuel.py
while True :
    try:
        fraction = input("Fraction: ")
        x,y = fraction.split("/")   #split string into num/den
        newx = int(x)
        newy = int(y)
        fuel = round(newx / newy * 100)

        if newx > newy:             #num > den start over
            continue
        elif fuel <= 1:          # 1 or less empty
            print("E")
        elif fuel >= 99:           # over 99 full
            print("F")
        else:
            print( str(fuel) + "%")      # all good print

    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
# ################################
# # taqueria.py

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
cost = 0
while True:
    try:
        if input() == 'q':
            break
        item = input("Item: ").title()
        cost = cost + menu[item]
        print(f"Total: ${cost:.2f}")
    except EOFError:
        print()
        break
    except KeyError:
        pass

#########################################
# outdated.py

def main():
    month,day, year = get_date()
    day = int(day)
    month = int(month)
    print(f"{year}-{month:02}-{day:02}")

def get_date():
    months = [  "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]

    while True:
        date = input("date: ").strip()
        if "/" in date:
            month, day, year = date.split("/")
        elif "," in date:
            month, day, year = date.split()
            if month in months:
                month = months.index(month)+1
                day = day.strip(",")
        else:
            continue
        try:
            if int(day) > 31 or int(month) > 12:
                continue
            else:
                break
        except ValueError:
            continue
    return month, day, year

main()


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

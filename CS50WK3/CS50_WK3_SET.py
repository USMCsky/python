while True :
    try:
        fraction = input("Fraction: ")
        x,y = fraction.split("/")
        newx = int(x)
        newy = int(y)

        fuel = round(newx / newy *100)

        if newx > newy:
            continue

        elif fuel >= 99:
            print("F")
        elif fuel <= 1 :
            print("E")
        else:
            print( str(fuel) + "%")

    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

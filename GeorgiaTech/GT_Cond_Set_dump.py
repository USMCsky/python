temperature = 0
celsius = True


if temperature <= 0 and celsius == True:
    print("Freezing")
elif temperature <= 32 and celsius == False:
    print("Freezing")
else:
    print("Not freezing")

team_1 = "Georgia Tech"
team_1_score = 28
team_2 = "Georgia"
team_2_score = 27

if team_1_score > team_2_score:
    winner = team_1
    margin = team_1_score - team_2_score
    print(team_1 + " beat " + team_2 + " by " + str(margin))

elif team_2_score > team_1_score:
    winner = team_2
    margin = team_2_score - team_1_score
    print(team_2 + " beat " + team_1 + " by " + str(margin))

else:
    print(team_1 + " played " + team_2 + " and it was a tie")


steak = False
pork = True
guacamole = True
queso = False

price = 5.00

if steak or pork:
    print("Adding 0.50 for steak or pork!")
    price = price + 0.50

if guacamole:
    print("Adding 1.00 for guacamole!")
    price = price + 1.00

if queso:
    print("Adding 1.00 for queso!")
    price = price + 1.00

print(price)


item = "quesadilla"
meat = "steak"
queso = False
guacamole = False
double_meat = False

if item == "quesadilla":
    base_price = 4.0
elif item == "burrito":
    base_price = 5.0
else:
    base_price = 4.5

if meat in ["steak", "pork"]:
    base_price += 0.50

if double_meat:
    if meat in ["steak", "pork"]:
        base_price += 1.50
    else:
        base_price += 1.00

if guacamole:
    base_price += 1.0

if queso and item != "nachos":
    base_price += 1.00

print(base_price)

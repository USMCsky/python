import random
import time

team1_name = "UNT"
team1_rank = 12

team2_name = "Baylor"
team2_rank = 14

team1_chance = 16 - team1_rank
team2_chance = 16 - team2_rank

team1_chance += random.randint(0,16)
team2_chance += random.randint(0,16)

print("we are gathering details...")
time.sleep(2)
print("...we are almost there...\n")
time.sleep(2)

if team1_chance >= team2_chance and team1_chance != team2_chance:
    confidence = (team1_chance - team2_chance) / 31 * 100
    confidence = int(confidence)
    print(team1_name + " WINS!🏆" + " with a " + str(confidence) + "% of confidence!!!🏆")
else:
    confidence = (team2_chance - team1_chance) / 31 * 100
    confidence = int(confidence)
    print(team2_name + " WINS!🏆" + " with a " + str(confidence) + "% of confidence!!!🏆")

if team1_chance == team2_chance:
    print("😒IT IS A TIE!!!😒")

print(f"TEAM 1: {team1_chance}")
print(f"TEAM 2: {team2_chance}")

story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

scores = {
    'A': {'Story': 6, 'Text': 5, 'Role': 4, 'Director': 3, 'Cast': 2},
    'B': {'Story': 5, 'Text': 4, 'Role': 3, 'Director': 2, 'Cast': 1},
    'C': {'Story': 4, 'Text': 3, 'Role': 2, 'Director': 1, 'Cast': 0},
    'D': {'Story': 2, 'Text': 1, 'Role': 1, 'Director': 0, 'Cast': 0},
    'F': {'Story': 0, 'Text': 0, 'Role': 0, 'Director': 0, 'Cast': 0}
}

total_score = scores[story]['Story'] + scores[text]['Text'] + scores[role]['Role'] + scores[director]['Director'] + scores[cast]['Cast']

if total_score >= 20:
    category = "Perfect score"
elif 17 <= total_score <= 19:
    category = "Must do"
elif 14 <= total_score <= 16:
    category = "Seriously consider"
elif 12 <= total_score <= 13:
    category = "On the bubble"
else:
    category = "Pass"

print(total_score)
print(category)

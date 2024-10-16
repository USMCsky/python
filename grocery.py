# grocery.py
groceries = {}
while True:
    try:
        item = input().upper()
        if item in groceries.keys():
            groceries[item] += 1
        else:
            groceries[item] = 1
            pass
    except EOFError:
        sort = dict(sorted(groceries.items()))
        break

for item in sort:
    print(groceries[item], item)
  

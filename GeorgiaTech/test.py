num = 5
result = 1
for i in range(1, num + 1):
    result *= i
print(result)
###########################
## All the following loops have the same result
for i in range(1, 6):
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1
    print("")

for i in range(1, 6):
    for j in range(0, i):
        print(j, end = " ")
    print("")

i = 0
while i < 6:
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1
    i += 1
    print("")


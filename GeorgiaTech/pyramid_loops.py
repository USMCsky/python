# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# Which of the following code segments would have the output shown above?

for i in range(0, 5):
    for j in range(0, i):
        print(j, end=" ")
    print(" ")

for i in range(5, 0):
    for j in range(5, i):
        print(j, end=" ")
    print(" ")

for i in range(5, 0, -1):
    for j in range(5, i, -1):
        print(j, end=" ")
    print(" ")

print("")

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print(" ")

for i in range(0, 5):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print(" ")
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# Which of the following code segments would have the output shown above?

i = 0
while i < 5:
    j = i
    while j > 0:
        print(j, end=" ")
        j -= 1
    i += 1
    print("")

print(" ")

i = 5
while i > 0:
    j = i
    while j > 0:
        print(j, end=" ")
        j -= 1
    i -= 1
    print("")

i = 0
while i < 5:
    j = 0
    while j < i:
        print(j, end=" ")
        j += 1
    i += 1
    print("")

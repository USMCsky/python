#
i = -2
j = 2
try:
    while i < j:
        print(j // i)
        i += 1
except:
    print("An error occurred!")
print("Done!")

# -1, -2, infinite loop
i = -2
j = 2
while i < j:
    try:
        print(j // i)
        i += 1
    except:
        print("An error occurred!")
print("Done!")

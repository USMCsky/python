my_var = 1
try:
    result = 10 // my_var
    print(result)
except (ZeroDivisionError, TypeError):
    print("An expected error occurred!")
else:
    print("No errors occurred!")
finally:
    print("Closing down...")
print("Done!")


my_var = 0
try:
    result = 10 // my_var
    print(result)
except (ZeroDivisionError, TypeError):
    print("An expected error occurred!")
else:
    print("No errors occurred!")
finally:
    print("Closing down...")
print("Done!")

my_var = "taco"
try:
    result = 10 // my_var
    print(result)
except (ZeroDivisionError, TypeError):
    print("An expected error occurred!")
else:
    print("No errors occurred!")
finally:
    print("Closing down...")
print("Done!")

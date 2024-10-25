#function set 3.4
#3.4.5
def say_good_night():
  name = "Jack"
  return "Good Night, " + name + " and "
say_good_night()
print("Jill")
#outputs Jill

print(say_good_night(), end = "")
print("Jill")
#outputs Good Night, Jack and Jill

def yay_TAs(ta1, ta2, ta3):
  result = ta3 + ", " + ta2 + ", and " + ta1 + " are awesome!"
  return result
my_string = yay_TAs("Jackie", "Joshua", "Marguerite")
print(my_string)
#outputs Marguerite, Joshua, and Jackie are awesome!

print(1, 2, 3, sep = "")
print(4, 5, 6, end = "$")
print()
print(7, 8, 9, sep = "!", end = "!")
print(0)
#outputs 
#123
#4 5 6$
#7!8!9!0



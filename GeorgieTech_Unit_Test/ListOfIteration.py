given_items = ["one", "two", 3, 4, "five", ["six", "seven", "eight"]]

#Write a program that iterates through the items in the
#given list. For each item, you should attempt to iterate
#through the item and print each character seperately.

#If this second part fails, print "Not iterable" -- but
#even if the second part fails, you should still go on
#to the next item in the list.

#Hint: Although we'll cover lists more in Unit 4, all
#you need to know right now is that this syntax will run
#a loop over a list, a string, or any other iterable
#type of information:
#To iterate over the items in 'item', you can do the
#same thing: for subitem in item:

for item in given_items:
    try:
        for subitem in item:
            print(subitem)
    except TypeError:
        print("Not iterable")

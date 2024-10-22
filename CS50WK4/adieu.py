# In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:
# Adieu, adieu, to yieu and yieu and yieu
# Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:
# Adieu, adieu, to yieu, yieu, and yieu
# In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d.
# Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and
#  names with commas.
# Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect. You can install it with:
# pip install inflect

import inflect
def main():
    p = inflect.engine()
    names = []
    print("Name:")
    try:
        while True:
            name = input()
            if name:
                names.append(name)
    except EOFError:
        pass

    if names:
        farewell = "Adieu, adieu, to " + p.join(names)
        print(farewell)

main()

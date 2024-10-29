# In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2,
# restructuring your code per the below, wherein shorten expects a str as input and returns
# that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
#original code from set 2
# twttr_post = input("Input: ")
# vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
# print("Posts: ",end="")
# for vowel in twttr_post:
#     if vowel in vowels:
#         continue
#     print(vowel, end="")

# def main():
#
# def shorten(word):
#
# if __name__ == "__main__":
#     main()
#restructured twttr.py

def main():
    twttr_post = input("Input: ")
    shortened = shorten(twttr_post)
    print("Posts:", shortened)

def shorten(word):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    result = "".join([char for char in word if char not in vowels])
    return result

if __name__ == "__main__":
    main()



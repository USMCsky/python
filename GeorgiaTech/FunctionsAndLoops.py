# Given a string and a non-negative int n, we('ll say that the front of
# the string is the first 3 chars, or whatever is there if the string is less than length
# 3. Return n copies of the front;)
#
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'
def main():
    s = input("str: ")
    n = int(input("int: "))  # Convert input to integer
    print(front_times(s, n))  # Call the function with appropriate arguments


def front_times(s, n):
    front_len = 3  # Define the number of characters for the "front"
    if front_len > len(s):  # Adjust if the string is shorter than 3 chars
        front_len = len(s)
    front = s[:front_len]

    result = ""
    for i in range(n):
        result += front  # String concatenation shorthand
    return result

main()

# Given a string, return a new string made of every other char starting with the first,
# so "Hello" yields "Hlo".
#
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'
def main():
    s = input("str: ")
    print(string_bits(s))

def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

main()

# Given an array of ints, return the number of 9's in the array.
#
# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9])
# Given an array of ints, return the number of 9's in the array.
#
# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9])

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count


def main():
    print(array_count9([1, 2, 9]))  # Output: 1
    print(array_count9([1, 9, 9]))  # Output: 2
    print(array_count9([1, 9, 9, 3, 9]))  # Output: 3

main()
#
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True
def array123(nums):
    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


def main():
    test_cases = [
        [1, 1, 2, 3, 1],
        [1, 1, 2, 4, 1],
        [1, 1, 2, 1, 2, 3]
    ]

    for case in test_cases:
        print(f"array123({case}) -> {array123(case)}")


# Call the main function
main()

import random

# Prompts user for a level. Gen and present 10 math problems.
# Tracks the num of correct answers.
# Outputs final score.
def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        attempts = 0

        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")

            attempts += 1
            if attempts == 3:
                print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")

# Prompts and re - prompts user to enter valid level(1, 2, or 3).
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


# Generates a rand int with the specified number of digits based on the level. Raises
# a ValueError if an invalid level is provided.
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()

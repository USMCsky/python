def main():
    hello(input("Enter your name: "))  # Get user input for name
    goodbye(input("Enter your name: "))  

def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":  # Check if the script is being run directly
    main()  # This will execute the main function when the script is run directly.

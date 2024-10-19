# The emojize_text function takes input text and converts any
# codes and aliases to corresponding emojis.
# The main function prompts user for a string input and then prints the emojized version of that string.
import emoji

def emojize_text(input_text):
    return emoji.emojize(input_text, language='alias')
def main():
    user_input = input("Input: ")
    emojized_output = emojize_text(user_input)
    print("Emojized version:", emojized_output)

main()

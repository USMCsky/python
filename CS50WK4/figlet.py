import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        fonts = figlet.getFonts()
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ('-f', '--font'):
        font = sys.argv[2]
        if font not in figlet.getFonts():
            print(f"Error: Font '{font}' not found.")
            sys.exit(1)
    else:
        print("Usage: figlet.py [-f FONT] [TEXT]")
        sys.exit(1)
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))

main()
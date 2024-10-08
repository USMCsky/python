### indoor voice
shout = input("TYPE SOMETHING IN ALL CAPS ")
quiet = print(shout.lower())

### playback
playback = input(" Type in something ")
slow = playback.replace(" ", "...")
print(slow)

# faces.py
def main():
    convert(input(str("Emoticons are the best :) :( PICK ONE! ")))

def convert(input):
    print(input.replace(":(", "🙁").replace(":)", "🙂"))

main()

#bitcoin.py
import requests
import sys

def arg_check():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    elif sys.argv[1].isalpha():
        sys.exit("Command-line arguement is not a number")

try:
    arg_check()
    req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate: int = req.json()["bpi"]["USD"]['rate_float']
    bit = rate * float(sys.argv[1])
    print(f"${bit,.4f}")

except requests.RequestException:
    sys.exit()

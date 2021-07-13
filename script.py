import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet():
    # name = "Hargun"
    name = input("What is your name?\n")
    print(f"Hello {name}")


greet()
r = requests.get("https://coreyms.com")
print(r.status_code)

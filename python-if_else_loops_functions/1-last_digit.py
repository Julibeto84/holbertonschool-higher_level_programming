#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
else:
    last = number % 10
strg = f"Last digit of {number} is {last} and is"
if last > 5:
    print(f"{strg} greater than 5")
elif last == 0:
    print(f"{strg} 0")
elif last != 0 and last < 6:
    print(f"{strg} less than 6 and not 0")

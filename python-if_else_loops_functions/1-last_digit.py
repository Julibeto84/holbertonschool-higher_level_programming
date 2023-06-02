#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 10:
    opnumber = number * -1
    last_digit = (opnumber % 10) * -1
else:
    opnumber = number
    last_digit = opnumber % 10
if last_digit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_digit))
elif last_digit > 5:
    print("Last digit of {:d} is {:d} and is greater \
than 5".format(number, last_digit))
else:
    print("Last digit of {:d} is {:d} and is less \
than 6 and not 0".format(number, last_digit))

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNum = number % 10
if lastNum > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastNum))
elif lastNum == 0:
    print("Last digit of {} is {} and is 0".format(number, lastNum))
else:
    lastNum = number % -10
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastNum))

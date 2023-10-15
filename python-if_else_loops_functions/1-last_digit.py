#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if ld > 5:
    positive_string = "Last digit of {} is {} and is greater than 5"
    print(positive_string.format(number, ld))
elif ld == 0:
    Zero_string = "Last digit of {} is {} and is 0"
    print(Zero_string.format(number, ld))
else:
    ld = number % -10
    negative_string = "Last digit of {} is {} and is less than 6 and not 0"
    print(negative_string.format(number, ld))

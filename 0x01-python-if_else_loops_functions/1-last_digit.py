#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

exc = 0
if number < 0:
    exc = 1
    number *= -1

lastd = number % 10

if exc == 1:
    number *= -1
    lastd *= -1

print("Last digit of {:d} is ".format(number), end="")
if lastd > 5:
    print("{:d} and is greater than 5".format(lastd))
elif lastd == 0:
    print("{:d} and is 0".format(lastd))
else:
    print("{:d} and is less than 6 and not 0".format(lastd))

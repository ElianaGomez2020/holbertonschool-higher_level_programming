#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastd = (number * -1) % 10
    lastd = lastd * -1
else:
    lastd = number % 10
print('Last digit of', number, 'is', lastd, end =' ')
if lastd > 5:
    print('and is greater than 5')
elif lastd == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')

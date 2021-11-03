# Import module

from math import pi, sin
from random import randint

print(pi)
print(sin(1))

print(randint(10, 20))

count = 0
while True:
    n = randint(1, 10)
    print(n)
    count += 1
    if n == 7:
        break

print('We find 7 in ', count, 'times')

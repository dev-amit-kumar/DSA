# import the math module
import math


def prime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True


def primeBetter(num):
    x = int(math.sqrt(num)+1)
    for i in range(2, x):
        if(num % i == 0):
            return False
    return True


number = 6
result = prime(number)
print(result)
result = primeBetter(number)
print(result)

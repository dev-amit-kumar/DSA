# https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/

import math


def allPrime(n):
    if (n == 2 or n == 1 or n == 3):
        return n
    all = []
    while(n % 2 == 0):
        n = n // 2
        all.append(2)

    for i in range(3, int(math.sqrt(n))+1, 2):
        while(n % i == 0):
            all.append(i)
            n = n // i

    if n > 2:
        all.append(n)
    return all


n = 315
all = allPrime(n)
print(all)

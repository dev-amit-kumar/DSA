def findZeroes(n):
    if(n < 0):
        return -1
    total = 0
    while(n >= 5):
        n //= 5
        print(n)
        total += n
        print(total)
    return total


n = 100
zeroes = findZeroes(n)
print(zeroes)

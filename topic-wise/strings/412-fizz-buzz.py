# https://leetcode.com/problems/fizz-buzz/

def check(i):
    if (i % 5 == 0 and i % 3 == 0):
        return "FizzBuzz"
    elif (i % 3 == 0):
        return "Fizz"
    elif (i % 5 == 0):
        return "Buzz"
    else:
        return i


if __name__ == '__main__':
    n = int(input("Enter no"))
    a = []
    for i in range(1, n+1):
        a.append(check(i))
    print(a)

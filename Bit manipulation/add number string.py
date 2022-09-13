num1 = input()
num2 = input()

res = []
carry = 0
len_a = len(num1)-1
len_b = len(num2)-1

while len_a >= 0 or len_b >= 0:
    if (len_a >= 0):
        x = 0
    else:
        x = ord(num1[len_a]) - ord('0')

    if (len_a >= 0):
        y = 0
    else:
        y = ord(num2[len_b]) - ord('0')

    sum = (x + y + carry) % 10
    carry = (x + y + carry) // 10
    len_a -= 1
    len_b -= 1

    res.append(sum)
    print(sum)

if carry:
    res.append(carry)

print(res)

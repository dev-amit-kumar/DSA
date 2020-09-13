x = int(input())
len_x = len(str(x)) + 1
ans = 0
for i in range(1, len_x, 1):
    rem = x % 10
    x = x // 10

    ans = ans + rem
    ans = ans * 10

print(ans // 10)
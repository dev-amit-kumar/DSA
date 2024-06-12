n = 12345

# reverse_n * 10 + temp
# 0 * 10 + 5 = 5
# 5 * 10 + 4 = 54
# 54 * 10 + 3 = 543
# 543 * 10 + 2 = 5432
# 5432 * 10 + 1 = 54321

reverse_n=0
while(n>0):
    temp=n%10
    n=int(n/10)
    reverse_n= reverse_n * 10 + temp
print(reverse_n)

# n = 12345

# 12345
# 1234
# 123
# 12
# 1

# 0
counter = 0
while(n > 0):
    n = int(n / 10)
      temp = n % 10
    counter+=1
print(counter)
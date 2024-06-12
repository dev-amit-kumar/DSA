n = 121
dup = n
reverse_n = 0

while (n>0):
    temp = n % 10
    n= n // 10
    reverse_n = (reverse_n * 10) + temp

if str(dup) == str(reverse_n):
    print("No is Pallidrome")
else:
    print("No is not pallidrome")


# Check palindrome for strings
a = "naman"
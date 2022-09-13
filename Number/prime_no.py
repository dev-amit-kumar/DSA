# Python Program to find Prime Number
 
Number = int(input(" Please Enter any Number: "))
flag = 0
i = 2

while(i <= Number//2):
    if(Number % i == 0):
        flag = 1
        break
    i = i + 1

if (flag == 0 and Number != 1):
    print(Number, " is a Prime Number")
else:
    print(Number, " is not a Prime Number")
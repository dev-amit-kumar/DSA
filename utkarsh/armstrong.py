n = 153
duplicate = n
total = 0
while(n > 0):
    temp = n % 10
    n = int (n/10)
    total = total + (temp * temp * temp)
if(total == duplicate):
    print("Armstrong number")
else:
    print("Not a armstrong number")
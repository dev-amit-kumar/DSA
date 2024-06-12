n = 14
isPrime = True
for i in range(2, n):
    if(n % i == 0):
        isPrime = False
        break
print("Number is Prime ? - ", isPrime)
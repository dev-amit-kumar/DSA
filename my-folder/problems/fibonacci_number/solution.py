class Solution:
    def fib(self, N: int) -> int:
        f=[0 for i in range(N+1)]
        if N==0:
            return 0
        if N==1:
            return 1
        f[0]=0
        f[1]=1
        for i in range(2,N+1):
            f[i]=f[i-1]+f[i-2]
        return f[N]
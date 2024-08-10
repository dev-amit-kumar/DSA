class Solution:
    def recursion(self, n: int, dp) -> int:
        if(n <= 1):
            return n
        if (n in dp):
            return dp[n]
        dp[n] = self.recursion(n-1, dp) + self.recursion(n-2, dp)
        return dp[n]

    def fib(self, n: int) -> int:
        dp = {}
        return self.recursion(n, dp)
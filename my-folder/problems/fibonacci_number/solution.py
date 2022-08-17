class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 1
        # a = 0
        # b = 1
        # c = 1
        # if(n == 0):
        #     return a
        # elif (n == 1):
        #     return b
        # else:
        #     for i in range(1, n):
        #         c = a + b
        #         a = b
        #         b = c
        #     return b
        # Approach 2
        if (n == 0 or n == 1):
            return n
        return self.fib(n-1) + self.fib(n-2)
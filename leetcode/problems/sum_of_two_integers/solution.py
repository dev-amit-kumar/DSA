class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = pow(2, 32) - 1
        while b & mask:
            a, b = a ^ b, (a & b) << 1
        return a & mask if b > 0 else a

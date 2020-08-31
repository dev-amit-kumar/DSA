class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        neg = 1
        if x < 0:
            neg = -1
        x = abs(x)
        while x != 0:
            temp = x % 10
            x = int(x / 10)
            rev = rev * 10 + temp
        if rev >= 2 ** 31 or rev <=  - 2 ** 31:
            return 0
        return rev*neg
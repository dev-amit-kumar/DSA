class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            palindrome = x
            new = 0
            while x > 0:
                temp = x %10
                x = x //10
                new = new*10 + temp
            return new == palindrome
        else:
            return False
        
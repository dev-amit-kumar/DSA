class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open = 0
        close = 0
        left = 0
        ans = ""
        for i in range(0, len(s)):
            if (s[i] == "("):
                left = i if open == 0 else left
                open += 1
            else:
                close += 1
            if (open == close):
                ans += s[left+1: i]
                open = 0
                close = 0
        return ans

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        mid = n // 2
        def rec(s, i):
            if i == mid:
                return
            s[i], s[n-1-i] = s[n-1-i], s[i]
            rec(s, i+1)
        rec(s, 0)
        return s
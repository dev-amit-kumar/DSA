class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in range(0, len(t)):
            if j == len(s):
                break
            if t[i] == s[j]:
                j += 1
        return j == len(s)
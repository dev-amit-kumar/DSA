class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2: return ''
        seen = set(s)
        for i in range(len(s)):
            if s[i].lower() in seen and s[i].upper() in seen: 
                continue
            left = self.longestNiceSubstring(s[:i])
            right = self.longestNiceSubstring(s[i + 1:])
            return max(left, right, key=len)
        return s
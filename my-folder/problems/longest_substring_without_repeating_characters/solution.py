class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        if(len(str) == 1):
            return 1
        res = 0
        left = 0
        right = 0
        seen = {}
        while(right < len(str)):
            if(str[right] in seen):
                left = max(seen[str[right]] + 1, left)
            seen[str[right]] = right
            res = max(res, right - left + 1)
            right += 1
        return res
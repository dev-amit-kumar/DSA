class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        window = 3
        n = len(s)
        count = 0
        for i in range(0, n-2):
            currS = list(s[i: i+window])
            set_ = set(currS)
            if len(set_) == 3:
                count += 1
        return count
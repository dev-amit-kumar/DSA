class Solution:
    def sortString(self, s: str) -> str:
        result = ""
        counts = {}
        letters = sorted(set(s))
        letters = list(letters)
        for char in s:
            counts[char] = s.count(char)
        while len(result)<len(s):
            for l in letters:
                if counts[l] > 0:
                    result += l
                    counts[l] -= 1
            for l in letters[::-1]:
                if counts[l] > 0:
                    result += l
                    counts[l] -= 1
        return result
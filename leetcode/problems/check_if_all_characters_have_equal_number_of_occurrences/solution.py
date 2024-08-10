class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        occ = -1
        for key, values in freq.items():
            if occ == -1:
                occ = values
            elif occ != values:
                return False
        return True

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        abc = [None] * len(s)
        for i in range(len(indices)):
            abc[indices[i]] = s[i]
        return ''.join(map(str, abc))
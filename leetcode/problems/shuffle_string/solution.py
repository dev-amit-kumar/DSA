class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        data = ['i'] * len(s)
        for i in range(0, len(indices)):
            index = indices[i]
            value = s[i]
            data[index] = value
        return ''.join(data)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry != 0:
            curr = carry
            if i >= 0:
                curr += int(a[i])
                i -= 1
            if j >= 0:
                curr += int(b[j])
                j -= 1
            carry = curr // 2
            result = str(curr % 2) + result
        return result
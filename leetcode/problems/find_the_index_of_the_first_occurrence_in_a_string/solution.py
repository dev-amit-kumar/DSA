class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        ans = -1
        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                if len(haystack[i:]) < len(needle):
                    return -1
                x = 0
                for j in range(i, i+len(needle)):
                    if haystack[j] == needle[x]:
                        x += 1

                if x == len(needle):
                    return i

        return ans
        
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        i = 0
        n = len(s)
        while(i < n):
            stack.append(s[i])
            if (len(stack) > 1 and stack[-1] == stack[-2]):
                stack.pop()
                stack.pop()
            i += 1
        return ''.join(stack)
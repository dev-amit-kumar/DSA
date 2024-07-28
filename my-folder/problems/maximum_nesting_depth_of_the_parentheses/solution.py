class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        stack = []
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == ")":
                stack.pop()
            depth = max(depth, len(stack))
        return depth
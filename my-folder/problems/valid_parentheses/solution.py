class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if(stack and ((stack[-1] + i) == "()" or (stack[-1] + i) == "{}" or (stack[-1] + i) == "[]")):
                stack.pop()
            else:
                stack.append(i)
        return stack == []

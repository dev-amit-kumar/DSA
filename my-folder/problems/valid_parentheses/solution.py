class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if(i == "(" or i == "{" or i == "["):
                stack.append(i)
            else:
                stack.append(i)
            if(len(stack) >1):
                if(stack and ((stack[-2] + i) == "()" or (stack[-2] + i) == "{}" or (stack[-2] + i) == "[]")):
                    stack.pop()
                    stack.pop()
        if(len(stack) == 0):
            return True
        else:
            return False

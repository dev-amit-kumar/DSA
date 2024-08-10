class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if (i in [")", "}", "]"]):
                if (len(stack) == 0):
                    return False
                if (i == ")" and stack[-1] == "("):
                    stack.pop()
                elif (i == "}" and stack[-1] == "{"):
                    stack.pop()
                elif (i == "]" and stack[-1] == "["):
                    stack.pop()
                else: return False
            elif(i in ["(", "[", "{"]):
                stack.append(i)
            else:
                return False
        return True if len(stack) == 0 else False
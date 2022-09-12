'''def isValid(s):
    stack = []
    open_close_p = {"(" : ")", "{": "}", "[": "]"}
    open_p = ("(", "{", "[")
    for i in s:
        if i in open_p:
            stack.append(i)
        elif stack and i==open_close_p[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []'''
'''class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if(stack and ((stack[-1] + i) == "()" or (stack[-1] + i) == "{}" or (stack[-1] + i) == "[]")):
                stack.pop()
            else:
                stack.append(i)
        return stack == []
'''
'''
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
'''


def isValid(s):
    stack = []
    open_close_p = {"(": ")", "{": "}", "[": "]"}
    for i in s:
        if (stack and i == open_close_p[stack[-1]]):
            stack.pop()
        else:
            stack.append(i)
    return stack == []


if __name__ == "__main__":
    s = input()
    print(isValid(s))

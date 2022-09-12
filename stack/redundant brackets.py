# Link:
# https://www.codingninjas.com/codestudio/problems/redundant-brackets_975473

def findRedundantBrackets(s):
    stack = []
    operators = ["*", "+", "/", "-"]
    for i in range(0, len(s)):
        if (s[i] == "("):
            stack.append("(")
        elif (s[i] == ")"):
            if (stack[-2] == "(" and stack[-1] in operators):
                stack.pop()
                stack.pop()
            else:
                return True
        elif (s[i] in operators):
            stack.append(s[i])
    return False


str = "(a+((b*c)))"
result = findRedundantBrackets(str)
print(result)

def insertAtBottom(stack1, element):
    if (len(stack1) == 0):
        return stack1.append(element)
    num = stack1.pop()
    insertAtBottom(stack1, element)
    stack1.append(num)
    return stack1


def solve(stack):
    if (len(stack) == 0):
        return stack
    num = stack.pop()
    solve(stack)
    new = insertAtBottom(stack, num)
    return new


def reverseStack(stack):
    return solve(stack)


stack = [0, 1, 2, 3, 4, 5]
print(reverseStack(stack))

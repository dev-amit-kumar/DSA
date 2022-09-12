# Link: https://www.codingninjas.com/codestudio/problems/sort-a-stack_985275

def sortLogic(stack1, element):
    if (len(stack1) <= 1 or element >= stack1[-1]):
        stack1.append(element)
        return stack1
    num = stack1.pop()
    sortLogic(stack1, element)
    stack1.append(num)
    return stack1


def sortStack(stack):
    if (len(stack) <= 1):
        return stack
    num = stack.pop()
    sortStack(stack)
    new = sortLogic(stack, num)
    return new


stack = [1, 4, 5, 3, 2, 2]
print(sortStack(stack))

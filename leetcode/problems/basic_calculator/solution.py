class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        number = 0
        sign = 1
        stack = []
        for i in s:
            if i.isdigit():
                number = number * 10 + int(i)
            elif i in "+-":
                result += (number * sign)
                sign = -1 if i == '-' else 1
                number = 0
            elif i == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif i == ")":
                result += sign * number
                result *= stack.pop()
                result += stack.pop()
                number = 0
        return result + number * sign
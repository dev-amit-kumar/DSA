class Solution:
    def interpret(self, command: str) -> str:
        result = ''
        temp = ''
        for i in command:
            if i == "G":
                result += 'G'
            elif i == "(":
                temp = i
            elif i == ")":
                temp += i
                if temp == "()":
                    result += "o"
                else:
                    result += 'al'
                temp = ''
            else:
                temp += i
        return result
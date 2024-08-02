class Solution:
    def defangIPaddr(self, address: str) -> str:
        newStr = ''
        for i in address:
            if i == '.':
                newStr += '[.]'
            else:
                newStr += i
        return newStr
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        sum = 0
        carry = 0
        len_a = len(num1)-1
        len_b = len(num2)-1

        while len_a >= 0 or len_b >= 0:
            if(len_a >= 0):
                x = ord(num1[len_a]) - ord('0')
            else:
                x = 0

            if(len_b >= 0):
                y = ord(num2[len_b]) - ord('0')
            else:
                y = 0

            sum = (x + y + carry) % 10
            carry = (x + y + carry) // 10
            len_a -= 1
            len_b -= 1

            res.append(sum)

        if (carry == 1):
            res.append(carry)
        
        return ''.join(str(x) for x in res[::-1])
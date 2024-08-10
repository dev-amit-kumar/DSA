'''
Remove K digits
Given a non-negative integer represented as a string num and an integer k, remove k digits from the number so that the new number is the smallest possible. The remaining digits should maintain their original order in the string. Return the result as a string.

Input Format:

The first line contains the string num, representing the non-negative integer.
The second line contains the integer k.
Output Format:

Print the smallest possible integer as a string after removing k digits.
Sample Input 1:

1432219
3
Sample Output 1:

1219
Explanation:

Removing the digits 4, 3, and 2 from "1432219" leads to the new number "1219", which is the smallest possible result.

Sample Input 2:

10200
1
Sample Output 2:

200
Explanation:

Removing one digit (the leading 1) from "10200" results in "0200", and removing the leading zeroes gives "200" as the smallest possible result.

Constraints:
1<=k<= num.length<= 100000
num contains of only digits
'''
'''
To solve the problem of removing `k` digits from the given number represented as a string `num` to obtain the smallest possible number, you can use a stack-based approach. The idea is to ensure that the digits are as small as possible by removing digits that are larger and have smaller digits following them.

Here's a step-by-step approach to solve the problem:

1. **Initialize an Empty Stack**: Use a stack to build the result.

2. **Iterate Over Digits**: For each digit in the string, compare it with the top of the stack.
   - If the current digit is smaller than the top of the stack, and you still have digits to remove (`k > 0`), pop the stack. This is because removing a larger digit will likely result in a smaller number.
   - Push the current digit onto the stack.

3. **Handle Remaining Removals**: If there are still digits left to remove after processing all digits, remove them from the end of the stack.

4. **Construct the Result**: Convert the stack to a string and remove any leading zeros.

### Explanation of the Code:

1. **Iterate Through Digits**: For each digit, compare it with the top of the stack. If the digit is smaller than the stack's top, pop from the stack (removing a larger digit) until you can't or until you've removed `k` digits.

2. **Append Digits**: Always push the current digit onto the stack after processing removals.

3. **Handle Remaining Removals**: If there are still removals left after processing all digits, remove from the end of the stack.

4. **Create Result String**: Convert the stack to a string and remove any leading zeros. Return `'0'` if the result is empty to handle edge cases.

This approach ensures that the resulting number is the smallest possible while maintaining the original order of digits and efficiently handles the removals.
'''

class Solution:
    def removeKdigits(self, s, k):
        stack = []
        for digit in s:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0:
            stack.pop()
            k -= 1
        result = ''.join(stack).lstrip('0')
        return result if result else '0'
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack to keep track of indices. The first element is initialized to -1
        # to handle edge cases where the valid substring starts from the beginning.
        stack = [-1]
        max_length = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                # Index of the last unmatched '('
                stack.pop()
                if not stack:
                    # Stack is empty, meaning there was no matching '('
                    # Push the current index as the new base
                    stack.append(i)
                else:
                    # Stack is not empty, meaning we have found a matching pair
                    # After popping, stack[-1] is either the index of the last unmatched '(' or
                    # the left boundary of the current valid substring,
                    # which can be -1, or the index of an invalid ')'. 
                    # Current substring spans from stack[-1] + 1 to i. 
                    max_length = max(max_length, i - stack[-1])

        return max_length
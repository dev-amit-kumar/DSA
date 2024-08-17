class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        arr = []
        def backtrack(sub, i):
            if len(sub) == len(s):
                arr.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub+s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)

        backtrack('', 0)
        return arr
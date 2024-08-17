class Solution:
    def helper(self, answerKey: str, k: int, ch: bool) -> int:
        left, ans, count = 0, 0, 0
        for i in range(len(answerKey)):
            if answerKey[i] == ch:
                count += 1
            while count > k:
                if answerKey[left] == ch:
                    count -= 1
                left += 1
            ans = max(ans, i-left+1)
        return ans

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.helper(answerKey, k, 'T'), self.helper(answerKey, k, 'F'))
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l = k - 1
        r = n - 1
        initial_sum = sum(cardPoints[:k])
        max_sum = initial_sum

        for _ in range(k):
            initial_sum += (cardPoints[r] - cardPoints[l])
            max_sum = max(max_sum, initial_sum)
            l -= 1
            r -= 1
        return max_sum

class Solution:
    def subsets(self, nums):
        ans = []
        current = []
        self.backtrack(nums, len(nums), 0, [], ans)
        return ans

    def backtrack(self, nums, n, i, current, ans):
        if i == n:
            ans.append(current)
            return
        self.backtrack(nums, n, i+1, current, ans)
        self.backtrack(nums, n, i+1, current + [nums[i]], ans)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[0: n]
        y = nums[n: 2*n]
        ans = []
        for i in range(0, n):
            ans.append(x[i])
            ans.append(y[i])
        return ans
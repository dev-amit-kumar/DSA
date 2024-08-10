class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr=float('inf')
        mins=float('inf')
        curr1=float('-inf')
        maxs1=float('-inf')
        total=0
        for i in nums:
            curr1=max(curr1+i,i)
            maxs1=max(maxs1,curr1) # check whether cur max is bigger or prev max is bigger
        for i in nums:
            total+=i
            curr=min(curr+i,i)
            mins=min(mins,curr)
        if (mins==total) :
            return maxs1
        return max(maxs1,total-mins)
# subtracting the minimum subarray sum from the total sum gives the maximum sum of the subarray.
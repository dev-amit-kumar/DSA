class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Brute force solution
        # nums.sort()
        # ans = []
        # for i in range(0, len(nums)):
        #     if nums[i] == target:
        #         ans.append(i)
        #     elif nums[i] > target:
        #         break
        # return ans

        # Binary search solution
        nums.sort()
        start, end = -1, -1

        # Find first occurence
        left = 0
        right = len(nums) - 1
        while(left <= right):
            middle = (left + right) // 2
            if (target == nums[middle]):
                start = middle
                right = middle - 1
            elif (target < nums[middle]):
                right = middle - 1
            elif (target > nums[middle]):
                left = middle + 1

        # Find second occurence
        left = start
        right = len(nums) - 1
        while(left <= right):
            middle = (left + right) // 2
            if (target == nums[middle]):
                end = middle
                left = middle + 1
            elif (target < nums[middle]):
                right = middle - 1
            elif (target > nums[middle]):
                left = middle + 1
        if start == end == -1:
            return []
        return list(range(start, end+1))
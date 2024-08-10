from copy import deepcopy

class Solution(object):
    def subsets(self, nums):
        total_sets = []
        def subsetsFn(nums, l, r, total):
            if l>r:
                total_sets.append(total)
                return
            new_total = deepcopy(total)
            new_total.append(nums[l])
            subsetsFn(nums, l+1, r, new_total)
            subsetsFn(nums, l+1, r, total)
        subsetsFn(nums, 0, len(nums)-1, [])
        return total_sets
        
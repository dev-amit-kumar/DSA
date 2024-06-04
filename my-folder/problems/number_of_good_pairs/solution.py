class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Brute force
        # ans = []
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] == nums[j]):
        #             ans.append([i,j])
        # return len(ans)

        # using hash_map
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        total = 0
        for i in nums:
            # if hash[i] == 1:
            #     total += 0
            if hash[i] > 1:
                a = hash[i]
                val = ((a)*(a-1))/2
                total += val
                hash[i] = 0
        return int(total)
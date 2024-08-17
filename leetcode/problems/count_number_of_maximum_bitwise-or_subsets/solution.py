class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for num in nums:
            temp = dict(mp)        
            for t in temp:
                mp[t|num] += temp[t]
            mp[num] += 1

        return mp[max(mp.keys())]
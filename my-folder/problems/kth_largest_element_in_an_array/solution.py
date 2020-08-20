class Solution :
    def findKthLargest ( self , nums , k ):
        dict = {}
        for num in nums:
            if num not in dict :
                dict[num] = 1
            else :
                dict[num] += 1
        ans = []
        for i in range ( min (nums), max (nums) + 1 ):
            if i in dict .keys():
                count = dict[i]
                while count: 
                    ans.append(i)
                    count -= 1
                    if len (ans) == len (nums) - (k - 1 ):
                        return ans[- 1] 
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_no = max(candies)
        ans = []
        for i in candies:
            curr = False
            if(i + extraCandies >= max_no):
                curr = True
            ans.append(curr)
        return ans
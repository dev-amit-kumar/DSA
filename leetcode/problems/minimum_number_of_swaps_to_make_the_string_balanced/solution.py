class Solution:
    def minSwaps(self, s: str) -> int:
        maxClosing = 0
        maxCount = 0

        for brac in s:
            if brac == "]":
                maxClosing +=1
            else:
                maxClosing -=1
            
            maxCount = max(maxCount ,maxClosing)
        
        return math.floor((maxCount+1)/2)
                
        
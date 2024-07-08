class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        freq = {}
        count = 0
        for x,y in rectangles:
            ratio = x / y
            if ratio in freq:
                freq[ratio] += 1
                count += freq[ratio]
            else:
                freq[ratio] = 0
        return count
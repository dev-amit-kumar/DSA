class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)

        # copy the first intervals which are not overlapping and occur before the newInterval
        while (i < n and intervals[i][1] < newInterval[0]):
            i += 1
        
        beforeOverlap = i

        # create new interval based on the overlapping
        while(i < n and intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # return the result
        return intervals[:beforeOverlap] + [newInterval] + intervals[i:]
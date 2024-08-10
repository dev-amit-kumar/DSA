class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            first, second = intervals[i]
            if first > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif second < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [min(first, newInterval[0]), max(second, newInterval[1])]
        res.append(newInterval)
        return res
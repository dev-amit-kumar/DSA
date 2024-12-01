class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = [intervals[0]]
        for a, b in intervals:
            if a > result[-1][1]:
                result.append([a,b])
            else:
                result[-1][1] = max(result[-1][1], b)
        return result
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        position = 0
        heap = [-x for x in score]
        heapq.heapify(heap)
        result = [-1] * len(score)
        while heap:
            top = heapq.heappop(heap)
            position += 1
            index = score.index(top * -1)
            match position:
                case 1:
                    result[index] = "Gold Medal"
                case 2:
                    result[index] = "Silver Medal"
                case 3:
                    result[index] = "Bronze Medal"
                case _:
                    result[index] = str(position)
        return result
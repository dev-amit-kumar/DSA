class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for circle in queries:
            count = 0 
            for point in points:
                x = point[0] - circle[0]
                y = point[1] - circle[1]
                c = (x ** 2 + y ** 2) ** 0.5
                if c <= circle[2]:
                    count += 1
            answer.append(count)
        return answer
        
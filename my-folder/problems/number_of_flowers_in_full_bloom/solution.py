class Solution:
    def binarySearch(self, arr, target):
        l = 0
        r = len(arr)
        while(l < r):
            mid = (l+r)//2
            if target < arr[mid]:
                r = mid
            else:
                l = mid + 1
        return l

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        n = len(flowers)
        start = [0] * n
        end = [0] * n
        for i in range(n):
            start[i] = flowers[i][0]
            end[i] = flowers[i][1] + 1
        start.sort()
        end.sort()

        result = []

        for person in people:
            endDay = self.binarySearch(end, person)
            startDay = self.binarySearch(start, person)
            result.append(startDay - endDay)
        return result
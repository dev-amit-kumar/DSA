class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        seenNumbers = set()
        seenNumbers.add(1)
        prime_factors = [2, 3, 5]
        current_ugly = 1
        for _ in range(n):
            current_ugly = heapq.heappop(minHeap)
            for prime in prime_factors:
                next_ugly = current_ugly * prime
                if next_ugly not in seenNumbers:
                    heapq.heappush(minHeap, next_ugly)
                    seenNumbers.add(next_ugly)
        return current_ugly
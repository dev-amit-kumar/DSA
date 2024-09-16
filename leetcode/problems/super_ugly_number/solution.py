class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        minHeap = [1]
        seen = set()
        seen.add(1)
        current = 1
        for _ in range(n):
            current = heapq.heappop(minHeap)
            for prime in primes:
                next_ugly = current * prime
                if next_ugly not in seen:
                    heapq.heappush(minHeap, next_ugly)
                    seen.add(next_ugly)
        return current
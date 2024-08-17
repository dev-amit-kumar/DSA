from collections import deque
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []
        max_deque = deque()

        for i in range(n):
            if max_deque and max_deque[0] < i - k + 1:
                max_deque.popleft()
            while max_deque and nums[max_deque[-1]] < nums[i]:
                max_deque.pop()
            max_deque.append(i)
            if i >= k - 1:
                start = i - k + 1
                max_val = nums[max_deque[0]]
                is_consecutive = True
                for j in range(start, start + k - 1):
                    if nums[j] + 1 != nums[j + 1]:
                        is_consecutive = False
                        break
                if is_consecutive:
                    results.append(max_val)
                else:
                    results.append(-1)
        return results

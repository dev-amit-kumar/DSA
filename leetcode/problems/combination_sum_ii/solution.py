class Solution:
    def solve(self, candidates, target, arr, n, curr, i):
        total = sum(curr)
        if total == target:
            arr.append(curr[:])
            return
        if i >= n or total > target:
            return
        curr.append(candidates[i])
        self.solve(candidates, target, arr, n, curr, i+1)
        curr.pop()
        for j in range(i+1, n):
            if candidates[i] != candidates[j]:
                self.solve(candidates, target, arr, n, curr, j)
                break

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        arr = []
        self.solve(candidates, target, arr, len(candidates), [], 0)
        return arr
        
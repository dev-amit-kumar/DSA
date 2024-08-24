class Solution:
    def solve(self, candidates, target, arr, n, curr, i):
        total = sum(curr)
        if total == target:
            arr.append(curr[:])
            return
        if i >= n or total > target:
            return
        self.solve(candidates, target, arr, n, curr, i+1)
        curr.append(candidates[i])
        self.solve(candidates, target, arr, n, curr, i)
        curr.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = []
        self.solve(candidates, target, arr, len(candidates), [], 0)
        return arr
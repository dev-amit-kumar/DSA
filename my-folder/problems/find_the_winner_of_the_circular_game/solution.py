class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n+1))
        index = 0
        while(len(arr) > 1):
            kk = (index + k - 1) % len(arr)
            arr.pop(kk)
            index = kk
        return arr[0]
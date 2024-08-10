class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            val = arr[i]*2
            if val in arr and arr.index(val) != i:
                return True
        return False
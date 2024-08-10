class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arrFreq = {}
        for num in arr:
            arrFreq[num] = arrFreq.get(num, 0) + 1
        for num in target:
            if num not in arrFreq:
                return False
            arrFreq[num] -= 1
            if arrFreq[num] == 0:
                del arrFreq[num]
        return len(arrFreq) == 0
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for arr in image:
            arr.reverse()
            for i in range(0, len(arr)):
                arr[i] = 0 if arr[i] == 1 else 1
            result.append(arr)
        return result
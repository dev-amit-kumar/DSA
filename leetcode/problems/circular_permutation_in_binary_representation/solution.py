class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        if n == 1:
            if start == 0: return [0, 1]
            else: return [1, 0]

        S = [0, 1]
        for m in range(2, n+1):
            p = 1 << (m-1)
            S.extend(p + S[k] for k in range(len(S)-1, -1, -1))

        i = S.index(start)
        if i: return S[i:] + S[:i]
        else: return S
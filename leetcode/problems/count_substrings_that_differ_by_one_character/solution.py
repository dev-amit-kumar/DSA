class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        equal_prev, unequal_prev = [0] * (lt+1), [0] * (lt+1)
        ans = 0
        for i in range(ls):
            equal_curr, unequal_curr = [0] * (lt+1), [0] * (lt+1)
            for j in range(lt):
                if(s[i] == t[j]):
                    equal_curr[j+1] = 1+equal_prev[j]
                unequal_curr[j+1] = 1+equal_prev[j] if(s[i] != t[j]) else unequal_prev[j]
                ans += unequal_curr[j+1]
            equal_prev, unequal_prev = equal_curr, unequal_curr
        return ans
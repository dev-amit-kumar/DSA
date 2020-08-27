class Solution:
            
    def numDecodings(self, s: str) -> int:
        combos = 1
        prev_combos = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                
                combos, prev_combos = 0, combos
            elif i + 1 < len(s) and s[i:i+2] <= "26":
                
                combos, prev_combos = combos + prev_combos, combos
            else:
                combos, prev_combos = combos, combos
        return combos
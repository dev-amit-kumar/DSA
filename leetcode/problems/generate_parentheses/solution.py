class Solution:
    def generate(self, left, right, ans, s, n):
        if left == right == n:
            ans.append(s)
            return
        if left < n:
            self.generate(left + 1, right, ans, s + "(", n)
        if right < left:
            self.generate(left, right + 1, ans, s + ")", n)
        return
        

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generate(0, 0, ans, "", n)
        return ans

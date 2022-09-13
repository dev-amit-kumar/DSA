# class Solution(object):
#    def generateParenthesis(self, n):
#       """
#       :type n: int
#       :rtype: List[str]
#       """
#       result = []
#       self.generateParenthesisUtil(n,n,"",result)
#       return result
#    def generateParenthesisUtil(self, left,right,temp,result):
#       if left == 0 and right == 0:
#          result.append(temp)
#          return
#       if left>0:
#          self.generateParenthesisUtil(left-1,right,temp+'(',result)
#       if right > left:
#          self.generateParenthesisUtil(left, right-1, temp + ')', result)
# ob = Solution()
# print(ob.generateParenthesis(10))
def find(openB, closeB, n, s, ans):
    if (closeB == n):
        ans.append(''.join(s))
        return
    else:
        if (openB > closeB):
            s.append(')')
            find(openB, closeB+1, n, s, ans)
            s.pop()
        if (openB < n):
            s.append('(')
            find(openB+1, closeB, n, s, ans)
            s.pop()
    return


ans = []
s = []
find(0, 0, 2, s, ans)
print(ans)


class Solution(object):
    def generateParenthesis(self, N):
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans


class Solution1(object):
    def generateParenthesis(self, N):
        ans = []

        def find(openB, closeB, N, s):
            if (closeB == N):
                ans.append(''.join(s))
                return
            else:
                if (openB > closeB):
                    s.append(')')
                    find(openB, closeB+1, N, s)
                    s.pop()
                if (openB < N):
                    s.append('(')
                    find(openB+1, closeB, N, s)
                    s.pop()
            return
        find(0, 0, N, [])
        return ans

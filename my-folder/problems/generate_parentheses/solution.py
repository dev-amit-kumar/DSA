class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def find(openB, closeB, N, s):
            if(closeB == N):
                ans.append(''.join(s))
                return
            else:
                if(openB>closeB):
                    s.append(')')
                    find(openB, closeB+1, N, s)
                    s.pop()
                if(openB<N):
                    s.append('(')
                    find(openB+1, closeB, N ,s)
                    s.pop()
            return
        find(0,0,N,[])
        return ans
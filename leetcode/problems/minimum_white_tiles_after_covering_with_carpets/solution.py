class Solution:

    def check(self,s,dp,i,j,n,k,l):
        if(i>=n):return 0
        if(dp[i][j]!=-1):return dp[i][j]
        if(s[i]=='0'):
            dp[i][j]=self.check(s,dp,i+1,j,n,k,l)
            return dp[i][j]
        dp[i][j]=1+self.check(s,dp,i+1,j,n,k,l)
        if(j<k):dp[i][j]=min(dp[i][j],self.check(s,dp,i+l,j+1,n,k,l))
        return dp[i][j]


    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n=len(floor)
        dp=[[-1 for i in range(numCarpets+1)] for j in range(n)]
        return self.check(floor,dp,0,0,n,numCarpets,carpetLen)
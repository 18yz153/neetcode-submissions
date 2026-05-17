class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]

        def dfs(i,j):
            if dp[i][j] != 0:
                return dp[i][j]
            r = 1
            for di,dj in [[0,1],[0,-1],[-1,0],[1,0]]:
                newi=i+di
                newj = j+dj
                if 0<=newi<m and 0<=newj<n:
                    if matrix[i][j]<matrix[newi][newj]:
                        r= max(r,dfs(newi,newj)+1)
            return r
        res = 0            
        for i in range(m):
            for j in range(n):
                dp[i][j]=dfs(i,j)
                res = max(res,dp[i][j])
        print(dp)
        return res
        
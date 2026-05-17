class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(0,len(dp)):
            dp[i][i] = True
        for i in range(len(dp)-2,-1,-1):
            for j in range(i+1,len(dp)):
                if s[i]==s[j]:
                    dp[i][j]= dp[i+1][j-1] or j-i<=2
        print(dp)
        res = []
        def search(ind,curr):
            if ind == len(s):
                res.append(curr[:])
                return
            for i in range(ind,len(s)):
                c=s[ind:i+1]
                if dp[ind][i]:
                    curr.append(c)
                    search(i+1,curr)
                    curr.pop()
        search(0,[])
        return res

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[False]*(len(s1)+1)
        dp[0] = True
        for i in range(1,len(dp)):
            dp[i] = dp[i-1] and s3[i-1] == s1[i-1]
        for i in range(1,len(s2)+1):
            dp[0] = dp[0] and s2[i - 1] == s3[i - 1]
            for j in range(1,len(dp)):
                m1 =dp[j-1] and s3[i+j-1] == s1[j-1]
                m2=dp[j] and s3[i+j-1] == s2[i-1]
                dp[j]= m1 or m2



        return dp[-1]
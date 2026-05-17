class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*len(s)
        wordset = set(wordDict)
        for j in range(0,len(dp)):
            if s[:j+1] in wordset:
                dp[j] = True
            else:
                for i in range(0,j):
                    if dp[i] and s[i+1:j+1] in wordset:
                        dp[j] = True
                        break
        return dp[-1]
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        using=set()
        res = 0
        while r < len(s):
            if s[r] not in using:
                using.add(s[r])
                res = max(r-l+1,res)
                r+=1
            else:
                using.remove(s[l])
                l+=1
        return res
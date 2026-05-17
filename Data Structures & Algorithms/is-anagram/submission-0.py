from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        d = defaultdict(int)
        for i in range(0,len(s)):
            d[s[i]]+=1
            d[t[i]]-=1
        for x in d.values():
            if x !=0:
                return False
        return True
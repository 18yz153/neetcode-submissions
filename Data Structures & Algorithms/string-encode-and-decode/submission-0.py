class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in range(0,len(strs)):
            res = res + str(len(strs[i]))+'#'+strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        res= []
        length = ''
        while i<len(s):
            if s[i]!='#':
                length=length+s[i]
                i+=1
            else:
                res.append(s[i+1:i+1+int(length)])
                i=i+1+int(length)
                length=''
        return res
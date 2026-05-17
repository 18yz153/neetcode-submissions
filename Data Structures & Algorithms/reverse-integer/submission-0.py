class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            neg = -1
        else:
            neg = 1
        x=abs(x)
        limit = 2**31 - 1
        res = 0
        while x >0:
            lastdight = x %10
            x=x//10
            res = res*10+lastdight
            if res > limit:
                return 0
        return res * neg

        
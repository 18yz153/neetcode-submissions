class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n=-n
            x=1/x
        if n ==0:
            return 1.00
        res = 1
        while n>1:
            if n%2==0:
                n=n>>1
                x=x*x
            else:
                n-=1
                res=res*x
        res =res*x
        return res
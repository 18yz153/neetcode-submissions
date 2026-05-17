class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def search(curr,op,close):
            if len(curr) == 2*n:
                res.append(''.join(curr))
                return
            if op<n:
                curr.append('(')
                search(curr,op+1,close)
                curr.pop()

            if close<op:
                curr.append(')')
                search(curr,op,close+1)
                curr.pop()
        search([],0,0)
        return res

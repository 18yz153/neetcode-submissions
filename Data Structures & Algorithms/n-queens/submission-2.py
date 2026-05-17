class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diag=set()
        subdiag=set()
        col=set()
        res = []
        def search(rows,ind):
            if len(rows) ==n:
                nonlocal res
                strres = [''.join(r) for r in rows]
                res.append(strres)
                return
            i=ind
            for j in range(0,n):
                r = ['.']*n
                r[j] = 'Q'
                if j in col or i-j in diag or i+j in subdiag:
                    continue
                rows.append(r)
                col.add(j)
                diag.add(i-j)
                subdiag.add(i+j)
                search(rows,ind+1)
                rows.pop()
                col.remove(j)
                diag.remove(i-j)
                subdiag.remove(i+j)
        search([],0)
        return res
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        firstrow=any(x==0 for x in matrix[0])
        firstcol = any(x[0]==0 for x in matrix)
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstrow:
            for j in range(n):
                matrix[0][j] = 0
        if firstcol:
            for i in range(m):
                matrix[i][0] = 0

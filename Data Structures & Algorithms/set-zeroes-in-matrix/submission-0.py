class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        colind = []
        rowind= []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==0:
                    rowind.append(i)
                    colind.append(j)
        for i in rowind:
            for j in range(0,len(matrix[0])):
                matrix[i][j]=0
        for i in range(0,len(matrix)):
            for j in colind:
                matrix[i][j]=0
        
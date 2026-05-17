from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n=len(board),len(board[0])
        valid=set()
        direction = [[0,1],[0,-1],[-1,0],[1,0]]
        def dfs(i,j):
            valid.add((i,j))
            for d in direction:
                newi = i + d[0]
                newj = j +d[1]
                if 0<=newi<m and 0<=newj<n and board[newi][newj] == 'O' and (newi,newj) not in valid:
                    dfs(newi,newj)
        for i in range(0,m):
            if board[i][0]== "O":
                dfs(i,0)
            
            if board[i][n-1]== "O":
                dfs(i,n-1)
        for j in range(1,n-1):
            if board[0][j]== "O":
                dfs(0,j)
            
            if board[m-1][j]== "O":
                dfs(m-1,j)
        for i in range(1,m-1):
            for j in range(1,n-1):
                if (i,j) not in valid and board[i][j]=="O":
                    board[i][j]="X"

